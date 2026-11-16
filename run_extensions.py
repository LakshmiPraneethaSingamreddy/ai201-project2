#!/usr/bin/env python3
"""Run the Unit 9 extension scenarios and write a three-run report.

Usage:

    python run_extensions.py
    python run_extensions.py --label unit9
    python run_extensions.py --runs 3

Each scenario in scenarios_extension.py runs once per round. The default
therefore executes 25 cases per round and 75 cases across three rounds.
"""

import argparse
import datetime as dt
import json
import traceback
from pathlib import Path
from unittest.mock import patch

from generate import ModelUnavailable
import scenarios_extension
import serve


ROOT = Path(__file__).parent
LOG_PATH = ROOT / "logs" / "fitfindr.jsonl"

TARGETS = {
    1: "5 of 5",
    2: "5 of 5",
    3: "5 of 5",
    4: "5 of 5",
    5: "5 of 5",
}

SOURCES = {
    1: "serve.py::ask",
    2: "serve.py::ask exception handling",
    3: "serve.py::finish_request_logging",
    4: "serve.py::ask model/API failure handling",
    5: "serve.py::ask validation",
}


def _post(client, scenario):
    """Send one scenario body and return its status, body, and request ID."""
    response = client.post(
        scenario["path"],
        json=scenario["payload"],
    )
    return {
        "status": response.status_code,
        "body": response.get_json(silent=True),
        "request_id": response.headers.get("X-Request-ID"),
    }


def _run_model_failure_case(client, scenario):
    """Make the model dependency fail while using the real agent and route."""
    listing = {
        "id": "simulated_listing",
        "title": "Simulated Listing",
        "price": 25.0,
        "platform": "test-store",
    }
    if scenario["fault"] == "timeout":
        message = "Couldn't reach the model: simulated timeout"
    else:
        message = "The model API returned a simulated failure"

    with (
        patch("agent.call_tool", return_value=[listing]),
        patch(
            "tools.generate",
            side_effect=ModelUnavailable(message),
        ),
    ):
        return _post(client, scenario)


def _run_http_case(scenario):
    """Run an HTTP scenario against the Flask application."""
    client = serve.app.test_client()

    if scenario.get("fault") in {"timeout", "model_failure"}:
        result = _run_model_failure_case(client, scenario)
    else:
        result = _post(client, scenario)

    criterion = scenario["criterion"]
    body = result["body"] if isinstance(result["body"], dict) else {}

    if criterion == 1:
        expected_fields = scenario["expected"]
        passed = (
            result["status"] == scenario["expected_status"]
            and all(
                isinstance(body.get(field), str) and body[field].strip()
                for field in expected_fields
            )
        )
    elif criterion == 2:
        error = body.get("error", "")
        passed = (
            result["status"] == scenario["expected_status"]
            and isinstance(error, str)
            and "timeout" in error.lower()
            and not body.get("fit_card")
        )
    elif criterion == 4:
        error = body.get("error", "")
        passed = (
            result["status"] == scenario["expected_status"]
            and isinstance(error, str)
            and error.strip()
            and "traceback" not in error.lower()
            and not body.get("fit_card")
        )
    elif criterion == 5:
        passed = (
            result["status"] == scenario["expected_status"]
            and result["status"] != 500
            and isinstance(body.get("error"), str)
        )
    else:
        passed = False

    return {
        "passed": passed,
        "actual": result,
        "expected": scenario.get("expected", scenario.get("expected_status")),
        "source": SOURCES[criterion],
    }


def _flush_log_handlers():
    for handler in serve.app.logger.handlers:
        handler.flush()


def _find_log_record(request_id):
    """Find the completed JSONL record for one HTTP request."""
    _flush_log_handlers()
    if not request_id or not LOG_PATH.exists():
        return None

    for line in LOG_PATH.read_text(encoding="utf-8").splitlines():
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if (
            record.get("event") == "request_completed"
            and record.get("request_id") == request_id
        ):
            return record
    return None


def _run_logging_case(scenario):
    """Run one request and verify its completed record is in the JSONL log."""
    client = serve.app.test_client()
    result = _post(client, scenario)
    record = _find_log_record(result["request_id"])
    expected_fields = scenario["expected_log"]["fields"]
    passed = record is not None and all(field in record for field in expected_fields)

    return {
        "passed": passed,
        "actual": {
            "response": result,
            "log_record": record,
        },
        "expected": scenario["expected_log"],
        "source": SOURCES[scenario["criterion"]],
    }


def run_case(scenario):
    """Run one scenario and preserve failures as explicit test results."""
    try:
        if scenario["criterion"] == 3:
            return _run_logging_case(scenario)
        return _run_http_case(scenario)
    except Exception as exc:  # A crashed case must appear in the report.
        return {
            "passed": False,
            "actual": {
                "crashed": f"{type(exc).__name__}: {exc}",
                "traceback": traceback.format_exc(),
            },
            "expected": scenario.get("expected"),
            "source": SOURCES[scenario["criterion"]],
        }


def _format_value(value):
    return json.dumps(value, indent=2, ensure_ascii=True, default=str)


def write_report(rounds, args):
    """Write the summary table and real case output to the results directory."""
    serve.config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    label = f"_{args.label}" if args.label else ""
    path = serve.config.RESULTS_DIR / f"extension_run_{stamp}{label}.md"

    lines = [
        f"# Unit 9 extension run log{f' — {args.label}' if args.label else ''}",
        "",
        f"- Rounds: {len(rounds)}",
        "- Cases per criterion per round: 5",
        f"- Total cases: {len(rounds) * len(scenarios_extension.SCENARIOS)}",
        f"- When: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "| Criterion | Target | "
        + " | ".join(f"Run {i}" for i in range(1, len(rounds) + 1))
        + " | Verdict |",
        "|---|---|"
        + "|".join("---" for _ in rounds)
        + "|---|",
    ]

    summaries = {}
    for criterion in range(1, 6):
        counts = []
        for round_results in rounds:
            results = [
                result
                for result in round_results
                if result["scenario"]["criterion"] == criterion
            ]
            counts.append(
                f"{sum(result['outcome']['passed'] for result in results)}/{len(results)}"
            )
        summaries[criterion] = counts
        verdict = "MET" if all(
            int(count.split("/")[0]) >= int(TARGETS[criterion].split()[0])
            for count in counts
        ) else "MISSED"
        lines.append(
            f"| {criterion}. {SOURCES[criterion]} | {TARGETS[criterion]} | "
            + " | ".join(counts)
            + f" | {verdict} |"
        )

    lines += ["", "## Real output", ""]
    for round_number, round_results in enumerate(rounds, 1):
        lines += [f"### Run {round_number}", ""]
        for result in round_results:
            scenario = result["scenario"]
            lines += [
                f"#### Criterion {scenario['criterion']}: {scenario['name']}",
                "",
                f"- Source: `{result['outcome']['source']}`",
                f"- Pass: `{result['outcome']['passed']}`",
                "- Expected:",
                "```json",
                _format_value(result["outcome"]["expected"]),
                "```",
                "- Actual output:",
                "```json",
                _format_value(result["outcome"]["actual"]),
                "```",
                "",
            ]

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(
        description="Run Unit 9 extension scenarios and write a results report."
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=3,
        help="complete rounds to run (default: 3)",
    )
    parser.add_argument("--label", default="", help="optional report label")
    args = parser.parse_args()

    problems = scenarios_extension.validate()
    if problems:
        raise SystemExit("Invalid extension scenarios:\n- " + "\n- ".join(problems))
    if args.runs < 1:
        raise SystemExit("--runs must be at least 1")

    rounds = []
    for round_number in range(1, args.runs + 1):
        print(f"Starting extension run {round_number}/{args.runs}")
        round_results = []
        for scenario in scenarios_extension.SCENARIOS:
            outcome = run_case(scenario)
            round_results.append({"scenario": scenario, "outcome": outcome})
            status = "PASS" if outcome["passed"] else "FAIL"
            print(f"  {status}: criterion {scenario['criterion']} — {scenario['name']}")
        rounds.append(round_results)

    report_path = write_report(rounds, args)
    print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    main()
