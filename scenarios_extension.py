"""
The Unit 9 extension scenarios.

Each criterion has five distinct test cases. Run each scenario once and
compare the observed response with its expected result.
"""

SCENARIOS = [
    # Criterion 1: valid requests return an outfit and fit card.
    {
        "name": "valid graphic tee request",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "vintage graphic tee under $30"},
        "expected_status": 200,
        "expected": ("outfit_suggestion", "fit_card"),
        "criterion": 1,
    },
    {
        "name": "valid denim jacket request",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "denim jacket under $50"},
        "expected_status": 200,
        "expected": ("outfit_suggestion", "fit_card"),
        "criterion": 1,
    },
    {
        "name": "valid jeans request",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "black jeans size M under $40"},
        "expected_status": 200,
        "expected": ("outfit_suggestion", "fit_card"),
        "criterion": 1,
    },
    {
        "name": "valid cardigan request",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "brown cardigan under $35"},
        "expected_status": 200,
        "expected": ("outfit_suggestion", "fit_card"),
        "criterion": 1,
    },
    {
        "name": "valid hoodie request",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "vintage hoodie under $45"},
        "expected_status": 200,
        "expected": ("outfit_suggestion", "fit_card"),
        "criterion": 1,
    },

    # Criterion 2: timed-out requests return an error instead of crashing.
    {
        "name": "graphic tee timeout",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "vintage graphic tee under $30"},
        "fault": "timeout",
        "expected_status": 500,
        "expected": "timeout in error response",
        "criterion": 2,
    },
    {
        "name": "denim jacket timeout",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "denim jacket under $50"},
        "fault": "timeout",
        "expected_status": 500,
        "expected": "timeout in error response",
        "criterion": 2,
    },
    {
        "name": "jeans timeout",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "black jeans size M under $40"},
        "fault": "timeout",
        "expected_status": 500,
        "expected": "timeout in error response",
        "criterion": 2,
    },
    {
        "name": "cardigan timeout",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "brown cardigan under $35"},
        "fault": "timeout",
        "expected_status": 500,
        "expected": "timeout in error response",
        "criterion": 2,
    },
    {
        "name": "hoodie timeout",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "vintage hoodie under $45"},
        "fault": "timeout",
        "expected_status": 500,
        "expected": "timeout in error response",
        "criterion": 2,
    },

    # Criterion 3: each request creates a completed JSONL log record.
    {
        "name": "graphic tee request is logged",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "vintage graphic tee under $30"},
        "expected_log": {
            "path": "logs/fitfindr.jsonl",
            "event": "request_completed",
            "fields": ("request_id", "status", "duration_ms", "error"),
        },
        "criterion": 3,
    },
    {
        "name": "denim jacket request is logged",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "denim jacket under $50"},
        "expected_log": {
            "path": "logs/fitfindr.jsonl",
            "event": "request_completed",
            "fields": ("request_id", "status", "duration_ms", "error"),
        },
        "criterion": 3,
    },
    {
        "name": "jeans request is logged",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "black jeans size M under $40"},
        "expected_log": {
            "path": "logs/fitfindr.jsonl",
            "event": "request_completed",
            "fields": ("request_id", "status", "duration_ms", "error"),
        },
        "criterion": 3,
    },
    {
        "name": "cardigan request is logged",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "brown cardigan under $35"},
        "expected_log": {
            "path": "logs/fitfindr.jsonl",
            "event": "request_completed",
            "fields": ("request_id", "status", "duration_ms", "error"),
        },
        "criterion": 3,
    },
    {
        "name": "hoodie request is logged",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "vintage hoodie under $45"},
        "expected_log": {
            "path": "logs/fitfindr.jsonl",
            "event": "request_completed",
            "fields": ("request_id", "status", "duration_ms", "error"),
        },
        "criterion": 3,
    },

    # Criterion 4: the selected listing ID reaches suggest_outfit.
    {
        "name": "graphic tee listing ID reaches suggest_outfit",
        "query": "vintage graphic tee under $30",
        "wardrobe": "example",
        "expected": "search_listings ID equals suggest_outfit ID",
        "criterion": 4,
    },
    {
        "name": "denim jacket listing ID reaches suggest_outfit",
        "query": "denim jacket under $50",
        "wardrobe": "example",
        "expected": "search_listings ID equals suggest_outfit ID",
        "criterion": 4,
    },
    {
        "name": "jeans listing ID reaches suggest_outfit",
        "query": "black jeans size M under $40",
        "wardrobe": "example",
        "expected": "search_listings ID equals suggest_outfit ID",
        "criterion": 4,
    },
    {
        "name": "cardigan listing ID reaches suggest_outfit",
        "query": "brown cardigan under $35",
        "wardrobe": "example",
        "expected": "search_listings ID equals suggest_outfit ID",
        "criterion": 4,
    },
    {
        "name": "hoodie listing ID reaches suggest_outfit",
        "query": "vintage hoodie under $45",
        "wardrobe": "example",
        "expected": "search_listings ID equals suggest_outfit ID",
        "criterion": 4,
    },

    # Criterion 5: malformed input returns HTTP 400 instead of HTTP 500.
    {
        "name": "missing query field",
        "method": "POST",
        "path": "/ask",
        "payload": {},
        "expected_status": 400,
        "expected": "error response and no HTTP 500",
        "criterion": 5,
    },
    {
        "name": "empty query string",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": ""},
        "expected_status": 400,
        "expected": "error response and no HTTP 500",
        "criterion": 5,
    },
    {
        "name": "whitespace-only query",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": "   "},
        "expected_status": 400,
        "expected": "error response and no HTTP 500",
        "criterion": 5,
    },
    {
        "name": "null query",
        "method": "POST",
        "path": "/ask",
        "payload": {"query": None},
        "expected_status": 400,
        "expected": "error response and no HTTP 500",
        "criterion": 5,
    },
    {
        "name": "query field omitted in alternate payload",
        "method": "POST",
        "path": "/ask",
        "payload": {"text": "vintage graphic tee under $30"},
        "expected_status": 400,
        "expected": "error response and no HTTP 500",
        "criterion": 5,
    },
]


def validate() -> list[str]:
    """Complain about malformed extension scenarios before running them."""
    problems = []
    counts = {criterion: 0 for criterion in range(1, 6)}

    for i, scenario in enumerate(SCENARIOS, 1):
        criterion = scenario.get("criterion")
        if criterion not in counts:
            problems.append(f"scenario {i} has an invalid criterion")
            continue
        counts[criterion] += 1

        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")
        if criterion in {1, 2, 3, 5}:
            if scenario.get("method") != "POST":
                problems.append(f"scenario {i} must use POST")
            if scenario.get("path") != "/ask":
                problems.append(f"scenario {i} must use /ask")
            if "payload" not in scenario:
                problems.append(f"scenario {i} has no request payload")
        if criterion == 4:
            if not scenario.get("query", "").strip():
                problems.append(f"scenario {i} has no query")
            if scenario.get("wardrobe") != "example":
                problems.append(f"scenario {i} must use the example wardrobe")
        if "expected_status" in scenario and not isinstance(
            scenario["expected_status"], int
        ):
            problems.append(f"scenario {i} has a non-integer expected status")

    for criterion, count in counts.items():
        if count != 5:
            problems.append(
                f"criterion {criterion} has {count} scenarios; expected 5"
            )

    return problems
