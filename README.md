# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does
FitFindr helps a user find a thrifted item and style it with pieces they already own. It parses the user's description, size, and maximum price, then searches the listings for matching items. If no matches are found, it saves a clear message explaining that the user can change the description, size, or price and stops before requesting outfit advice. When a match is found, FitFindr selects the top result, generates one or two outfit suggestions using the user's wardrobe, and creates a fit card that highlights the item, price, platform, and styling idea; if the wardrobe is empty, it provides general styling advice instead.


---

## Tool Inventory
### `search_listings`

- **What it does:** Searches the listings data for items matching the user's description, optional size, and optional maximum price. It ranks matching listings and returns the best matches first.
- **Inputs:** description (str), size (str), max_price(float)
- **Returns:** returns a list of dicts, where each dict has id (str), title(str), description(str), category (str), style_tags (list), size(str), condition (str), price(float), colors(list), brand(str), platform(str) fields
- **When it has nothing:** It returns an empty list

### `suggest_outfit`

- **What it does:** Given the thrifted item and the user's wardrobe, it asks model to suggest one or two outfits for the user.
- **Inputs:** new_item (dict), wardrobe (dict)
- **Returns:** Returns the models response of suggested outfits (str)
- **When it has nothing:** When the wardrobe is empty, it asks the model for general styling ideas instead of using specific wardrobe pieces.

### `create_fit_card`

- **What it does:** Asks the model to write a short, post-ready caption about the thrifted item and suggested outfit.
- **Inputs:** outfit (str), new_item (dict)
- **Returns:** A string containing a two-to-four sentence caption that mentions the item, price, platform, and style.
- **When it has nothing:** When the outfit is empty it return "I need an outfit suggestion before I can create a fit card" without calling the model.

---

## Planning Loop

**Branch rule:** If search_listings returns no results, the agent should let the user know that no matching items were found, explain that they can try changing their search, and stop without calling suggest_outfit. Otherwise, select the first result and call the suggest_outfit function with that item and the wardrobe, and continue to create_fit_card function.

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** Regex extracts an optional size and maximum price,
then removes those constraints and common request phrases from the query to
produce the description.

**What moves through the session:** `parsed` is passed to `search_results`;
the first result becomes `selected_item`, which is passed with `wardrobe` to
`outfit_suggestion`; that suggestion and the item produce `fit_card`.

---

## Sample Run
**One full query**

```
$ python app.py ask 'find me a pair of jeans under $40'

```

     Found:    Straight Leg Black Jeans — Faded — $30.0 on thredUp

     Outfit:   Here are two complete outfits centered around your new Levi's faded black straight-leg jeans, built using pieces exclusively from your wardrobe:

     ### Outfit 1: Casual Grunge (Edgy & Relaxed)
     * **Top:** White ribbed tank top
     * **Outerwear:** Vintage black denim jacket (layered over the tank)
     * **Shoes:** Black combat boots
     * **Accessories:** Black crossbody bag
     * **Styling details:** Tuck the white ribbed tank into the mid-rise, faded black jeans to highlight the waist, throw on the cropped vintage black denim jacket for a tonal denim-on-denim look, and finish with the combat boots and black crossbody bag to lean into the grunge aesthetic.

     ### Outfit 2: Streetwear Sporty (Cozy & Layered)
     * **Top:** Oversized grey crewneck sweatshirt
     * **Shoes:** Chunky white sneakers
     * **Accessories:** Black crossbody bag
     * **Styling details:** Let the oversized grey crewneck hang loosely over the cropped, straight-leg fit of the jeans for a relaxed silhouette. Pair with the chunky white sneakers to add a sporty contrast to the faded black denim, and wear the black crossbody bag to keep your hands free.

     Fit card: Scored these faded black Levi's straight-leg jeans on thredUp for just $30, and they’ve instantly become my go-to for effortless grunge fits. I love styling them with a crisp white tank and combat boots, or dressing them down with an oversized grey crewneck and chunky sneakers. Natural fading gives them that perfectly broken-in vintage look right out of the box.

     2 model calls this session, 1719 prompt + 331 output tokens

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

```
     [{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title':'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with fadedgraphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]

```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

```
     Here are two complete outfits centered around the Vintage Levi's 501 Jeans, built entirely from your wardrobe:

     ### Outfit 1: Casual Streetwear
     * **Base:** Levi's 501 Jeans (Medium Wash)
     * **Top:** White ribbed tank top tucked in
     * **Layer:** Oversized grey crewneck sweatshirt worn over the tank
     * **Footwear:** Chunky white sneakers
     * **Accessories:** Black crossbody bag
     * **Styling details:** Let the oversized grey crewneck contrast with the fitted white tank underneath. Cinch the medium wash denim with the white sneakers for an effortless, everyday streetwear look, and carry the black crossbody bag for hands-free convenience.

     ### Outfit 2: Edgy Vintage Mix
     * **Base:** Levi's 501 Jeans (Medium Wash)
     * **Top:** Black cropped zip hoodie
     * **Outerwear:** Vintage black denim jacket
     * **Footwear:** Black combat boots
     * **Accessories:** Brown leather belt, Black crossbody bag
     * **Styling details:** Use the brown leather belt to define the waist of the jeans. Layer theblack cropped zip hoodie under the slightly cropped vintage black denim jacket for a textured, all-black-on-denim contrast. Finish with the lace-up combat boots to lean into the grunge and vintage aesthetic.
     ```
     $ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

     ```
     Nothing beats a broken-in pair of classic indigo Levi's 501s with just the right amount of knee fading. I love styling these vintage gems with crisp white sneakers for that effortless everyday streetwear look. Snag this pair over on Depop for just $38 before someone else beats youto it!
---

## How I Used AI
**Moment 1**
- *What I asked for:* I asked Copilot to help me implement search_listings according to the project requirements.
- *What came back:* The initial version returned some irrelevant listings because initially it only matched keywords found only in the listings’ descriptions, even when those keywords did not reflect what the user was asking for.
- *What I changed:* I made the matching stricter by requiring keywords to appear in the listing title or style tags before checking the description. Listings with no title or style-tag matches are skipped. This reduced false positives and made the search results more relevant.

**Moment 2**
- *What I asked for:* I asked Copilot to review the acceptance criteria I wrote for FitFindr.
- *What came back:* Copilot pointed out that my third criterion was too general because it did not specify how to verify that the listing found by search_listings was passed correctly to suggest_outfit.
- *What I changed:* I made the criterion more precise by requiring the listing ID returned by search_listings to match the listing ID received by suggest_outfit, which made the state transfer easy to test and verify.

**Moment 3**
- *What I asked for:* I asked Copilot to help me understand how to direct the tool call to MCP servers instead of directly callinf the function.
- *What came back:* CIt helped me understand what is MCP and why it is used and how to call the tool via MCP server.


<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion                                                                       | Target| Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict  |
|---------------------------------------------------------------------------------|-------|-------|-------|-------|-------|-------|----------|
| 1. A matching query completes all three tools                                   | 4 of 5| PASS  | PASS  | PASS  | PASS  | PASS  | MET(5/5) |
| 2. An impossible query stops before the second tool                             | 5 of 5| PASS  | PASS  | PASS  | PASS  | PASS  | MET(5/5) |
| 3. The listing id passed to suggest_outfit is same as output of search_listings | 4 of 5| PASS  | PASS  | PASS  | PASS  | PASS  | MET(5/5) |
| 4. The fit card must contain all required information(TITLE, PRICE, PLATFORM)   | 4 of 5| PASS  | PASS  | PASS  | PASS  | PASS  | MET(5/5) |
| 5. The tool must consider all the user's requirements                           | 4 of 5| PASS  | PASS  | PASS  | PASS  | PASS  | MET(5/5) |

**Real output from one try**, pasted as text, naming the file and function
that produced it:

```
### matching query completes

- Query: `vintage graphic tee under $30`
- Wardrobe: example

     **Try 1**

     - stopped early: no
     - selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
     - search_results: 10

     Outfit suggestion:

     ```
     Here are two complete outfits centered on the vintage-style graphic tee, built entirely from your wardrobe:

     ### Outfit 1: 90s Streetwear Grunge
     * **Top:** Graphic Tee — 2003 Tour Bootleg Style (`lst_006`)
     * **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)
     * **Outerwear:** Vintage black denim jacket (`w_006`)
     * **Shoes:** Chunky white sneakers (`w_007`)
     * **Accessories:** Black crossbody bag (`w_010`)

     **Styling Details:** Let the boxy tee hang loose over the high-waisted baggy jeans for an effortless, relaxed silhouette. Layer the slightly cropped black denim jacket on top to play with proportion and texture. Finish with the chunky white sneakers for contrast and the black crossbody bag for everyday wear.

     ---

     ### Outfit 2: Edgy Monochrome
     * **Top:** Graphic Tee — 2003 Tour Bootleg Style (`lst_006`)
     * **Bottoms:** Wide-leg khaki trousers (`w_002`)
     * **Layer (Optional):** Black cropped zip hoodie (`w_005`) worn open or tied around the waist
     * **Shoes:** Black combat boots (`w_008`)
     * **Accessories:** Brown leather belt (`w_009`)

     **Styling Details:** Tuck or half-tuck the tee into the wide-leg khaki trousers, cinched at the waist with the brown leather belt to break up the earth tones and black. Pair with the black combat boots to lean into the grunge and vintage aesthetic of the shirt. If you need an extra layer, drape the black cropped zip hoodie over your shoulders or tie it around your waist.
     ```

     Fit card:

     ```
     Channel serious 90s grunge with this perfectly worn-in, boxy vintage-style graphic tee that brings instant effortless edge to any wardrobe. Pair it with dark baggy denim and a black denim jacket for an easy streetwear fit, or contrast the faded black wash with khaki trousers and combat boots. Grab this standout piece now for $24 on Depop before it's gone.
     ```

     Trace:

     ```
     [1] search_listings (via MCP)
          in:  {'description': 'vintage graphic tee', 'size': None, 'max_price': 30.0}
          out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Y2K Baby Tee — Butterfly Print, Vintage Band Tee — Faded Grey … +7 more
          →    10 match(es)
     [2] select_item
          out: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
     [3] suggest_outfit
          in:  Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
          out: Here are two complete outfits centered on the vintage-style graphic tee, built entirely from your wardrobe:  #…
     [4] create_fit_card
          in:  ({'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee…
          out: Channel serious 90s grunge with this perfectly worn-in, boxy vintage-style graphic tee that brings instant eff…
     ```

```
```
### impossible query stops early

- Query: `designer ballgown size XXS under $5`
- Wardrobe: example

     **Try 1**

     - stopped early: yes — No matching items were found. Try changing the description, size, or maximum price and search again.
     - selected_item: (none)
     - search_results: 0

     Trace:

     ```
     [1] search_listings (via MCP)
          in:  {'description': 'designer ballgown', 'size': 'XXS', 'max_price': 5.0}
          out: [] (empty)
          →    0 match(es)
     ```

```

```
### empty wardrobe

- Query: `denim jacket under $50`
- Wardrobe: empty

     **Try 1**

     - stopped early: no
     - selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     - search_results: 6

     Outfit suggestion:

     ```
     Here are two wearable, everyday outfit ideas for your light-wash cropped Wrangler denim jacket:

     ### 1. Casual Off-Duty (Sporty & Relaxed)
     * **Top:** A fitted white ribbed tank top or a vintage band tee.
     * **Bottoms:** High-waisted black or dark grey straight-leg sweatpants (or grey fleece joggers).
     * **Shoes:** Retro white leather sneakers (like Adidas Sambas or New Balance).
     * **Accessories:** A black nylon crossbody bag and a silver chain necklace to complement the hardware.

     ### 2. Elevated Denim-on-Denim (Chic & Effortless)
     * **Top:** A classic black or striped long-sleeve cotton turtleneck (tucked in).
     * **Bottoms:** High-waisted, wide-leg beige or khaki chinos to contrast the light denim wash.
     * **Shoes:** Black leather loafers or ankle boots.
     * **Accessories:** A structured brown leather belt, a matching tote bag, and minimalist gold hoop earrings.
     ```

     Fit card:

     ```
     Level up your off-duty rotation with this structured, light-wash Wrangler denim jacket that's practically begging for a vintage band tee and grey joggers. Available right now on Poshmark for just $42, this cropped classic is the ultimate blank canvas for your everyday wardrobe.
     ```

     Trace:

     ```
     [1] search_listings (via MCP)
          in:  {'description': 'denim jacket', 'size': None, 'max_price': 50.0}
          out: 6 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +3 more
          →    6 match(es)
     [2] select_item
          out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     [3] suggest_outfit
          in:  Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
          out: Here are two wearable, everyday outfit ideas for your light-wash cropped Wrangler denim jacket:  ### 1. Casual…
     [4] create_fit_card
          in:  ({'id': 'lst_007', 'title': 'Denim Jacket — Light Wash, Cropped', 'description': 'Cropped denim jacket in a li…
          out: Level up your off-duty rotation with this structured, light-wash Wrangler denim jacket that's practically begg…
     ```

```
```
### the top listing found is passed to suggest_outfit

- Query: `denim jacket under $50`
- Wardrobe: example

     **Try 1**

     - stopped early: no
     - selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     - search_results: 6

     Outfit suggestion:

     ```
     Here are two outfits built around your new Wrangler cropped light-wash denim jacket, using pieces entirely from your existing wardrobe:

     ### Outfit 1: Double Denim Streetwear
     *Play with denim contrast by pairing the light-wash jacket with darker bottoms.*

     * **Top:** White ribbed tank top (`w_003`) tucked in to highlight the cropped length of the jacket.
     * **Bottoms:** Baggy straight-leg jeans in dark blue/indigo (`w_001`).
     * **Shoes:** Chunky white sneakers (`w_007`).
     * **Accessories:** Black crossbody bag (`w_010`).
     * **Styling Detail:** Let the contrast between the light-wash jacket and the dark, high-waisted baggy jeans create a balanced streetwear silhouette, finished cleanly with crisp white sneakers.

     ---

     ### Outfit 2: Casual Earth Tones
     *Contrast the cool light blue of the jacket with warm, neutral tones.*

     * **Top:** Oversized grey crewneck sweatshirt (`w_004`) layered underneath for a cozy, textured look.
     * **Bottoms:** Wide-leg khaki trousers (`w_002`) worn with the brown leather belt (`w_009`).
     * **Shoes:** Black combat boots (`w_008`).
     * **Accessories:** Black crossbody bag (`w_010`).
     * **Styling Detail:** The structured, cropped light-wash denim jacket adds great shape on top of the oversized grey crewneck, while the khaki trousers and combat boots ground the outfit with a mix of minimal and grunge elements.
     ```

     Fit card:

     ```
     This vintage Wrangler cropped denim jacket is the ultimate versatile layering piece, featuring structured shoulders and a dreamy light wash. Grab it on Poshmark for just $42 to anchor your spring wardrobe. Style it double-denim with indigo jeans and crisp white sneakers, or layer it over a grey crewneck and khaki trousers for a cool streetwear twist.
     ```

     Trace:

     ```
     [1] search_listings (via MCP)
          in:  {'description': 'denim jacket', 'size': None, 'max_price': 50.0}
          out: 6 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +3 more
          →    6 match(es)
     [2] select_item
          out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     [3] suggest_outfit
          in:  Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
          out: Here are two outfits built around your new Wrangler cropped light-wash denim jacket, using pieces entirely fro…
     [4] create_fit_card
          in:  ({'id': 'lst_007', 'title': 'Denim Jacket — Light Wash, Cropped', 'description': 'Cropped denim jacket in a li…
          out: This vintage Wrangler cropped denim jacket is the ultimate versatile layering piece, featuring structured shou…
     ```
```

```
### fit card has all required information

- Query: `denim jacket under $50`
- Wardrobe: example

     **Try 1**

     - stopped early: no
     - selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     - search_results: 6

     Outfit suggestion:

     ```
     Here are two complete outfits built around your new Wrangler cropped light-wash denim jacket, using pieces entirely from your wardrobe:

     ### Outfit 1: Denim-on-Denim Streetwear
     * **The Look:** A high-contrast take on the Canadian tuxedo, leaning into the jacket’s streetwear potential.
     * **Top:** White ribbed tank top (**w_003**) tucked in to highlight the waist.
     * **Bottoms:** Baggy straight-leg jeans, dark wash (**w_001**) for a sharp light-over-dark denim contrast.
     * **Shoes:** Chunky white sneakers (**w_007**).
     * **Accessories:** Black crossbody bag (**w_010**).

     ### Outfit 2: Casual Earth Tones
     * **The Look:** A relaxed, balanced everyday outfit mixing crisp light blue denim with warm neutrals.
     * **Top:** White ribbed tank top (**w_003**).
     * **Bottoms:** Wide-leg khaki trousers (**w_002**).
     * **Accessories:** Brown leather belt (**w_009**) to pull in the earth tones.
     * **Shoes:** Chunky white sneakers (**w_007**) to keep the look fresh and casual. *(Optional layering detail: If it gets chilly, layer the oversized grey crewneck sweatshirt (**w_004**) underneath the cropped jacket, letting the hem peek out the bottom).*
     ```

     Fit card:

     ```
     Scored this vintage Wrangler light blue cropped denim jacket on Poshmark for just $42, and it’s the ultimate blank canvas for custom styling with its structured shoulders and classic streetwear vibe. I'm pairing it today in a high-contrast Canadian tuxedo with dark baggy jeans, a white ribbed tank, and chunky sneakers, or dressing it down with wide-leg khaki trousers and a brown leather belt for an easy earth-toned look.
     ```

     Trace:

     ```
     [1] search_listings (via MCP)
          in:  {'description': 'denim jacket', 'size': None, 'max_price': 50.0}
          out: 6 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +3 more
          →    6 match(es)
     [2] select_item
          out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     [3] suggest_outfit
          in:  Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
          out: Here are two complete outfits built around your new Wrangler cropped light-wash denim jacket, using pieces ent…
     [4] create_fit_card
          in:  ({'id': 'lst_007', 'title': 'Denim Jacket — Light Wash, Cropped', 'description': 'Cropped denim jacket in a li…
          out: Scored this vintage Wrangler light blue cropped denim jacket on Poshmark for just $42, and it’s the ultimate b…
     ```

```

```
### returned listings consider user preferences

- Query: `denim jacket under $50`
- Wardrobe: example

     **Try 1**

     - stopped early: no
     - selected_item: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     - search_results: 6

     Outfit suggestion:

     ```
     Here are two complete outfits built around your new Wrangler cropped light-wash denim jacket, using pieces entirely from your wardrobe:

     ### Outfit 1: Canadian Tuxedo (Streetwear Vibe)
     * **Top:** White ribbed tank top
     * **Bottoms:** Baggy straight-leg jeans, dark wash (with the Brown leather belt)
     * **Shoes:** Chunky white sneakers
     * **Accessories:** Black crossbody bag
     * **Styling details:** Pairing the light wash jacket with dark wash jeans creates a sharp, high-contrast double-denim look. Wear the fitted white ribbed tank tucked into the high-waisted baggy jeans, let the jacket's structured shoulders pop over top, and finish with chunky sneakers and the black crossbody bag.

     ### Outfit 2: Contrast & Comfort (Casual Earth Tones)
     * **Top:** Oversized grey crewneck sweatshirt (worn underneath)
     * **Bottoms:** Wide-leg khaki trousers
     * **Shoes:** Black combat boots
     * **Accessories:** Black crossbody bag
     * **Styling details:** Layer the cropped light-wash denim jacket directly over the oversized grey crewneck. Because the grey sweatshirt drops below the hip, the cropped length of the Wrangler jacket will create a cool, structured proportion against the wide-leg khaki trousers. Ground the look with black combat boots to add an edge to the softer earth tones.
     ```

     Fit card:

     ```
     Scored this vintage Wrangler light-wash denim jacket for just $42 on Poshmark, and it’s the ultimate blank canvas for layering. I love how the structured shoulders pop whether I'm styling it for a high-contrast double-denim streetwear look or throwing it over an oversized crewneck with khakis. Grab it before it's gone!
     ```

     Trace:

     ```
     [1] search_listings (via MCP)
          in:  {'description': 'denim jacket', 'size': None, 'max_price': 50.0}
          out: 6 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +3 more
          →    6 match(es)
     [2] select_item
          out: Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
     [3] suggest_outfit
          in:  Denim Jacket — Light Wash, Cropped ($42.0, poshmark)
          out: Here are two complete outfits built around your new Wrangler cropped light-wash denim jacket, using pieces ent…
     [4] create_fit_card
          in:  ({'id': 'lst_007', 'title': 'Denim Jacket — Light Wash, Cropped', 'description': 'Cropped denim jacket in a li…
          out: Scored this vintage Wrangler light-wash denim jacket for just $42 on Poshmark, and it’s the ultimate blank can…
     ```
```
File: run_eval.py ,Function:write_report()

---

## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion                                                                    | Target | Verdict | How I decided |
|---|------------------------------------------------------------------------------|--------|---------|---------------|
| 1 | A matching query completes all three tools                                   | 4 of 5 |   MET   | The matching query returned listings, generated outfit suggestions based on the top listing, and created fit cards successfully in all 5 attempts. |
| 2 | An impossible query stops before the second tool                             | 5 of 5 |   MET   | The impossible query returned the message, "No matching items were found. Try changing the description, size, or maximum price and search again", and stopped before calling suggest_outfit function. |
| 3 | The listing id passed to suggest_outfit is same as output of search_listings | 4 of 5 |   MET   | For each try the only top listing returned from the search_listings is passed to the suggest_outfits function |
| 4 | The fit card must contain all required information(TITLE, PRICE, PLATFORM)   | 4 of 5 |   MET   | For every fit card the tool generated, it included the title of the listing, price and platform where it is available |
| 5 | The tool must consider all the user's requirements                           | 4 of 5 |   MET   | For every try, it considered the max_price given and suggested the outfits only under the max_price |

**Diagnoses**
All of my criteria have been met. I think they are generally strong, but in future I like to replace Criterion 4, which checks whether the fit card includes the title, price, and platform. While that is still a useful criterion, I think a stronger alternative would be:"For at least 4 out of 5 queries containing a description, size, and maximum price, parse_query() correctly extracts all supported fields".I feel like this criterion would directly test the query-parsing logic and provide more meaningful coverage of how the agent understands user requests. 


---

## Loop Trace
**Happy path**

```

 python app.py ask ' cardigan under $50'
[1] search_listings (via MCP)
      in:  {'description': 'cardigan', 'size': None, 'max_price': 50.0}
      out: 1 items: Knit Cardigan — Chunky Brown
      →    1 match(es)
[2] select_item
      out: Knit Cardigan — Chunky Brown ($35.0, depop)
[3] suggest_outfit
      in:  Knit Cardigan — Chunky Brown ($35.0, depop)
      out: Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrob…
[4] create_fit_card
      in:  ({'id': 'lst_008', 'title': 'Knit Cardigan — Chunky Brown', 'description': 'Super cozy oversized cardigan. Ear…
      out: Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled…

  Found:    Knit Cardigan — Chunky Brown — $35.0 on depop

  Outfit:   Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:

### Outfit 1: Casual & Minimalist Earth Tones
* **Top:** White ribbed tank top
* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)
* **Bottoms:** Wide-leg khaki trousers
* **Accessories:** Brown leather belt
* **Shoes:** Chunky white sneakers
* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.

### Outfit 2: Contrast Denim & Edge
* **Top:** White ribbed tank top
* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)
* **Bottoms:** Baggy straight-leg jeans, dark wash
* **Shoes:** Black combat boots
* **Accessories:** Black crossbody bag
* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.

  Fit card: Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.

2 model calls this session, 1741 prompt + 316 output tokens
```

**Empty search**

```
 python app.py ask 'vintage saree under $1'
[1] search_listings (via MCP)
      in:  {'description': 'vintage saree', 'size': None, 'max_price': 1.0}
      out: [] (empty)
      →    0 match(es)

  No matching items were found. Try changing the description, size, or maximum price and search again.

0 model calls this session
```

**On the MCP move:** I have re-written the function call to search_listings in run_eval.py, so that it is called through MCP server instead of calling it directly. The only change is that how the answer is returned from the search_listings function and other than that, I have not notived any chnages and have not faced any problems for calling the search_listings function through MCP.



---

## The Improvement

**What I changed:** All of my tests passed before and everything is working fine. So, I have not changed anything.



### Run Log — After

| # | Criterion                                                                    | Target | Verdict | How I decided |
|---|------------------------------------------------------------------------------|--------|---------|---------------|
| 1 | A matching query completes all three tools                                   | 4 of 5 |   MET   | The matching query returned listings, generated outfit suggestions based on the top listing, and created fit cards successfully in all 5 attempts. |
| 2 | An impossible query stops before the second tool                             | 5 of 5 |   MET   | The impossible query returned the message, "No matching items were found. Try changing the description, size, or maximum price and search again", and stopped before calling suggest_outfit function. |
| 3 | The listing id passed to suggest_outfit is same as output of search_listings | 4 of 5 |   MET   | For each try the only top listing returned from the search_listings is passed to the suggest_outfits function |
| 4 | The fit card must contain all required information(TITLE, PRICE, PLATFORM)   | 4 of 5 |   MET   | For every fit card the tool generated, it included the title of the listing, price and platform where it is available |
| 5 | The tool must consider all the user's requirements                           | 4 of 5 |   MET   | For every try, it considered the max_price given and suggested the outfits only under the max_price |
---

## What's Still Broken
After making this fix, all of my criteria passed, and I ran the tests multiple times to confirm that everything continued to work correctly.



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
