"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import json
import re

import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────
_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "can",
    "could", "for", "from", "has", "have", "how", "if", "in", "into",
    "is", "it", "its", "just", "like", "look", "looking", "more", "need",
    "not", "of", "on", "one", "or", "out", "over", "size", "so", "that",
    "the", "their", "them", "there", "these", "they", "this", "those",
    "to", "too", "under", "up", "very", "want", "wanted", "was", "we",
    "were", "what", "when", "where", "which", "who", "why", "with",
    "would", "you", "your"
}

def _keywords(text:str) -> set[str]:
    "Lowercase words worth matching on, stopwords removed"
    words = re.findall(r"[a-z0-9]+",(text or "").lower())
    return {w for w in words if w not in _STOPWORDS and len(w) > 1}

def _size_tokens(size:str) -> set[str]: #for figuring out what size does the user is looking for
    cleaned = re.sub(r"\([^)]*\)", "", size or "")
    parts = [p.strip().upper() for p in cleaned.split("/")]
    return {p for p in parts if p}

def _size_matches(wanted:str, listing_size:str) -> bool:
    if not wanted:
        return True
    listing_tokens = _size_tokens(listing_size)
    if any(token.startswith("ONE SIZE") for token in listing_tokens):
        return True
    return bool(_size_tokens(wanted) & listing_tokens)


def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, and optionally a
    size and a price ceiling.

    This is the tool that doesn't call the model, which makes it the easiest one
    to test and the one to move onto MCP in unit 4.

    Args:
        description: keywords describing what the user wants
                     (e.g. "vintage graphic tee").
        size:        a size string to filter by, or None to skip size filtering.
                     Match case-insensitively — "M" should match "S/M".

                     ⚠️ Read the sizes in the data before you reach for a plain
                     substring test. `"s" in "us 9"` is True, and so is
                     `"l" in "xl"`. A filter that returns shoes when someone
                     asked for a small top reads like a broken search, and it
                     will quietly cost you in unit 4 when you test criterion 1.
                     What counts as a size match is part of your spec — decide
                     it and write it into your Tool Inventory.
        max_price:   maximum price, inclusive, or None to skip price filtering.

    Returns:
        A list of matching listing dicts, best match first.
        **Returns an empty list when nothing matches — an empty list, not None,
        and not an exception.** Your loop branches on this.

    Each listing dict has these fields:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Note that `brand` is None for most listings. That is deliberate and
    realistic — thrift listings often have no brand. If something you write
    assumes a brand is always there, you will find out in unit 4.

    TODO:
        1. Load every listing with load_listings().
        2. Filter by max_price and by size, when each is provided.
        3. Score what's left by keyword overlap with `description`.
        4. Drop anything scoring zero.
        5. Sort by score, highest first, and return the listing dicts —
           at most config.SEARCH_RESULT_LIMIT of them.

    Test it from a terminal before you move on:
        python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
    """
    wanted_keywords = _keywords(description)
    matches: list[dict] = []

    for listing in load_listings():
        if max_price is not None:
            try:
                if float(listing.get("price", 0)) > float(max_price):
                    continue
            except (TypeError, ValueError):
                continue

        if size is not None and not _size_matches(size, listing.get("size", "")):
            continue

        primary_text = " ".join([
            listing.get("title", ""),
            " ".join(listing.get("style_tags", [])),
        ])
        primary_score = len(wanted_keywords & _keywords(primary_text))

        if primary_score > 0:
            description_score = len(
                wanted_keywords & _keywords(listing.get("description", ""))
            )
            listing["_match_score"] = (primary_score * 2) + description_score
            matches.append(listing)

    matches.sort(key=lambda item: (-item["_match_score"], item.get("price", float("inf"))))

    for listing in matches:
        listing.pop("_match_score", None)

    return matches[: config.SEARCH_RESULT_LIMIT]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """
    Given a thrifted item and the user's wardrobe, suggest one or two outfits.

    This one calls the model, through `generate()`. You don't need to think
    about rate limits — the adapter handles pacing for you.

    Args:
        new_item: a listing dict — the item the user is considering.
        wardrobe: a wardrobe dict with an 'items' key holding a list of items.
                  **It may be empty.** Handle that.

    Returns:
        A non-empty string with outfit suggestions.
        With an empty wardrobe, return general styling advice rather than
        raising or returning "". Unit 4 has you trigger the empty wardrobe on
        purpose, so decide now what it should do.

    TODO:
        1. Check whether wardrobe['items'] is empty.
        2. If it is, ask the model for general styling ideas for this item.
        3. If it isn't, format the wardrobe items into the prompt and ask for
           specific combinations naming pieces the user already owns.
        4. Return the model's response.

    Test it from a terminal before you move on:
        python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
    """
    wardrobe_items = wardrobe.get("items", [])
    item_details = json.dumps(new_item, indent=2, sort_keys=True)

    if not wardrobe_items:
        prompt = f"""
            Suggest one or two wearable outfit ideas for this thrifted item:

            {item_details}

            The user has not entered any wardrobe items yet, so give general styling
            advice using pieces someone could reasonably own or shop for. Mention colors,
            layers, shoes, and accessories where useful. Be concise and practical.
            """.strip()
    else:
        wardrobe_details = json.dumps(wardrobe_items, indent=2, sort_keys=True)
        prompt = f"""
            Suggest one or two complete outfits centered on this thrifted item:

            {item_details}

            Build the outfits from the user's existing wardrobe below whenever possible.
            Name the exact wardrobe pieces you use, and add practical styling details such
            as colors, layers, shoes, or accessories. Do not invent wardrobe items that
            are not listed. Be concise and practical.

            User wardrobe:
            {wardrobe_details}
            """.strip()

    return generate(prompt)


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    This calls the model too.

    Args:
        outfit:   the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If `outfit` is empty or whitespace, return a descriptive message rather
        than raising.

    The caption should read like a real post rather than a product description,
    mention the item and its price and platform once each, and be specific about
    the vibe.

    It should also come out **differently for different inputs**. If you run
    this three times on the same item and get three word-for-word identical
    strings, it's one of two things, and both are near the top of `config.py`:

        • CACHE_ENABLED — the adapter handed back an answer it already had
        • TEMPERATURE   — at 0.0 the model gives the same words every time

    TODO:
        1. Guard against an empty or whitespace-only `outfit`.
        2. Build a prompt with the item details and the outfit.
        3. Call generate() and return the response.

    Test it from a terminal before you move on:
        python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
    """
    if not outfit or not outfit.strip():
        return "I need an outfit suggestion before I can create a fit card."

    item_details = json.dumps(new_item, indent=2, sort_keys=True)
    prompt = f"""
        Write a short, post-ready fit card caption for this thrifted item and
        the suggested outfit below.

        Item details:
        {item_details}

        Outfit:
        {outfit.strip()}

        Write exactly two to four sentences. Make it sound natural and specific
        to the item's style and colors, rather than like a product listing.
        Mention the item, its price, and its platform once each. Return only
        the caption, with no title, quotation marks, or extra explanation.
        """.strip()

    return generate(prompt)
