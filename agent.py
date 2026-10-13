"""
The FitFindr planning flow.

This is the file that makes FitFindr an agent rather than a script. It decides
which tool to run next based on what the last one returned.

If the search returns no listings, the flow stops before calling the
model-backed tools. **That branch is the graded part of this unit.**

Build and test your three tools in `tools.py` first. Then come here.

    python agent.py          runs both example paths below
"""

import re
import trace
from tools import search_listings, suggest_outfit, create_fit_card
from generate import ModelUnavailable
from mcp_client import call_tool


# ── session state ─────────────────────────────────────────────────────────────

def new_session(query: str, wardrobe: dict) -> dict:
    """
    A fresh session for one user interaction.

    The session is the single source of truth for a run. Every tool result goes
    in here, and the next tool reads it back out.

    You could pass values straight from one call to the next. It would work,
    and you would not be able to test it — you can't print a variable you have
    already overwritten. Going through the session is what makes the state
    visible, and unit 4 has you write a criterion about exactly that.

    Add fields if you need them.
    """
    return {
        "query": query,              # what the user typed
        "parsed": {},                # description / size / max_price you pulled out of it
        "search_results": [],        # everything search_listings returned
        "selected_item": None,       # the one you chose — goes into suggest_outfit
        "wardrobe": wardrobe,        # the user's wardrobe
        "outfit_suggestion": None,   # what suggest_outfit returned
        "fit_card": None,            # what create_fit_card returned
        "error": None,               # set when the run ended early
    }


# ── planning flow ────────────────────────────────────────────────────────────

def parse_query(query: str) -> dict:
    """Extract the description, requested size, and price limit from a query."""
    price_match = re.search(
        r"\b(?:under|below|less than|up to|max(?:imum)?(?: price)?)"
        r"\s*\$?\s*(\d+(?:\.\d+)?)",
        query,
        flags=re.IGNORECASE,
    )
    size_match = re.search(
        r"\bsize\s*[:=]?\s*([A-Za-z0-9]+(?:\s*/\s*[A-Za-z0-9]+)?)",
        query,
        flags=re.IGNORECASE,
    )

    max_price = float(price_match.group(1)) if price_match else None
    size = size_match.group(1).strip() if size_match else None
    description = query
    if price_match:
        description = description.replace(price_match.group(0), "")
    if size_match:
        description = description.replace(size_match.group(0), "")
    description = re.sub(
        r"\b(?:looking for|i want|i need|find me|show me)\b",
        "",
        description,
        flags=re.IGNORECASE,
    )
    description = re.sub(r"\s+", " ", description).strip(" ,")

    return {
        "description": description,
        "size": size,
        "max_price": max_price,
    }


def run_agent(query: str, wardrobe: dict) -> dict:
    """
    Run the planning flow once and return the finished session.

    The search result branch stops before the model-backed tools when no
    listings match the parsed query.
    """
    session = new_session(query, wardrobe)
    count = 1

    count+=1
    trace.check_iterations(count)
    parsed = parse_query(query)
    session["parsed"] = parsed

    count += 1
    trace.check_iterations(count)
    #results = search_listings(parsed["description"], parsed["size"], parsed["max_price"])
    results = call_tool("search_listings", {"description": parsed["description"], "size": parsed["size"], "max_price": parsed["max_price"]})
    session["search_results"] = results
    trace.step("search_listings (via MCP)", inputs=str(parsed), returned=results,
           note=f"{len(results)} match(es)")

    if not session["search_results"]:
        session["error"] = (
            "No matching items were found. Try changing the description, "
            "size, or maximum price and search again."
        )
        return session

    session["selected_item"] = results[0]
    trace.step("select_item", returned = session["selected_item"])
    session["outfit_suggestion"] = suggest_outfit(
        session["selected_item"],
        session["wardrobe"],
    )
    trace.step("suggest_outfit", inputs=session["selected_item"],
           returned=session["outfit_suggestion"])
    session["fit_card"] = create_fit_card(
        session["outfit_suggestion"],
        session["selected_item"],
    )
    trace.step("create_fit_card", inputs=(session["selected_item"], session["fit_card"]),
           returned=session["fit_card"])
    return session


# ── running it directly ───────────────────────────────────────────────────────

def _show(session: dict) -> None:
    if session["error"]:
        print(f"  stopped: {session['error']}")
        print(f"  fit_card is {session['fit_card']!r} — it should still be None here")
        return

    item = session["selected_item"] or {}
    print(f"  found:    {item.get('title')} — ${item.get('price')} on {item.get('platform')}")
    print(f"  outfit:   {session['outfit_suggestion']}")
    print(f"  fit card: {session['fit_card']}")


if __name__ == "__main__":
    from utils.data_loader import get_example_wardrobe

    print("=== A query the data can match ===")
    _show(run_agent(
        query="looking for a vintage graphic tee under $30",
        wardrobe=get_example_wardrobe(),
    ))

    print("\n=== A query it can't ===")
    _show(run_agent(
        query="designer ballgown size XXS under $5",
        wardrobe=get_example_wardrobe(),
    ))

    print(
        "\nThe second one should stop before the fit card. If both paths look "
        "the same,\nthe branch isn't doing anything yet."
    )
