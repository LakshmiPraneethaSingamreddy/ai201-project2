# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools
Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.
**Why this target:**
My search is based entirely on keyword matching across the listing title,
style tags, and description, so some valid queries may use phrasing that does
not overlap with the listing data.
---

## 2. An impossible query stops before the second tool
Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.
**Why this target:**
Because an empty search result means there is no thrifted item to pass to
suggest_outfit function. The agent should therefore stop before calling that tool in the all 5 of 5 tries and return a message telling the user what to change.

---

## 3. Something about state
In at least 4 of 5 successful runs, the listing ID returned by
`search_listings` must be the same listing ID passed to "suggest_outfit" function.
**Why this target:**
This checks that the listing found by the search is the same listing passed to the next tool. If the search finds nothing, the agent stops before calling suggest_outfit, so that run is not included in the state comparison.

---

## 4. Something about the fit card
In at least 4 of 5 fit-card runs, the returned caption must mention the
selected item's title, its price, and its platform, and each of those three
details must appear exactly once.
**Why this target:**
The fit card should include the selected item's identifying details, price, and
platform exactly once so it reads like a natural post rather than a repeated
product description.


---

## 5. Your choice
In at least 4 of 5 searches where the user provides a `max_price` or `size`,
every returned listing must satisfy each provided filter: its price must be at
or below `max_price`, and its size must match the requested size.
**Why this target:**
`search_listings` must apply the provided price and size filters in addition to
the description keywords, so it does not return a listing that matches the
style description but violates the user's price ceiling or requested size.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
