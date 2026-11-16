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


<!-- ═══════════════════════ UNIT 9 — THE EXTENSION ═══════════════════════

    
     ═══════════════════════════════════════════════════════════════════ -->

---
## Capstone
**System I Chose:** FirFindr
**The Shape:** I chose Shape B because I want to make FitFindr handle situations where something goes wrong instead of only working when everything goes perfectly. I will add failure handling for problems like invalid input, an unavailable MCP server, model/API errors, timeouts, and rate limits. I will also deploy the agent through the existing HTTP server and add logging and timing so I can see what happened during each request. My goal is for the deployed system to return clear errors, avoid continuing with incomplete results, and record enough information to measure how it behaves on both successful and failed requests.

**Out of Scope:** I am not adding a second retrieval strategy or changing how listings are ranked. I am not rebuilding the user interface or creating a separate frontend. I am also not adding more outfit-generation features; I am just focusing on making the existing flow reliable when failures occur.

**Instrumentation:**


I cloned the repository into a new folder and followed `RUNNING.md`. I created the virtual environment, installed the requirements, configured `.env`, started the local server with `python serve.py`, and tested both successful and rejected requests.

Each request writes a structured JSON record to
`logs/fitfindr.jsonl`.

The records include:

- `timestamp`
- `query` — the request input
- `status` — the HTTP result
- `duration_ms` — request duration
- `search_results`
- `model_calls`
- `error`

The  ten successful records from a session are:

```json

{"timestamp": "2026-11-16T17:35:30.292110+00:00", "level": "INFO", "event": "request_started", "request_id": "335760dab956", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:35:31.870701+00:00", "level": "INFO", "event": "request_completed", "request_id": "335760dab956", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 1578.88, "search_results": 10, "model_calls": 0, "error": false}

{"timestamp": "2026-11-16T17:37:53.236886+00:00", "level": "INFO", "event": "request_started", "request_id": "d9b2566855d6", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:01.605263+00:00", "level": "INFO", "event": "request_completed", "request_id": "d9b2566855d6", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 8363.06, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:02.620395+00:00", "level": "INFO", "event": "request_started", "request_id": "1dae05d6bdaa", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:08.579033+00:00", "level": "INFO", "event": "request_completed", "request_id": "1dae05d6bdaa", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 5958.64, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:09.589926+00:00", "level": "INFO", "event": "request_started", "request_id": "13fa23463365", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:15.017956+00:00", "level": "INFO", "event": "request_completed", "request_id": "13fa23463365", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 5428.2, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:16.033224+00:00", "level": "INFO", "event": "request_started", "request_id": "290cf9c1308c", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:21.207493+00:00", "level": "INFO", "event": "request_completed", "request_id": "290cf9c1308c", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 5173.21, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:22.228982+00:00", "level": "INFO", "event": "request_started", "request_id": "84ae07cb134a", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:26.100755+00:00", "level": "INFO", "event": "request_completed", "request_id": "84ae07cb134a", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 3874.27, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:27.111376+00:00", "level": "INFO", "event": "request_started", "request_id": "6ada638aca63", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:32.024737+00:00", "level": "INFO", "event": "request_completed", "request_id": "6ada638aca63", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 4910.01, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:33.031320+00:00", "level": "INFO", "event": "request_started", "request_id": "9afe21061e69", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:36.856866+00:00", "level": "INFO", "event": "request_completed", "request_id": "9afe21061e69", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 3826.22, "search_results": 10, "model_calls": 1, "error": true}

{"timestamp": "2026-11-16T17:38:37.872053+00:00", "level": "INFO", "event": "request_started", "request_id": "e0720d62dfca", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:38:43.315742+00:00", "level": "INFO", "event": "request_completed", "request_id": "e0720d62dfca", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 5443.86, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:38:44.324388+00:00", "level": "INFO", "event": "request_started", "request_id": "ec083718e2fe", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:39:01.237112+00:00", "level": "INFO", "event": "request_completed", "request_id": "ec083718e2fe", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 16918.81, "search_results": 10, "model_calls": 2, "error": false}

{"timestamp": "2026-11-16T17:39:02.260789+00:00", "level": "INFO", "event": "request_started", "request_id": "fd8f1819e5ca", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T17:39:06.783122+00:00", "level": "INFO", "event": "request_completed", "request_id": "fd8f1819e5ca", "method": "POST", "path": "/ask", "query": "vintage graphic tee under $30", "status": 200, "duration_ms": 4523.17, "search_results": 10, "model_calls": 2, "error": false}

```

**failed request:**
The rejected empty-query request returned HTTP 400 and created a structured failure record in `logs/fitfindr.jsonl`.

```json
curl.exe -X POST http://localhost:5000/ask -H "Content-Type: application/json" -d '{}'

     
{"timestamp": "2026-11-16T18:05:07.811658+00:00", "level": "INFO", "event": "request_started", "request_id": "23d7b4f73a84", "method": "POST", "path": "/ask"}

{"timestamp": "2026-11-16T18:05:07.811658+00:00", "level": "INFO", "event": "request_completed", "request_id": "23d7b4f73a84", "method": "POST", "path": "/ask", "query": "", "status": 400, "duration_ms": 0.35, "search_results": "-", "model_calls": 0, "error": true}
```

**What It Costs:**

FitFindr run costs  are approximately **6.44 seconds of wall-clock compute time**.

I measured this by disabling the response cache with: AI201_CACHE=0 so that for every request the model will be called instead of returning answer from cache. Then I  ran ten successful requests and averaged their duration_ms values from the ten request_completed records in logs/fitfindr.jsonl.


     $successful = Get-Content .\logs\fitfindr.jsonl | ForEach-Object {
     >>     $_ | ConvertFrom-Json
     >> } | Where-Object {
     >>     $_.event -eq "request_completed" -and $_.status -eq 200
     >> } | Select-Object -Last 10
     >> 
     >> $successful | Measure-Object -Property duration_ms -Average

Output: 

     Count    : 10
     Average  : 6441.945
     Sum      : 
     Maximum  : 
     Minimum  : 
     Property : duration_ms


The measured average was 6441.945 milliseconds, which is approximately 6.44 seconds per run. This is measured runtime, not a dollar estimate.

For 100 people making one request each day, the measured runtime would be:

```text
100 requests × 6.441945 seconds per request = 644.1945 seconds
644.1945 seconds ÷ 60 = 10.74 minutes of wall-clock compute time per day
```

I cannot calculate a dollar amount from this measurement alone because it
measures runtime, not provider pricing or token charges.

**RUN LOG BEFORE:**

 I created five test cases for each criterion in `scenarios_extension.py`. I ran all of the tests using `run_extensions.py`, and the results were saved in the `results` folder.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. For all 5 of 5 valid requests, the system returns a non-empty complete outfit suggestion and non-empty fit card. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. For all 5 of 5 time out requests, the system returns a clear error message instead of crashing or returning an incomplete result. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. For all 5 of 5 requests, every output appears in log file.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. In at least 4 of 5 successful runs, the listing ID returned by search_listings matches the listing ID passed to suggest_outfit.| 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. For all 5 of 5 cases, malformed input returns HTTP 400 instead of HTTP 500. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |


Criterion 1: valid denim jacket request

     - Source: `serve.py::ask`
     - Pass: `True`
     - Expected:
     ```json
     [
     "outfit_suggestion",
     "fit_card"
     ]
     ```
     - Actual output:
     ```json
     {
     "status": 200,
     "body": {
     "error": null,
     "fit_card": "Scored this vintage Wrangler cropped denim jacket on Poshmark for just $42, and it\u2019s the ultimate blank canvas for layering. I love pairing the light wash with dark baggy denim and fresh white sneakers for an effortless streetwear vibe. It also looks amazing thrown over an oversized grey crewneck and khaki trousers for an easy mix of cool and warm tones.",
     "outfit_suggestion": "Here are two complete outfits built around your new Wrangler light-wash cropped denim jacket using items from your wardrobe:\n\n### Outfit 1: Canadian Tuxedo / Streetwear Edge\n*Play with denim-on-denim by contrasting the light-wash jacket with dark bottoms.*\n\n* **Top:** White ribbed tank top (`w_003`) tucked in to highlight the cropped fit of the jacket.\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`) \u2014 the high waist pairs great with the cropped jacket.\n* **Shoes:** Chunky white sneakers (`w_007`) to tie in the white tank top.\n* **Accessories:** Black crossbody bag (`w_010`).\n\n### Outfit 2: Casual Earth Tones\n*Contrast the cool light blue of the jacket with warm, neutral trousers.*\n\n* **Top:** Oversized grey crewneck sweatshirt (`w_004`) worn underneath as a cozy layer, letting the hem peek out below the cropped jacket.\n* **Bottoms:** Wide-leg khaki trousers (`w_002`).\n* **Shoes:** Black combat boots (`w_008`) to ground the lighter tones of the outfit.\n* **Accessories:** Brown leather belt (`w_009`) threaded through the trousers to pull the earth tones together.",
     "parsed": {
          "description": "denim jacket",
          "max_price": 50.0,
          "size": null
     },
     "query": "denim jacket under $50",
          .......}}

Criterion 2: hoodie timeout

     - Source: `serve.py::ask exception handling`
     - Pass: `True`
     - Expected:
     ```json
     "timeout in error response"
     ```
     - Actual output:
     ```json
     {
     "status": 500,
     "body": {
     "error": "TimeoutError: simulated request timeout"
     },
     "request_id": "4b66389aa7cd"
     }
     ```

Criterion 3: graphic tee request is logged

     - Source: `serve.py::finish_request_logging`
     - Pass: `True`
     - Expected:
     ```json
     {
     "path": "logs/fitfindr.jsonl",
     "event": "request_completed",
     "fields": [
     "request_id",
     "status",
     "duration_ms",
     "error"
     ]
     }
     ```
     - Actual output:
     ```json
     {
     "response": {
     "status": 200,
     "body": {
          "error": null,
          "fit_card": "Scored this soft, worn-in 2003 tour bootleg graphic tee on Depop for just $24, and it has the absolute best boxy fit. I love styling the faded black cotton either layered under a cropped zip hoodie for casual streetwear days or tucked into wide-leg khakis with heavy combat boots for a grunge edge.",
          "outfit_suggestion": "Here are two complete outfits centered around your new vintage graphic tee, using pieces straight from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n*Play up the bootleg band tee vibe with relaxed denim and classic streetwear layers.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Outerwear:** Black cropped zip hoodie (`w_005`) worn unzipped over the tee\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hem of the boxy tee peek out from under the cropped zip hoodie for a layered, textured look. Pair with the baggy dark-wash jeans and finish with the chunky white sneakers and crossbody bag for an easy everyday streetwear fit.\n\n### Outfit 2: Grunge-Inspired Contrast\n*Lean into the grunge aesthetic by pairing the faded black tee with khaki and heavy boots.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Outerwear:** Vintage black denim jacket (`w_006`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Tuck the graphic tee loosely into the wide-leg khaki trousers, cinched with the brown leather belt to add definition. Throw on the slightly cropped black denim jacket and anchor the look with the black combat boots to lean into the vintage, worn-in edge of the tee.",
          .....}}}


Criterion 4: hoodie listing ID reaches suggest_outfit

     - Source: `agent.py::run_agent`
     - Pass: `True`
     - Expected:
     ```json
     "search_listings ID equals suggest_outfit ID"
     ```
     - Actual output:
     ```json
     {
     "selected_id": "test_hoodie_listing_ID_reaches_suggest_outfit",
     "suggested_id": "test_hoodie_listing_ID_reaches_suggest_outfit",
     "error": null
     }
     ```

Criterion 5: missing query field

     - Source: `serve.py::ask validation`
     - Pass: `True`
     - Expected:
     ```json
     "error response and no HTTP 500"
     ```
     - Actual output:
     ```json
     {
     "status": 400,
     "body": {
     "error": "Send JSON with a 'query' field, e.g. {\"query\": \"vintage graphic tee under $30\"}"
     },
     "request_id": "b058b4e5c700"
     }
     ```

**File:** run_extensions.py
**Function:** main()

**Diagnoses:**
     All my five criteria are met, and there was no repeated failure across the runs. But, I think my criterion 4 is weaker, because it measures the behavior I had tested before too. In a future version, I would replace it a with a criterion that tests how the system handles the model/API failure because it tests the system behaviour when external dependency is unavailable.

**RUN LOG AFTER:**

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.For all 5 of 5 valid requests, the system returns a non-empty complete outfit suggestion and non-empty fit card.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. For all 5 of 5 time out requests, the system returns a clear error message instead of crashing or returning an incomplete result.| 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. For all 5 of 5 requests, every output appears in log file. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. For 5 of 5 simulated model/API failures, the response contains a non-empty error message, no traceback, and no fit card. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. For all 5 of 5 cases, malformed input returns HTTP 400 instead of HTTP 500. | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

     All five criteria were met after the change. Before the change, model/API failures could return HTTP 200 with an error field, which made the request appear successful to an HTTP client. After the change, model/API failures return HTTP 500 with a readable error message and no usable fit card. This helped make failures easier for clients to detect and confirmed that the system handles unavailable model services correctly. The tradeoff is that clients must now handle HTTP 500 responses for service failures, while normal no-match responses remain HTTP 200 and malformed requests remain HTTP 400.

**What's Still Broken:**

No current criterion was missed in the after run. One limitation remains: the model/API failure test uses a simulated failure, so it confirms the app handles the error correctly but does not prove how it would behave during a real provider outage.

**Next Step:**

If this were a real service, I would first add a staging fault-injection test
at the actual model and MCP client boundaries. That would verify the same
HTTP 500 behavior against realistic transport failures without relying on a
live provider outage.

**How I Used AI:**
**Moment 1**
- *What I asked for:* I asked Copilot to help me implement run_extensions.py to test the capstone criteria
- *What came back:* The first version was more complicated than necessary and duplicated some functionality that already existed in the project.
- *What I changed:* I asked Copilot to reuse the existing patterns from run_eval.py and simplify the implementation instead of recreating functionality. This produced a cleaner runner that fit the project’s existing structure better.

**Moment 2**
- *What I asked for:* I asked Copilot to help me understand how to connect logging, model-failure handling, and the other extension features.
- *What came back:* It explained where each part of the logic belongs, why it is needed, and how to integrate it with the existing system.


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
