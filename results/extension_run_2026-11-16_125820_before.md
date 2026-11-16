# Unit 9 extension run log — before

- Rounds: 3
- Cases per criterion per round: 5
- Total cases: 75
- When: 2026-11-16 12:58:20

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. serve.py::ask | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. serve.py::ask exception handling | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. serve.py::finish_request_logging | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. agent.py::run_agent | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. serve.py::ask validation | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

## Real output

### Run 1

#### Criterion 1: valid graphic tee request

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
    "fit_card": "Scored this soft, worn-in 2003 tour bootleg graphic tee on Depop for just $24, and it has the absolute best boxy fit. I love styling the faded black cotton either layered under a cropped zip hoodie for casual streetwear days or tucked into wide-leg khakis with heavy combat boots for a grunge edge.",
    "outfit_suggestion": "Here are two complete outfits centered around your new vintage graphic tee, using pieces straight from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n*Play up the bootleg band tee vibe with relaxed denim and classic streetwear layers.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Outerwear:** Black cropped zip hoodie (`w_005`) worn unzipped over the tee\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hem of the boxy tee peek out from under the cropped zip hoodie for a layered, textured look. Pair with the baggy dark-wash jeans and finish with the chunky white sneakers and crossbody bag for an easy everyday streetwear fit.\n\n### Outfit 2: Grunge-Inspired Contrast\n*Lean into the grunge aesthetic by pairing the faded black tee with khaki and heavy boots.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Outerwear:** Vintage black denim jacket (`w_006`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Tuck the graphic tee loosely into the wide-leg khaki trousers, cinched with the brown leather belt to add definition. Throw on the slightly cropped black denim jacket and anchor the look with the black combat boots to lean into the vintage, worn-in edge of the tee.",
    "parsed": {
      "description": "vintage graphic tee",
      "max_price": 30.0,
      "size": null
    },
    "query": "vintage graphic tee under $30",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "white",
          "pink",
          "purple"
        ],
        "condition": "excellent",
        "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
        "id": "lst_002",
        "platform": "depop",
        "price": 18.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "vintage",
          "graphic tee",
          "cottagecore"
        ],
        "title": "Y2K Baby Tee \u2014 Butterfly Print"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "grey",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.",
        "id": "lst_033",
        "platform": "depop",
        "price": 19.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "band tee",
          "graphic tee",
          "streetwear"
        ],
        "title": "Vintage Band Tee \u2014 Faded Grey"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "navy"
        ],
        "condition": "good",
        "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
        "id": "lst_012",
        "platform": "thredUp",
        "price": 20.0,
        "size": "XL (fits oversized)",
        "style_tags": [
          "vintage",
          "basics",
          "oversized",
          "classic"
        ],
        "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "burgundy",
          "wine"
        ],
        "condition": "excellent",
        "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
        "id": "lst_020",
        "platform": "thredUp",
        "price": 16.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "basics",
          "earth tones",
          "classic"
        ],
        "title": "Henley Long Sleeve \u2014 Washed Burgundy"
      },
      {
        "brand": "Ralph Lauren",
        "category": "tops",
        "colors": [
          "green",
          "forest green"
        ],
        "condition": "good",
        "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
        "id": "lst_024",
        "platform": "thredUp",
        "price": 18.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "classic",
          "earth tones"
        ],
        "title": "Vintage Polo Shirt \u2014 Forest Green"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black"
      ],
      "condition": "good",
      "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
      "id": "lst_006",
      "platform": "depop",
      "price": 24.0,
      "size": "L",
      "style_tags": [
        "graphic tee",
        "vintage",
        "grunge",
        "streetwear",
        "band tee"
      ],
      "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "78770eabdc0a"
}
```

#### Criterion 1: valid denim jacket request

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
    "search_results": [
      {
        "brand": "Wrangler",
        "category": "outerwear",
        "colors": [
          "light blue"
        ],
        "condition": "excellent",
        "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
        "id": "lst_007",
        "platform": "poshmark",
        "price": 42.0,
        "size": "S",
        "style_tags": [
          "denim",
          "vintage",
          "classic",
          "streetwear"
        ],
        "title": "Denim Jacket \u2014 Light Wash, Cropped"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "light blue",
          "blue"
        ],
        "condition": "good",
        "description": "DIY cutoff denim shorts from Levi's 501s. Raw hem, slightly frayed. High-waisted. Perfect summer length.",
        "id": "lst_016",
        "platform": "poshmark",
        "price": 24.0,
        "size": "W27",
        "style_tags": [
          "vintage",
          "denim",
          "summer",
          "classic"
        ],
        "title": "High-Waisted Denim Shorts \u2014 Cutoff"
      },
      {
        "brand": null,
        "category": "outerwear",
        "colors": [
          "medium blue"
        ],
        "condition": "good",
        "description": "Denim vest with silver stud detailing along the collar and pockets. Classic rock-inspired customization. Fits like a medium.",
        "id": "lst_038",
        "platform": "depop",
        "price": 27.0,
        "size": "M",
        "style_tags": [
          "grunge",
          "vintage",
          "denim",
          "customized",
          "rock"
        ],
        "title": "Denim Vest \u2014 Medium Wash, Studded"
      },
      {
        "brand": "Champion",
        "category": "outerwear",
        "colors": [
          "navy",
          "white"
        ],
        "condition": "excellent",
        "description": "Authentic 90s track jacket with stripe detail down the sleeves. Full zip. Lightweight \u2014 great for layering.",
        "id": "lst_004",
        "platform": "poshmark",
        "price": 45.0,
        "size": "M",
        "style_tags": [
          "90s",
          "vintage",
          "athletic",
          "streetwear"
        ],
        "title": "90s Track Jacket \u2014 Navy/White Stripe"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "black",
          "faded black"
        ],
        "condition": "good",
        "description": "Faded black straight-leg jeans. Sits at the hips, classic fit. Slightly cropped length. No rips, just natural fading.",
        "id": "lst_037",
        "platform": "thredUp",
        "price": 30.0,
        "size": "W28",
        "style_tags": [
          "vintage",
          "classic",
          "grunge",
          "denim"
        ],
        "title": "Straight Leg Black Jeans \u2014 Faded"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "blue",
          "indigo"
        ],
        "condition": "good",
        "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
        "id": "lst_001",
        "platform": "depop",
        "price": 38.0,
        "size": "W30 L30",
        "style_tags": [
          "vintage",
          "classic",
          "denim",
          "streetwear"
        ],
        "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
      }
    ],
    "selected_item": {
      "brand": "Wrangler",
      "category": "outerwear",
      "colors": [
        "light blue"
      ],
      "condition": "excellent",
      "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
      "id": "lst_007",
      "platform": "poshmark",
      "price": 42.0,
      "size": "S",
      "style_tags": [
        "denim",
        "vintage",
        "classic",
        "streetwear"
      ],
      "title": "Denim Jacket \u2014 Light Wash, Cropped"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "73c990b5f236"
}
```

#### Criterion 1: valid jeans request

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
    "fit_card": "Every wardrobe needs a good sheer black mesh long-sleeve for effortless layering, and I've been living in this stretchy, Y2K-inspired staple lately. Throw it on with baggy dark-wash denim and chunky white sneakers for a textured streetwear look, or dress it down with wide-leg trousers and combat boots. Grab this excellent-condition piece for just $15 over on my Depop before it's gone!",
    "outfit_suggestion": "Here are two complete outfits centered around the thrifted sheer black mesh long-sleeve top, built entirely from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n* **Base Layer:** Thrifted mesh long-sleeve top worn over the **White ribbed tank top** (w_003) for a textured, dimensional look.\n* **Bottoms:** **Baggy straight-leg jeans, dark wash** (w_001).\n* **Outerwear:** **Black cropped zip hoodie** (w_005) layered on top.\n* **Shoes:** **Chunky white sneakers** (w_007).\n* **Accessories:** **Black crossbody bag** (w_010).\n\n### Outfit 2: Grunge-Inspired Monochrome\n* **Base Layer:** Thrifted mesh long-sleeve top worn solo or layered over the white tank.\n* **Bottoms:** **Wide-leg khaki trousers** (w_002) paired with the **Brown leather belt** (w_009) to add definition at the waist.\n* **Outerwear:** **Vintage black denim jacket** (w_006) thrown over the shoulders.\n* **Shoes:** **Black combat boots** (w_008) to lean into the grunge aesthetic.\n* **Accessories:** **Black crossbody bag** (w_010).",
    "parsed": {
      "description": "black jeans",
      "max_price": 40.0,
      "size": "M"
    },
    "query": "black jeans size M under $40",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "excellent",
        "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
        "id": "lst_017",
        "platform": "depop",
        "price": 15.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "grunge",
          "goth",
          "layering"
        ],
        "title": "Mesh Long-Sleeve Top \u2014 Black"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black"
      ],
      "condition": "excellent",
      "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
      "id": "lst_017",
      "platform": "depop",
      "price": 15.0,
      "size": "S/M",
      "style_tags": [
        "y2k",
        "grunge",
        "goth",
        "layering"
      ],
      "title": "Mesh Long-Sleeve Top \u2014 Black"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "00b46817b4ea"
}
```

#### Criterion 1: valid cardigan request

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
    "fit_card": "Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.",
    "outfit_suggestion": "Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:\n\n### Outfit 1: Casual & Minimalist Earth Tones\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Wide-leg khaki trousers\n* **Accessories:** Brown leather belt\n* **Shoes:** Chunky white sneakers\n* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.\n\n### Outfit 2: Contrast Denim & Edge\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Baggy straight-leg jeans, dark wash\n* **Shoes:** Black combat boots\n* **Accessories:** Black crossbody bag\n* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.",
    "parsed": {
      "description": "brown cardigan",
      "max_price": 35.0,
      "size": null
    },
    "query": "brown cardigan under $35",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "tan"
        ],
        "condition": "excellent",
        "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
        "id": "lst_008",
        "platform": "depop",
        "price": 35.0,
        "size": "One Size / Oversized",
        "style_tags": [
          "cottagecore",
          "cozy",
          "oversized",
          "earth tones",
          "knitwear"
        ],
        "title": "Knit Cardigan \u2014 Chunky Brown"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "brown",
        "tan"
      ],
      "condition": "excellent",
      "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
      "id": "lst_008",
      "platform": "depop",
      "price": 35.0,
      "size": "One Size / Oversized",
      "style_tags": [
        "cottagecore",
        "cozy",
        "oversized",
        "earth tones",
        "knitwear"
      ],
      "title": "Knit Cardigan \u2014 Chunky Brown"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "533f91bca45f"
}
```

#### Criterion 1: valid hoodie request

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
    "fit_card": "Nothing beats the ultimate worn-in feel of this faded black vintage graphic hoodie, scored on Depop for just $26. Style it grungy with baggy denim and combat boots, or keep it balanced by layering it over a ribbed white tank with wide-leg khaki trousers and chunky sneakers. It has that perfectly distressed, lived-in look that instantly makes any outfit effortless.",
    "outfit_suggestion": "Here are two complete outfits centered around your new faded black graphic hoodie, built entirely from your wardrobe:\n\n### Outfit 1: 90s Grunge Streetwear\n*Lean into the worn-in texture of the hoodie with heavy denim and combat boots.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hoodie drape loosely over the high-waisted baggy jeans. Pair with the combat boots to lean into the grunge aesthetic, and throw on the black crossbody bag for an easy, utilitarian everyday look.\n\n### Outfit 2: Casual High-Low Contrast\n*Pair the slouchy, faded hoodie with structured earth-tone trousers for a balanced, laid-back streetwear look.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item) layered over the White ribbed tank top (`w_003`) peeking out the bottom\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Wear the white ribbed tank underneath so a bit of white pops at the hem. Tuck the wide-leg khaki trousers in at the waist using the brown leather belt for some contrast, and finish the outfit with the chunky white sneakers to keep it sporty and relaxed.",
    "parsed": {
      "description": "vintage hoodie",
      "max_price": 45.0,
      "size": null
    },
    "query": "vintage hoodie under $45",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "navy"
        ],
        "condition": "good",
        "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
        "id": "lst_012",
        "platform": "thredUp",
        "price": 20.0,
        "size": "XL (fits oversized)",
        "style_tags": [
          "vintage",
          "basics",
          "oversized",
          "classic"
        ],
        "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "blue",
          "indigo"
        ],
        "condition": "good",
        "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
        "id": "lst_001",
        "platform": "depop",
        "price": 38.0,
        "size": "W30 L30",
        "style_tags": [
          "vintage",
          "classic",
          "denim",
          "streetwear"
        ],
        "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "burgundy",
          "wine"
        ],
        "condition": "excellent",
        "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
        "id": "lst_020",
        "platform": "thredUp",
        "price": 16.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "basics",
          "earth tones",
          "classic"
        ],
        "title": "Henley Long Sleeve \u2014 Washed Burgundy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "white",
          "pink",
          "purple"
        ],
        "condition": "excellent",
        "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
        "id": "lst_002",
        "platform": "depop",
        "price": 18.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "vintage",
          "graphic tee",
          "cottagecore"
        ],
        "title": "Y2K Baby Tee \u2014 Butterfly Print"
      },
      {
        "brand": "Ralph Lauren",
        "category": "tops",
        "colors": [
          "green",
          "forest green"
        ],
        "condition": "good",
        "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
        "id": "lst_024",
        "platform": "thredUp",
        "price": 18.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "classic",
          "earth tones"
        ],
        "title": "Vintage Polo Shirt \u2014 Forest Green"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black",
        "charcoal"
      ],
      "condition": "fair",
      "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
      "id": "lst_015",
      "platform": "depop",
      "price": 26.0,
      "size": "L",
      "style_tags": [
        "vintage",
        "grunge",
        "graphic",
        "streetwear"
      ],
      "title": "Vintage Graphic Hoodie \u2014 Faded Black"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "93da17c8fcaa"
}
```

#### Criterion 2: graphic tee timeout

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
  "request_id": "04f310d658d9"
}
```

#### Criterion 2: denim jacket timeout

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
  "request_id": "280820471b2a"
}
```

#### Criterion 2: jeans timeout

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
  "request_id": "683d1aaec4a0"
}
```

#### Criterion 2: cardigan timeout

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
  "request_id": "117092c86f53"
}
```

#### Criterion 2: hoodie timeout

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

#### Criterion 3: graphic tee request is logged

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
      "parsed": {
        "description": "vintage graphic tee",
        "max_price": 30.0,
        "size": null
      },
      "query": "vintage graphic tee under $30",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "good",
          "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
          "id": "lst_006",
          "platform": "depop",
          "price": 24.0,
          "size": "L",
          "style_tags": [
            "graphic tee",
            "vintage",
            "grunge",
            "streetwear",
            "band tee"
          ],
          "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "white",
            "pink",
            "purple"
          ],
          "condition": "excellent",
          "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
          "id": "lst_002",
          "platform": "depop",
          "price": 18.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "vintage",
            "graphic tee",
            "cottagecore"
          ],
          "title": "Y2K Baby Tee \u2014 Butterfly Print"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.",
          "id": "lst_033",
          "platform": "depop",
          "price": 19.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "band tee",
            "graphic tee",
            "streetwear"
          ],
          "title": "Vintage Band Tee \u2014 Faded Grey"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
          "id": "lst_015",
          "platform": "depop",
          "price": 26.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "graphic",
            "streetwear"
          ],
          "title": "Vintage Graphic Hoodie \u2014 Faded Black"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "navy"
          ],
          "condition": "good",
          "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
          "id": "lst_012",
          "platform": "thredUp",
          "price": 20.0,
          "size": "XL (fits oversized)",
          "style_tags": [
            "vintage",
            "basics",
            "oversized",
            "classic"
          ],
          "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "burgundy",
            "wine"
          ],
          "condition": "excellent",
          "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
          "id": "lst_020",
          "platform": "thredUp",
          "price": 16.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "basics",
            "earth tones",
            "classic"
          ],
          "title": "Henley Long Sleeve \u2014 Washed Burgundy"
        },
        {
          "brand": "Ralph Lauren",
          "category": "tops",
          "colors": [
            "green",
            "forest green"
          ],
          "condition": "good",
          "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
          "id": "lst_024",
          "platform": "thredUp",
          "price": 18.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "classic",
            "earth tones"
          ],
          "title": "Vintage Polo Shirt \u2014 Forest Green"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "ee618d7847e8"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:15.538500+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "ee618d7847e8",
    "method": "POST",
    "path": "/ask",
    "query": "vintage graphic tee under $30",
    "status": 200,
    "duration_ms": 3227.72,
    "search_results": 10,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: denim jacket request is logged

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
      "fit_card": "Scored this vintage Wrangler cropped denim jacket on Poshmark for just $42, and it\u2019s the ultimate blank canvas for layering. I love pairing the light wash with dark baggy denim and fresh white sneakers for an effortless streetwear vibe. It also looks amazing thrown over an oversized grey crewneck and khaki trousers for an easy mix of cool and warm tones.",
      "outfit_suggestion": "Here are two complete outfits built around your new Wrangler light-wash cropped denim jacket using items from your wardrobe:\n\n### Outfit 1: Canadian Tuxedo / Streetwear Edge\n*Play with denim-on-denim by contrasting the light-wash jacket with dark bottoms.*\n\n* **Top:** White ribbed tank top (`w_003`) tucked in to highlight the cropped fit of the jacket.\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`) \u2014 the high waist pairs great with the cropped jacket.\n* **Shoes:** Chunky white sneakers (`w_007`) to tie in the white tank top.\n* **Accessories:** Black crossbody bag (`w_010`).\n\n### Outfit 2: Casual Earth Tones\n*Contrast the cool light blue of the jacket with warm, neutral trousers.*\n\n* **Top:** Oversized grey crewneck sweatshirt (`w_004`) worn underneath as a cozy layer, letting the hem peek out below the cropped jacket.\n* **Bottoms:** Wide-leg khaki trousers (`w_002`).\n* **Shoes:** Black combat boots (`w_008`) to ground the lighter tones of the outfit.\n* **Accessories:** Brown leather belt (`w_009`) threaded through the trousers to pull the earth tones together.",
      "parsed": {
        "description": "denim jacket",
        "max_price": 50.0,
        "size": null
      },
      "query": "denim jacket under $50",
      "search_results": [
        {
          "brand": "Wrangler",
          "category": "outerwear",
          "colors": [
            "light blue"
          ],
          "condition": "excellent",
          "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
          "id": "lst_007",
          "platform": "poshmark",
          "price": 42.0,
          "size": "S",
          "style_tags": [
            "denim",
            "vintage",
            "classic",
            "streetwear"
          ],
          "title": "Denim Jacket \u2014 Light Wash, Cropped"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "light blue",
            "blue"
          ],
          "condition": "good",
          "description": "DIY cutoff denim shorts from Levi's 501s. Raw hem, slightly frayed. High-waisted. Perfect summer length.",
          "id": "lst_016",
          "platform": "poshmark",
          "price": 24.0,
          "size": "W27",
          "style_tags": [
            "vintage",
            "denim",
            "summer",
            "classic"
          ],
          "title": "High-Waisted Denim Shorts \u2014 Cutoff"
        },
        {
          "brand": null,
          "category": "outerwear",
          "colors": [
            "medium blue"
          ],
          "condition": "good",
          "description": "Denim vest with silver stud detailing along the collar and pockets. Classic rock-inspired customization. Fits like a medium.",
          "id": "lst_038",
          "platform": "depop",
          "price": 27.0,
          "size": "M",
          "style_tags": [
            "grunge",
            "vintage",
            "denim",
            "customized",
            "rock"
          ],
          "title": "Denim Vest \u2014 Medium Wash, Studded"
        },
        {
          "brand": "Champion",
          "category": "outerwear",
          "colors": [
            "navy",
            "white"
          ],
          "condition": "excellent",
          "description": "Authentic 90s track jacket with stripe detail down the sleeves. Full zip. Lightweight \u2014 great for layering.",
          "id": "lst_004",
          "platform": "poshmark",
          "price": 45.0,
          "size": "M",
          "style_tags": [
            "90s",
            "vintage",
            "athletic",
            "streetwear"
          ],
          "title": "90s Track Jacket \u2014 Navy/White Stripe"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "black",
            "faded black"
          ],
          "condition": "good",
          "description": "Faded black straight-leg jeans. Sits at the hips, classic fit. Slightly cropped length. No rips, just natural fading.",
          "id": "lst_037",
          "platform": "thredUp",
          "price": 30.0,
          "size": "W28",
          "style_tags": [
            "vintage",
            "classic",
            "grunge",
            "denim"
          ],
          "title": "Straight Leg Black Jeans \u2014 Faded"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "blue",
            "indigo"
          ],
          "condition": "good",
          "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
          "id": "lst_001",
          "platform": "depop",
          "price": 38.0,
          "size": "W30 L30",
          "style_tags": [
            "vintage",
            "classic",
            "denim",
            "streetwear"
          ],
          "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
        }
      ],
      "selected_item": {
        "brand": "Wrangler",
        "category": "outerwear",
        "colors": [
          "light blue"
        ],
        "condition": "excellent",
        "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
        "id": "lst_007",
        "platform": "poshmark",
        "price": 42.0,
        "size": "S",
        "style_tags": [
          "denim",
          "vintage",
          "classic",
          "streetwear"
        ],
        "title": "Denim Jacket \u2014 Light Wash, Cropped"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "3d75b58a309a"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:18.900023+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "3d75b58a309a",
    "method": "POST",
    "path": "/ask",
    "query": "denim jacket under $50",
    "status": 200,
    "duration_ms": 3347.14,
    "search_results": 6,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: jeans request is logged

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
      "fit_card": "Every wardrobe needs a good sheer black mesh long-sleeve for effortless layering, and I've been living in this stretchy, Y2K-inspired staple lately. Throw it on with baggy dark-wash denim and chunky white sneakers for a textured streetwear look, or dress it down with wide-leg trousers and combat boots. Grab this excellent-condition piece for just $15 over on my Depop before it's gone!",
      "outfit_suggestion": "Here are two complete outfits centered around the thrifted sheer black mesh long-sleeve top, built entirely from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n* **Base Layer:** Thrifted mesh long-sleeve top worn over the **White ribbed tank top** (w_003) for a textured, dimensional look.\n* **Bottoms:** **Baggy straight-leg jeans, dark wash** (w_001).\n* **Outerwear:** **Black cropped zip hoodie** (w_005) layered on top.\n* **Shoes:** **Chunky white sneakers** (w_007).\n* **Accessories:** **Black crossbody bag** (w_010).\n\n### Outfit 2: Grunge-Inspired Monochrome\n* **Base Layer:** Thrifted mesh long-sleeve top worn solo or layered over the white tank.\n* **Bottoms:** **Wide-leg khaki trousers** (w_002) paired with the **Brown leather belt** (w_009) to add definition at the waist.\n* **Outerwear:** **Vintage black denim jacket** (w_006) thrown over the shoulders.\n* **Shoes:** **Black combat boots** (w_008) to lean into the grunge aesthetic.\n* **Accessories:** **Black crossbody bag** (w_010).",
      "parsed": {
        "description": "black jeans",
        "max_price": 40.0,
        "size": "M"
      },
      "query": "black jeans size M under $40",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "excellent",
          "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
          "id": "lst_017",
          "platform": "depop",
          "price": 15.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "grunge",
            "goth",
            "layering"
          ],
          "title": "Mesh Long-Sleeve Top \u2014 Black"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "excellent",
        "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
        "id": "lst_017",
        "platform": "depop",
        "price": 15.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "grunge",
          "goth",
          "layering"
        ],
        "title": "Mesh Long-Sleeve Top \u2014 Black"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "12a195976291"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:21.306976+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "12a195976291",
    "method": "POST",
    "path": "/ask",
    "query": "black jeans size M under $40",
    "status": 200,
    "duration_ms": 2384.93,
    "search_results": 1,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: cardigan request is logged

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
      "fit_card": "Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.",
      "outfit_suggestion": "Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:\n\n### Outfit 1: Casual & Minimalist Earth Tones\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Wide-leg khaki trousers\n* **Accessories:** Brown leather belt\n* **Shoes:** Chunky white sneakers\n* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.\n\n### Outfit 2: Contrast Denim & Edge\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Baggy straight-leg jeans, dark wash\n* **Shoes:** Black combat boots\n* **Accessories:** Black crossbody bag\n* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.",
      "parsed": {
        "description": "brown cardigan",
        "max_price": 35.0,
        "size": null
      },
      "query": "brown cardigan under $35",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "tan"
          ],
          "condition": "excellent",
          "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
          "id": "lst_008",
          "platform": "depop",
          "price": 35.0,
          "size": "One Size / Oversized",
          "style_tags": [
            "cottagecore",
            "cozy",
            "oversized",
            "earth tones",
            "knitwear"
          ],
          "title": "Knit Cardigan \u2014 Chunky Brown"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "tan"
        ],
        "condition": "excellent",
        "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
        "id": "lst_008",
        "platform": "depop",
        "price": 35.0,
        "size": "One Size / Oversized",
        "style_tags": [
          "cottagecore",
          "cozy",
          "oversized",
          "earth tones",
          "knitwear"
        ],
        "title": "Knit Cardigan \u2014 Chunky Brown"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "a1d3984ddc1c"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:23.472447+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "a1d3984ddc1c",
    "method": "POST",
    "path": "/ask",
    "query": "brown cardigan under $35",
    "status": 200,
    "duration_ms": 2139.47,
    "search_results": 4,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: hoodie request is logged

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
      "fit_card": "Nothing beats the ultimate worn-in feel of this faded black vintage graphic hoodie, scored on Depop for just $26. Style it grungy with baggy denim and combat boots, or keep it balanced by layering it over a ribbed white tank with wide-leg khaki trousers and chunky sneakers. It has that perfectly distressed, lived-in look that instantly makes any outfit effortless.",
      "outfit_suggestion": "Here are two complete outfits centered around your new faded black graphic hoodie, built entirely from your wardrobe:\n\n### Outfit 1: 90s Grunge Streetwear\n*Lean into the worn-in texture of the hoodie with heavy denim and combat boots.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hoodie drape loosely over the high-waisted baggy jeans. Pair with the combat boots to lean into the grunge aesthetic, and throw on the black crossbody bag for an easy, utilitarian everyday look.\n\n### Outfit 2: Casual High-Low Contrast\n*Pair the slouchy, faded hoodie with structured earth-tone trousers for a balanced, laid-back streetwear look.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item) layered over the White ribbed tank top (`w_003`) peeking out the bottom\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Wear the white ribbed tank underneath so a bit of white pops at the hem. Tuck the wide-leg khaki trousers in at the waist using the brown leather belt for some contrast, and finish the outfit with the chunky white sneakers to keep it sporty and relaxed.",
      "parsed": {
        "description": "vintage hoodie",
        "max_price": 45.0,
        "size": null
      },
      "query": "vintage hoodie under $45",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
          "id": "lst_015",
          "platform": "depop",
          "price": 26.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "graphic",
            "streetwear"
          ],
          "title": "Vintage Graphic Hoodie \u2014 Faded Black"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "navy"
          ],
          "condition": "good",
          "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
          "id": "lst_012",
          "platform": "thredUp",
          "price": 20.0,
          "size": "XL (fits oversized)",
          "style_tags": [
            "vintage",
            "basics",
            "oversized",
            "classic"
          ],
          "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "good",
          "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
          "id": "lst_006",
          "platform": "depop",
          "price": 24.0,
          "size": "L",
          "style_tags": [
            "graphic tee",
            "vintage",
            "grunge",
            "streetwear",
            "band tee"
          ],
          "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "blue",
            "indigo"
          ],
          "condition": "good",
          "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
          "id": "lst_001",
          "platform": "depop",
          "price": 38.0,
          "size": "W30 L30",
          "style_tags": [
            "vintage",
            "classic",
            "denim",
            "streetwear"
          ],
          "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "burgundy",
            "wine"
          ],
          "condition": "excellent",
          "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
          "id": "lst_020",
          "platform": "thredUp",
          "price": 16.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "basics",
            "earth tones",
            "classic"
          ],
          "title": "Henley Long Sleeve \u2014 Washed Burgundy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "white",
            "pink",
            "purple"
          ],
          "condition": "excellent",
          "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
          "id": "lst_002",
          "platform": "depop",
          "price": 18.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "vintage",
            "graphic tee",
            "cottagecore"
          ],
          "title": "Y2K Baby Tee \u2014 Butterfly Print"
        },
        {
          "brand": "Ralph Lauren",
          "category": "tops",
          "colors": [
            "green",
            "forest green"
          ],
          "condition": "good",
          "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
          "id": "lst_024",
          "platform": "thredUp",
          "price": 18.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "classic",
            "earth tones"
          ],
          "title": "Vintage Polo Shirt \u2014 Forest Green"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "0beadcce0a08"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:25.936490+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "0beadcce0a08",
    "method": "POST",
    "path": "/ask",
    "query": "vintage hoodie under $45",
    "status": 200,
    "duration_ms": 2448.02,
    "search_results": 10,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 4: graphic tee listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_graphic_tee_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_graphic_tee_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: denim jacket listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_denim_jacket_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_denim_jacket_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: jeans listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_jeans_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_jeans_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: cardigan listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_cardigan_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_cardigan_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: hoodie listing ID reaches suggest_outfit

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

#### Criterion 5: missing query field

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

#### Criterion 5: empty query string

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
  "request_id": "e96ebd1138b5"
}
```

#### Criterion 5: whitespace-only query

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
  "request_id": "90f283ff18db"
}
```

#### Criterion 5: null query

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
  "request_id": "868d0cfa583d"
}
```

#### Criterion 5: query field omitted in alternate payload

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
  "request_id": "324afc7ac32c"
}
```

### Run 2

#### Criterion 1: valid graphic tee request

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
    "fit_card": "Scored this soft, worn-in 2003 tour bootleg graphic tee on Depop for just $24, and it has the absolute best boxy fit. I love styling the faded black cotton either layered under a cropped zip hoodie for casual streetwear days or tucked into wide-leg khakis with heavy combat boots for a grunge edge.",
    "outfit_suggestion": "Here are two complete outfits centered around your new vintage graphic tee, using pieces straight from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n*Play up the bootleg band tee vibe with relaxed denim and classic streetwear layers.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Outerwear:** Black cropped zip hoodie (`w_005`) worn unzipped over the tee\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hem of the boxy tee peek out from under the cropped zip hoodie for a layered, textured look. Pair with the baggy dark-wash jeans and finish with the chunky white sneakers and crossbody bag for an easy everyday streetwear fit.\n\n### Outfit 2: Grunge-Inspired Contrast\n*Lean into the grunge aesthetic by pairing the faded black tee with khaki and heavy boots.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Outerwear:** Vintage black denim jacket (`w_006`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Tuck the graphic tee loosely into the wide-leg khaki trousers, cinched with the brown leather belt to add definition. Throw on the slightly cropped black denim jacket and anchor the look with the black combat boots to lean into the vintage, worn-in edge of the tee.",
    "parsed": {
      "description": "vintage graphic tee",
      "max_price": 30.0,
      "size": null
    },
    "query": "vintage graphic tee under $30",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "white",
          "pink",
          "purple"
        ],
        "condition": "excellent",
        "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
        "id": "lst_002",
        "platform": "depop",
        "price": 18.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "vintage",
          "graphic tee",
          "cottagecore"
        ],
        "title": "Y2K Baby Tee \u2014 Butterfly Print"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "grey",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.",
        "id": "lst_033",
        "platform": "depop",
        "price": 19.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "band tee",
          "graphic tee",
          "streetwear"
        ],
        "title": "Vintage Band Tee \u2014 Faded Grey"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "navy"
        ],
        "condition": "good",
        "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
        "id": "lst_012",
        "platform": "thredUp",
        "price": 20.0,
        "size": "XL (fits oversized)",
        "style_tags": [
          "vintage",
          "basics",
          "oversized",
          "classic"
        ],
        "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "burgundy",
          "wine"
        ],
        "condition": "excellent",
        "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
        "id": "lst_020",
        "platform": "thredUp",
        "price": 16.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "basics",
          "earth tones",
          "classic"
        ],
        "title": "Henley Long Sleeve \u2014 Washed Burgundy"
      },
      {
        "brand": "Ralph Lauren",
        "category": "tops",
        "colors": [
          "green",
          "forest green"
        ],
        "condition": "good",
        "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
        "id": "lst_024",
        "platform": "thredUp",
        "price": 18.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "classic",
          "earth tones"
        ],
        "title": "Vintage Polo Shirt \u2014 Forest Green"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black"
      ],
      "condition": "good",
      "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
      "id": "lst_006",
      "platform": "depop",
      "price": 24.0,
      "size": "L",
      "style_tags": [
        "graphic tee",
        "vintage",
        "grunge",
        "streetwear",
        "band tee"
      ],
      "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "8ad15616984b"
}
```

#### Criterion 1: valid denim jacket request

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
    "search_results": [
      {
        "brand": "Wrangler",
        "category": "outerwear",
        "colors": [
          "light blue"
        ],
        "condition": "excellent",
        "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
        "id": "lst_007",
        "platform": "poshmark",
        "price": 42.0,
        "size": "S",
        "style_tags": [
          "denim",
          "vintage",
          "classic",
          "streetwear"
        ],
        "title": "Denim Jacket \u2014 Light Wash, Cropped"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "light blue",
          "blue"
        ],
        "condition": "good",
        "description": "DIY cutoff denim shorts from Levi's 501s. Raw hem, slightly frayed. High-waisted. Perfect summer length.",
        "id": "lst_016",
        "platform": "poshmark",
        "price": 24.0,
        "size": "W27",
        "style_tags": [
          "vintage",
          "denim",
          "summer",
          "classic"
        ],
        "title": "High-Waisted Denim Shorts \u2014 Cutoff"
      },
      {
        "brand": null,
        "category": "outerwear",
        "colors": [
          "medium blue"
        ],
        "condition": "good",
        "description": "Denim vest with silver stud detailing along the collar and pockets. Classic rock-inspired customization. Fits like a medium.",
        "id": "lst_038",
        "platform": "depop",
        "price": 27.0,
        "size": "M",
        "style_tags": [
          "grunge",
          "vintage",
          "denim",
          "customized",
          "rock"
        ],
        "title": "Denim Vest \u2014 Medium Wash, Studded"
      },
      {
        "brand": "Champion",
        "category": "outerwear",
        "colors": [
          "navy",
          "white"
        ],
        "condition": "excellent",
        "description": "Authentic 90s track jacket with stripe detail down the sleeves. Full zip. Lightweight \u2014 great for layering.",
        "id": "lst_004",
        "platform": "poshmark",
        "price": 45.0,
        "size": "M",
        "style_tags": [
          "90s",
          "vintage",
          "athletic",
          "streetwear"
        ],
        "title": "90s Track Jacket \u2014 Navy/White Stripe"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "black",
          "faded black"
        ],
        "condition": "good",
        "description": "Faded black straight-leg jeans. Sits at the hips, classic fit. Slightly cropped length. No rips, just natural fading.",
        "id": "lst_037",
        "platform": "thredUp",
        "price": 30.0,
        "size": "W28",
        "style_tags": [
          "vintage",
          "classic",
          "grunge",
          "denim"
        ],
        "title": "Straight Leg Black Jeans \u2014 Faded"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "blue",
          "indigo"
        ],
        "condition": "good",
        "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
        "id": "lst_001",
        "platform": "depop",
        "price": 38.0,
        "size": "W30 L30",
        "style_tags": [
          "vintage",
          "classic",
          "denim",
          "streetwear"
        ],
        "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
      }
    ],
    "selected_item": {
      "brand": "Wrangler",
      "category": "outerwear",
      "colors": [
        "light blue"
      ],
      "condition": "excellent",
      "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
      "id": "lst_007",
      "platform": "poshmark",
      "price": 42.0,
      "size": "S",
      "style_tags": [
        "denim",
        "vintage",
        "classic",
        "streetwear"
      ],
      "title": "Denim Jacket \u2014 Light Wash, Cropped"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "edb00547bf97"
}
```

#### Criterion 1: valid jeans request

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
    "fit_card": "Every wardrobe needs a good sheer black mesh long-sleeve for effortless layering, and I've been living in this stretchy, Y2K-inspired staple lately. Throw it on with baggy dark-wash denim and chunky white sneakers for a textured streetwear look, or dress it down with wide-leg trousers and combat boots. Grab this excellent-condition piece for just $15 over on my Depop before it's gone!",
    "outfit_suggestion": "Here are two complete outfits centered around the thrifted sheer black mesh long-sleeve top, built entirely from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n* **Base Layer:** Thrifted mesh long-sleeve top worn over the **White ribbed tank top** (w_003) for a textured, dimensional look.\n* **Bottoms:** **Baggy straight-leg jeans, dark wash** (w_001).\n* **Outerwear:** **Black cropped zip hoodie** (w_005) layered on top.\n* **Shoes:** **Chunky white sneakers** (w_007).\n* **Accessories:** **Black crossbody bag** (w_010).\n\n### Outfit 2: Grunge-Inspired Monochrome\n* **Base Layer:** Thrifted mesh long-sleeve top worn solo or layered over the white tank.\n* **Bottoms:** **Wide-leg khaki trousers** (w_002) paired with the **Brown leather belt** (w_009) to add definition at the waist.\n* **Outerwear:** **Vintage black denim jacket** (w_006) thrown over the shoulders.\n* **Shoes:** **Black combat boots** (w_008) to lean into the grunge aesthetic.\n* **Accessories:** **Black crossbody bag** (w_010).",
    "parsed": {
      "description": "black jeans",
      "max_price": 40.0,
      "size": "M"
    },
    "query": "black jeans size M under $40",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "excellent",
        "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
        "id": "lst_017",
        "platform": "depop",
        "price": 15.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "grunge",
          "goth",
          "layering"
        ],
        "title": "Mesh Long-Sleeve Top \u2014 Black"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black"
      ],
      "condition": "excellent",
      "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
      "id": "lst_017",
      "platform": "depop",
      "price": 15.0,
      "size": "S/M",
      "style_tags": [
        "y2k",
        "grunge",
        "goth",
        "layering"
      ],
      "title": "Mesh Long-Sleeve Top \u2014 Black"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "1727be8be91a"
}
```

#### Criterion 1: valid cardigan request

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
    "fit_card": "Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.",
    "outfit_suggestion": "Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:\n\n### Outfit 1: Casual & Minimalist Earth Tones\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Wide-leg khaki trousers\n* **Accessories:** Brown leather belt\n* **Shoes:** Chunky white sneakers\n* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.\n\n### Outfit 2: Contrast Denim & Edge\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Baggy straight-leg jeans, dark wash\n* **Shoes:** Black combat boots\n* **Accessories:** Black crossbody bag\n* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.",
    "parsed": {
      "description": "brown cardigan",
      "max_price": 35.0,
      "size": null
    },
    "query": "brown cardigan under $35",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "tan"
        ],
        "condition": "excellent",
        "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
        "id": "lst_008",
        "platform": "depop",
        "price": 35.0,
        "size": "One Size / Oversized",
        "style_tags": [
          "cottagecore",
          "cozy",
          "oversized",
          "earth tones",
          "knitwear"
        ],
        "title": "Knit Cardigan \u2014 Chunky Brown"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "brown",
        "tan"
      ],
      "condition": "excellent",
      "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
      "id": "lst_008",
      "platform": "depop",
      "price": 35.0,
      "size": "One Size / Oversized",
      "style_tags": [
        "cottagecore",
        "cozy",
        "oversized",
        "earth tones",
        "knitwear"
      ],
      "title": "Knit Cardigan \u2014 Chunky Brown"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "521909f52eba"
}
```

#### Criterion 1: valid hoodie request

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
    "fit_card": "Nothing beats the ultimate worn-in feel of this faded black vintage graphic hoodie, scored on Depop for just $26. Style it grungy with baggy denim and combat boots, or keep it balanced by layering it over a ribbed white tank with wide-leg khaki trousers and chunky sneakers. It has that perfectly distressed, lived-in look that instantly makes any outfit effortless.",
    "outfit_suggestion": "Here are two complete outfits centered around your new faded black graphic hoodie, built entirely from your wardrobe:\n\n### Outfit 1: 90s Grunge Streetwear\n*Lean into the worn-in texture of the hoodie with heavy denim and combat boots.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hoodie drape loosely over the high-waisted baggy jeans. Pair with the combat boots to lean into the grunge aesthetic, and throw on the black crossbody bag for an easy, utilitarian everyday look.\n\n### Outfit 2: Casual High-Low Contrast\n*Pair the slouchy, faded hoodie with structured earth-tone trousers for a balanced, laid-back streetwear look.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item) layered over the White ribbed tank top (`w_003`) peeking out the bottom\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Wear the white ribbed tank underneath so a bit of white pops at the hem. Tuck the wide-leg khaki trousers in at the waist using the brown leather belt for some contrast, and finish the outfit with the chunky white sneakers to keep it sporty and relaxed.",
    "parsed": {
      "description": "vintage hoodie",
      "max_price": 45.0,
      "size": null
    },
    "query": "vintage hoodie under $45",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "navy"
        ],
        "condition": "good",
        "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
        "id": "lst_012",
        "platform": "thredUp",
        "price": 20.0,
        "size": "XL (fits oversized)",
        "style_tags": [
          "vintage",
          "basics",
          "oversized",
          "classic"
        ],
        "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "blue",
          "indigo"
        ],
        "condition": "good",
        "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
        "id": "lst_001",
        "platform": "depop",
        "price": 38.0,
        "size": "W30 L30",
        "style_tags": [
          "vintage",
          "classic",
          "denim",
          "streetwear"
        ],
        "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "burgundy",
          "wine"
        ],
        "condition": "excellent",
        "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
        "id": "lst_020",
        "platform": "thredUp",
        "price": 16.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "basics",
          "earth tones",
          "classic"
        ],
        "title": "Henley Long Sleeve \u2014 Washed Burgundy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "white",
          "pink",
          "purple"
        ],
        "condition": "excellent",
        "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
        "id": "lst_002",
        "platform": "depop",
        "price": 18.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "vintage",
          "graphic tee",
          "cottagecore"
        ],
        "title": "Y2K Baby Tee \u2014 Butterfly Print"
      },
      {
        "brand": "Ralph Lauren",
        "category": "tops",
        "colors": [
          "green",
          "forest green"
        ],
        "condition": "good",
        "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
        "id": "lst_024",
        "platform": "thredUp",
        "price": 18.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "classic",
          "earth tones"
        ],
        "title": "Vintage Polo Shirt \u2014 Forest Green"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black",
        "charcoal"
      ],
      "condition": "fair",
      "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
      "id": "lst_015",
      "platform": "depop",
      "price": 26.0,
      "size": "L",
      "style_tags": [
        "vintage",
        "grunge",
        "graphic",
        "streetwear"
      ],
      "title": "Vintage Graphic Hoodie \u2014 Faded Black"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "3282819c2fad"
}
```

#### Criterion 2: graphic tee timeout

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
  "request_id": "dbd99b8b655a"
}
```

#### Criterion 2: denim jacket timeout

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
  "request_id": "e77ee48cef31"
}
```

#### Criterion 2: jeans timeout

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
  "request_id": "a72546132333"
}
```

#### Criterion 2: cardigan timeout

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
  "request_id": "13e4f6fc7db4"
}
```

#### Criterion 2: hoodie timeout

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
  "request_id": "a6734cc76d48"
}
```

#### Criterion 3: graphic tee request is logged

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
      "parsed": {
        "description": "vintage graphic tee",
        "max_price": 30.0,
        "size": null
      },
      "query": "vintage graphic tee under $30",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "good",
          "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
          "id": "lst_006",
          "platform": "depop",
          "price": 24.0,
          "size": "L",
          "style_tags": [
            "graphic tee",
            "vintage",
            "grunge",
            "streetwear",
            "band tee"
          ],
          "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "white",
            "pink",
            "purple"
          ],
          "condition": "excellent",
          "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
          "id": "lst_002",
          "platform": "depop",
          "price": 18.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "vintage",
            "graphic tee",
            "cottagecore"
          ],
          "title": "Y2K Baby Tee \u2014 Butterfly Print"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.",
          "id": "lst_033",
          "platform": "depop",
          "price": 19.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "band tee",
            "graphic tee",
            "streetwear"
          ],
          "title": "Vintage Band Tee \u2014 Faded Grey"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
          "id": "lst_015",
          "platform": "depop",
          "price": 26.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "graphic",
            "streetwear"
          ],
          "title": "Vintage Graphic Hoodie \u2014 Faded Black"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "navy"
          ],
          "condition": "good",
          "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
          "id": "lst_012",
          "platform": "thredUp",
          "price": 20.0,
          "size": "XL (fits oversized)",
          "style_tags": [
            "vintage",
            "basics",
            "oversized",
            "classic"
          ],
          "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "burgundy",
            "wine"
          ],
          "condition": "excellent",
          "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
          "id": "lst_020",
          "platform": "thredUp",
          "price": 16.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "basics",
            "earth tones",
            "classic"
          ],
          "title": "Henley Long Sleeve \u2014 Washed Burgundy"
        },
        {
          "brand": "Ralph Lauren",
          "category": "tops",
          "colors": [
            "green",
            "forest green"
          ],
          "condition": "good",
          "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
          "id": "lst_024",
          "platform": "thredUp",
          "price": 18.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "classic",
            "earth tones"
          ],
          "title": "Vintage Polo Shirt \u2014 Forest Green"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "fff77189dd3b"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:40.968430+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "fff77189dd3b",
    "method": "POST",
    "path": "/ask",
    "query": "vintage graphic tee under $30",
    "status": 200,
    "duration_ms": 2313.33,
    "search_results": 10,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: denim jacket request is logged

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
      "fit_card": "Scored this vintage Wrangler cropped denim jacket on Poshmark for just $42, and it\u2019s the ultimate blank canvas for layering. I love pairing the light wash with dark baggy denim and fresh white sneakers for an effortless streetwear vibe. It also looks amazing thrown over an oversized grey crewneck and khaki trousers for an easy mix of cool and warm tones.",
      "outfit_suggestion": "Here are two complete outfits built around your new Wrangler light-wash cropped denim jacket using items from your wardrobe:\n\n### Outfit 1: Canadian Tuxedo / Streetwear Edge\n*Play with denim-on-denim by contrasting the light-wash jacket with dark bottoms.*\n\n* **Top:** White ribbed tank top (`w_003`) tucked in to highlight the cropped fit of the jacket.\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`) \u2014 the high waist pairs great with the cropped jacket.\n* **Shoes:** Chunky white sneakers (`w_007`) to tie in the white tank top.\n* **Accessories:** Black crossbody bag (`w_010`).\n\n### Outfit 2: Casual Earth Tones\n*Contrast the cool light blue of the jacket with warm, neutral trousers.*\n\n* **Top:** Oversized grey crewneck sweatshirt (`w_004`) worn underneath as a cozy layer, letting the hem peek out below the cropped jacket.\n* **Bottoms:** Wide-leg khaki trousers (`w_002`).\n* **Shoes:** Black combat boots (`w_008`) to ground the lighter tones of the outfit.\n* **Accessories:** Brown leather belt (`w_009`) threaded through the trousers to pull the earth tones together.",
      "parsed": {
        "description": "denim jacket",
        "max_price": 50.0,
        "size": null
      },
      "query": "denim jacket under $50",
      "search_results": [
        {
          "brand": "Wrangler",
          "category": "outerwear",
          "colors": [
            "light blue"
          ],
          "condition": "excellent",
          "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
          "id": "lst_007",
          "platform": "poshmark",
          "price": 42.0,
          "size": "S",
          "style_tags": [
            "denim",
            "vintage",
            "classic",
            "streetwear"
          ],
          "title": "Denim Jacket \u2014 Light Wash, Cropped"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "light blue",
            "blue"
          ],
          "condition": "good",
          "description": "DIY cutoff denim shorts from Levi's 501s. Raw hem, slightly frayed. High-waisted. Perfect summer length.",
          "id": "lst_016",
          "platform": "poshmark",
          "price": 24.0,
          "size": "W27",
          "style_tags": [
            "vintage",
            "denim",
            "summer",
            "classic"
          ],
          "title": "High-Waisted Denim Shorts \u2014 Cutoff"
        },
        {
          "brand": null,
          "category": "outerwear",
          "colors": [
            "medium blue"
          ],
          "condition": "good",
          "description": "Denim vest with silver stud detailing along the collar and pockets. Classic rock-inspired customization. Fits like a medium.",
          "id": "lst_038",
          "platform": "depop",
          "price": 27.0,
          "size": "M",
          "style_tags": [
            "grunge",
            "vintage",
            "denim",
            "customized",
            "rock"
          ],
          "title": "Denim Vest \u2014 Medium Wash, Studded"
        },
        {
          "brand": "Champion",
          "category": "outerwear",
          "colors": [
            "navy",
            "white"
          ],
          "condition": "excellent",
          "description": "Authentic 90s track jacket with stripe detail down the sleeves. Full zip. Lightweight \u2014 great for layering.",
          "id": "lst_004",
          "platform": "poshmark",
          "price": 45.0,
          "size": "M",
          "style_tags": [
            "90s",
            "vintage",
            "athletic",
            "streetwear"
          ],
          "title": "90s Track Jacket \u2014 Navy/White Stripe"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "black",
            "faded black"
          ],
          "condition": "good",
          "description": "Faded black straight-leg jeans. Sits at the hips, classic fit. Slightly cropped length. No rips, just natural fading.",
          "id": "lst_037",
          "platform": "thredUp",
          "price": 30.0,
          "size": "W28",
          "style_tags": [
            "vintage",
            "classic",
            "grunge",
            "denim"
          ],
          "title": "Straight Leg Black Jeans \u2014 Faded"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "blue",
            "indigo"
          ],
          "condition": "good",
          "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
          "id": "lst_001",
          "platform": "depop",
          "price": 38.0,
          "size": "W30 L30",
          "style_tags": [
            "vintage",
            "classic",
            "denim",
            "streetwear"
          ],
          "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
        }
      ],
      "selected_item": {
        "brand": "Wrangler",
        "category": "outerwear",
        "colors": [
          "light blue"
        ],
        "condition": "excellent",
        "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
        "id": "lst_007",
        "platform": "poshmark",
        "price": 42.0,
        "size": "S",
        "style_tags": [
          "denim",
          "vintage",
          "classic",
          "streetwear"
        ],
        "title": "Denim Jacket \u2014 Light Wash, Cropped"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "ca8dfa84c4fa"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:43.001287+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "ca8dfa84c4fa",
    "method": "POST",
    "path": "/ask",
    "query": "denim jacket under $50",
    "status": 200,
    "duration_ms": 2013.61,
    "search_results": 6,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: jeans request is logged

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
      "fit_card": "Every wardrobe needs a good sheer black mesh long-sleeve for effortless layering, and I've been living in this stretchy, Y2K-inspired staple lately. Throw it on with baggy dark-wash denim and chunky white sneakers for a textured streetwear look, or dress it down with wide-leg trousers and combat boots. Grab this excellent-condition piece for just $15 over on my Depop before it's gone!",
      "outfit_suggestion": "Here are two complete outfits centered around the thrifted sheer black mesh long-sleeve top, built entirely from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n* **Base Layer:** Thrifted mesh long-sleeve top worn over the **White ribbed tank top** (w_003) for a textured, dimensional look.\n* **Bottoms:** **Baggy straight-leg jeans, dark wash** (w_001).\n* **Outerwear:** **Black cropped zip hoodie** (w_005) layered on top.\n* **Shoes:** **Chunky white sneakers** (w_007).\n* **Accessories:** **Black crossbody bag** (w_010).\n\n### Outfit 2: Grunge-Inspired Monochrome\n* **Base Layer:** Thrifted mesh long-sleeve top worn solo or layered over the white tank.\n* **Bottoms:** **Wide-leg khaki trousers** (w_002) paired with the **Brown leather belt** (w_009) to add definition at the waist.\n* **Outerwear:** **Vintage black denim jacket** (w_006) thrown over the shoulders.\n* **Shoes:** **Black combat boots** (w_008) to lean into the grunge aesthetic.\n* **Accessories:** **Black crossbody bag** (w_010).",
      "parsed": {
        "description": "black jeans",
        "max_price": 40.0,
        "size": "M"
      },
      "query": "black jeans size M under $40",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "excellent",
          "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
          "id": "lst_017",
          "platform": "depop",
          "price": 15.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "grunge",
            "goth",
            "layering"
          ],
          "title": "Mesh Long-Sleeve Top \u2014 Black"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "excellent",
        "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
        "id": "lst_017",
        "platform": "depop",
        "price": 15.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "grunge",
          "goth",
          "layering"
        ],
        "title": "Mesh Long-Sleeve Top \u2014 Black"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "3be5e564c272"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:45.590156+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "3be5e564c272",
    "method": "POST",
    "path": "/ask",
    "query": "black jeans size M under $40",
    "status": 200,
    "duration_ms": 2567.01,
    "search_results": 1,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: cardigan request is logged

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
      "fit_card": "Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.",
      "outfit_suggestion": "Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:\n\n### Outfit 1: Casual & Minimalist Earth Tones\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Wide-leg khaki trousers\n* **Accessories:** Brown leather belt\n* **Shoes:** Chunky white sneakers\n* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.\n\n### Outfit 2: Contrast Denim & Edge\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Baggy straight-leg jeans, dark wash\n* **Shoes:** Black combat boots\n* **Accessories:** Black crossbody bag\n* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.",
      "parsed": {
        "description": "brown cardigan",
        "max_price": 35.0,
        "size": null
      },
      "query": "brown cardigan under $35",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "tan"
          ],
          "condition": "excellent",
          "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
          "id": "lst_008",
          "platform": "depop",
          "price": 35.0,
          "size": "One Size / Oversized",
          "style_tags": [
            "cottagecore",
            "cozy",
            "oversized",
            "earth tones",
            "knitwear"
          ],
          "title": "Knit Cardigan \u2014 Chunky Brown"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "tan"
        ],
        "condition": "excellent",
        "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
        "id": "lst_008",
        "platform": "depop",
        "price": 35.0,
        "size": "One Size / Oversized",
        "style_tags": [
          "cottagecore",
          "cozy",
          "oversized",
          "earth tones",
          "knitwear"
        ],
        "title": "Knit Cardigan \u2014 Chunky Brown"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "55d420f4db4e"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:47.733186+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "55d420f4db4e",
    "method": "POST",
    "path": "/ask",
    "query": "brown cardigan under $35",
    "status": 200,
    "duration_ms": 2127.51,
    "search_results": 4,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: hoodie request is logged

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
      "fit_card": "Nothing beats the ultimate worn-in feel of this faded black vintage graphic hoodie, scored on Depop for just $26. Style it grungy with baggy denim and combat boots, or keep it balanced by layering it over a ribbed white tank with wide-leg khaki trousers and chunky sneakers. It has that perfectly distressed, lived-in look that instantly makes any outfit effortless.",
      "outfit_suggestion": "Here are two complete outfits centered around your new faded black graphic hoodie, built entirely from your wardrobe:\n\n### Outfit 1: 90s Grunge Streetwear\n*Lean into the worn-in texture of the hoodie with heavy denim and combat boots.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hoodie drape loosely over the high-waisted baggy jeans. Pair with the combat boots to lean into the grunge aesthetic, and throw on the black crossbody bag for an easy, utilitarian everyday look.\n\n### Outfit 2: Casual High-Low Contrast\n*Pair the slouchy, faded hoodie with structured earth-tone trousers for a balanced, laid-back streetwear look.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item) layered over the White ribbed tank top (`w_003`) peeking out the bottom\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Wear the white ribbed tank underneath so a bit of white pops at the hem. Tuck the wide-leg khaki trousers in at the waist using the brown leather belt for some contrast, and finish the outfit with the chunky white sneakers to keep it sporty and relaxed.",
      "parsed": {
        "description": "vintage hoodie",
        "max_price": 45.0,
        "size": null
      },
      "query": "vintage hoodie under $45",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
          "id": "lst_015",
          "platform": "depop",
          "price": 26.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "graphic",
            "streetwear"
          ],
          "title": "Vintage Graphic Hoodie \u2014 Faded Black"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "navy"
          ],
          "condition": "good",
          "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
          "id": "lst_012",
          "platform": "thredUp",
          "price": 20.0,
          "size": "XL (fits oversized)",
          "style_tags": [
            "vintage",
            "basics",
            "oversized",
            "classic"
          ],
          "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "good",
          "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
          "id": "lst_006",
          "platform": "depop",
          "price": 24.0,
          "size": "L",
          "style_tags": [
            "graphic tee",
            "vintage",
            "grunge",
            "streetwear",
            "band tee"
          ],
          "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "blue",
            "indigo"
          ],
          "condition": "good",
          "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
          "id": "lst_001",
          "platform": "depop",
          "price": 38.0,
          "size": "W30 L30",
          "style_tags": [
            "vintage",
            "classic",
            "denim",
            "streetwear"
          ],
          "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "burgundy",
            "wine"
          ],
          "condition": "excellent",
          "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
          "id": "lst_020",
          "platform": "thredUp",
          "price": 16.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "basics",
            "earth tones",
            "classic"
          ],
          "title": "Henley Long Sleeve \u2014 Washed Burgundy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "white",
            "pink",
            "purple"
          ],
          "condition": "excellent",
          "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
          "id": "lst_002",
          "platform": "depop",
          "price": 18.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "vintage",
            "graphic tee",
            "cottagecore"
          ],
          "title": "Y2K Baby Tee \u2014 Butterfly Print"
        },
        {
          "brand": "Ralph Lauren",
          "category": "tops",
          "colors": [
            "green",
            "forest green"
          ],
          "condition": "good",
          "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
          "id": "lst_024",
          "platform": "thredUp",
          "price": 18.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "classic",
            "earth tones"
          ],
          "title": "Vintage Polo Shirt \u2014 Forest Green"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "5d1f87d2669a"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:57:50.638482+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "5d1f87d2669a",
    "method": "POST",
    "path": "/ask",
    "query": "vintage hoodie under $45",
    "status": 200,
    "duration_ms": 2886.01,
    "search_results": 10,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 4: graphic tee listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_graphic_tee_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_graphic_tee_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: denim jacket listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_denim_jacket_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_denim_jacket_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: jeans listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_jeans_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_jeans_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: cardigan listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_cardigan_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_cardigan_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: hoodie listing ID reaches suggest_outfit

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

#### Criterion 5: missing query field

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
  "request_id": "6b682d6f98c9"
}
```

#### Criterion 5: empty query string

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
  "request_id": "7c57378555b9"
}
```

#### Criterion 5: whitespace-only query

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
  "request_id": "6dab3a0cdf7d"
}
```

#### Criterion 5: null query

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
  "request_id": "9223f167b05e"
}
```

#### Criterion 5: query field omitted in alternate payload

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
  "request_id": "9dda0991373b"
}
```

### Run 3

#### Criterion 1: valid graphic tee request

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
    "fit_card": "Scored this soft, worn-in 2003 tour bootleg graphic tee on Depop for just $24, and it has the absolute best boxy fit. I love styling the faded black cotton either layered under a cropped zip hoodie for casual streetwear days or tucked into wide-leg khakis with heavy combat boots for a grunge edge.",
    "outfit_suggestion": "Here are two complete outfits centered around your new vintage graphic tee, using pieces straight from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n*Play up the bootleg band tee vibe with relaxed denim and classic streetwear layers.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Outerwear:** Black cropped zip hoodie (`w_005`) worn unzipped over the tee\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hem of the boxy tee peek out from under the cropped zip hoodie for a layered, textured look. Pair with the baggy dark-wash jeans and finish with the chunky white sneakers and crossbody bag for an easy everyday streetwear fit.\n\n### Outfit 2: Grunge-Inspired Contrast\n*Lean into the grunge aesthetic by pairing the faded black tee with khaki and heavy boots.*\n* **Top:** Graphic Tee \u2014 2003 Tour Bootleg Style (Thrifted)\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Outerwear:** Vintage black denim jacket (`w_006`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Tuck the graphic tee loosely into the wide-leg khaki trousers, cinched with the brown leather belt to add definition. Throw on the slightly cropped black denim jacket and anchor the look with the black combat boots to lean into the vintage, worn-in edge of the tee.",
    "parsed": {
      "description": "vintage graphic tee",
      "max_price": 30.0,
      "size": null
    },
    "query": "vintage graphic tee under $30",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "white",
          "pink",
          "purple"
        ],
        "condition": "excellent",
        "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
        "id": "lst_002",
        "platform": "depop",
        "price": 18.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "vintage",
          "graphic tee",
          "cottagecore"
        ],
        "title": "Y2K Baby Tee \u2014 Butterfly Print"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "grey",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.",
        "id": "lst_033",
        "platform": "depop",
        "price": 19.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "band tee",
          "graphic tee",
          "streetwear"
        ],
        "title": "Vintage Band Tee \u2014 Faded Grey"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "navy"
        ],
        "condition": "good",
        "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
        "id": "lst_012",
        "platform": "thredUp",
        "price": 20.0,
        "size": "XL (fits oversized)",
        "style_tags": [
          "vintage",
          "basics",
          "oversized",
          "classic"
        ],
        "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "burgundy",
          "wine"
        ],
        "condition": "excellent",
        "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
        "id": "lst_020",
        "platform": "thredUp",
        "price": 16.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "basics",
          "earth tones",
          "classic"
        ],
        "title": "Henley Long Sleeve \u2014 Washed Burgundy"
      },
      {
        "brand": "Ralph Lauren",
        "category": "tops",
        "colors": [
          "green",
          "forest green"
        ],
        "condition": "good",
        "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
        "id": "lst_024",
        "platform": "thredUp",
        "price": 18.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "classic",
          "earth tones"
        ],
        "title": "Vintage Polo Shirt \u2014 Forest Green"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black"
      ],
      "condition": "good",
      "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
      "id": "lst_006",
      "platform": "depop",
      "price": 24.0,
      "size": "L",
      "style_tags": [
        "graphic tee",
        "vintage",
        "grunge",
        "streetwear",
        "band tee"
      ],
      "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "50246d19a022"
}
```

#### Criterion 1: valid denim jacket request

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
    "search_results": [
      {
        "brand": "Wrangler",
        "category": "outerwear",
        "colors": [
          "light blue"
        ],
        "condition": "excellent",
        "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
        "id": "lst_007",
        "platform": "poshmark",
        "price": 42.0,
        "size": "S",
        "style_tags": [
          "denim",
          "vintage",
          "classic",
          "streetwear"
        ],
        "title": "Denim Jacket \u2014 Light Wash, Cropped"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "light blue",
          "blue"
        ],
        "condition": "good",
        "description": "DIY cutoff denim shorts from Levi's 501s. Raw hem, slightly frayed. High-waisted. Perfect summer length.",
        "id": "lst_016",
        "platform": "poshmark",
        "price": 24.0,
        "size": "W27",
        "style_tags": [
          "vintage",
          "denim",
          "summer",
          "classic"
        ],
        "title": "High-Waisted Denim Shorts \u2014 Cutoff"
      },
      {
        "brand": null,
        "category": "outerwear",
        "colors": [
          "medium blue"
        ],
        "condition": "good",
        "description": "Denim vest with silver stud detailing along the collar and pockets. Classic rock-inspired customization. Fits like a medium.",
        "id": "lst_038",
        "platform": "depop",
        "price": 27.0,
        "size": "M",
        "style_tags": [
          "grunge",
          "vintage",
          "denim",
          "customized",
          "rock"
        ],
        "title": "Denim Vest \u2014 Medium Wash, Studded"
      },
      {
        "brand": "Champion",
        "category": "outerwear",
        "colors": [
          "navy",
          "white"
        ],
        "condition": "excellent",
        "description": "Authentic 90s track jacket with stripe detail down the sleeves. Full zip. Lightweight \u2014 great for layering.",
        "id": "lst_004",
        "platform": "poshmark",
        "price": 45.0,
        "size": "M",
        "style_tags": [
          "90s",
          "vintage",
          "athletic",
          "streetwear"
        ],
        "title": "90s Track Jacket \u2014 Navy/White Stripe"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "black",
          "faded black"
        ],
        "condition": "good",
        "description": "Faded black straight-leg jeans. Sits at the hips, classic fit. Slightly cropped length. No rips, just natural fading.",
        "id": "lst_037",
        "platform": "thredUp",
        "price": 30.0,
        "size": "W28",
        "style_tags": [
          "vintage",
          "classic",
          "grunge",
          "denim"
        ],
        "title": "Straight Leg Black Jeans \u2014 Faded"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "blue",
          "indigo"
        ],
        "condition": "good",
        "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
        "id": "lst_001",
        "platform": "depop",
        "price": 38.0,
        "size": "W30 L30",
        "style_tags": [
          "vintage",
          "classic",
          "denim",
          "streetwear"
        ],
        "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
      }
    ],
    "selected_item": {
      "brand": "Wrangler",
      "category": "outerwear",
      "colors": [
        "light blue"
      ],
      "condition": "excellent",
      "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
      "id": "lst_007",
      "platform": "poshmark",
      "price": 42.0,
      "size": "S",
      "style_tags": [
        "denim",
        "vintage",
        "classic",
        "streetwear"
      ],
      "title": "Denim Jacket \u2014 Light Wash, Cropped"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "6a5fc6853df4"
}
```

#### Criterion 1: valid jeans request

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
    "fit_card": "Every wardrobe needs a good sheer black mesh long-sleeve for effortless layering, and I've been living in this stretchy, Y2K-inspired staple lately. Throw it on with baggy dark-wash denim and chunky white sneakers for a textured streetwear look, or dress it down with wide-leg trousers and combat boots. Grab this excellent-condition piece for just $15 over on my Depop before it's gone!",
    "outfit_suggestion": "Here are two complete outfits centered around the thrifted sheer black mesh long-sleeve top, built entirely from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n* **Base Layer:** Thrifted mesh long-sleeve top worn over the **White ribbed tank top** (w_003) for a textured, dimensional look.\n* **Bottoms:** **Baggy straight-leg jeans, dark wash** (w_001).\n* **Outerwear:** **Black cropped zip hoodie** (w_005) layered on top.\n* **Shoes:** **Chunky white sneakers** (w_007).\n* **Accessories:** **Black crossbody bag** (w_010).\n\n### Outfit 2: Grunge-Inspired Monochrome\n* **Base Layer:** Thrifted mesh long-sleeve top worn solo or layered over the white tank.\n* **Bottoms:** **Wide-leg khaki trousers** (w_002) paired with the **Brown leather belt** (w_009) to add definition at the waist.\n* **Outerwear:** **Vintage black denim jacket** (w_006) thrown over the shoulders.\n* **Shoes:** **Black combat boots** (w_008) to lean into the grunge aesthetic.\n* **Accessories:** **Black crossbody bag** (w_010).",
    "parsed": {
      "description": "black jeans",
      "max_price": 40.0,
      "size": "M"
    },
    "query": "black jeans size M under $40",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "excellent",
        "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
        "id": "lst_017",
        "platform": "depop",
        "price": 15.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "grunge",
          "goth",
          "layering"
        ],
        "title": "Mesh Long-Sleeve Top \u2014 Black"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black"
      ],
      "condition": "excellent",
      "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
      "id": "lst_017",
      "platform": "depop",
      "price": 15.0,
      "size": "S/M",
      "style_tags": [
        "y2k",
        "grunge",
        "goth",
        "layering"
      ],
      "title": "Mesh Long-Sleeve Top \u2014 Black"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "e176f2d00b99"
}
```

#### Criterion 1: valid cardigan request

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
    "fit_card": "Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.",
    "outfit_suggestion": "Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:\n\n### Outfit 1: Casual & Minimalist Earth Tones\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Wide-leg khaki trousers\n* **Accessories:** Brown leather belt\n* **Shoes:** Chunky white sneakers\n* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.\n\n### Outfit 2: Contrast Denim & Edge\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Baggy straight-leg jeans, dark wash\n* **Shoes:** Black combat boots\n* **Accessories:** Black crossbody bag\n* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.",
    "parsed": {
      "description": "brown cardigan",
      "max_price": 35.0,
      "size": null
    },
    "query": "brown cardigan under $35",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "tan"
        ],
        "condition": "excellent",
        "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
        "id": "lst_008",
        "platform": "depop",
        "price": 35.0,
        "size": "One Size / Oversized",
        "style_tags": [
          "cottagecore",
          "cozy",
          "oversized",
          "earth tones",
          "knitwear"
        ],
        "title": "Knit Cardigan \u2014 Chunky Brown"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "brown",
        "tan"
      ],
      "condition": "excellent",
      "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
      "id": "lst_008",
      "platform": "depop",
      "price": 35.0,
      "size": "One Size / Oversized",
      "style_tags": [
        "cottagecore",
        "cozy",
        "oversized",
        "earth tones",
        "knitwear"
      ],
      "title": "Knit Cardigan \u2014 Chunky Brown"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "ec50dbb57552"
}
```

#### Criterion 1: valid hoodie request

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
    "fit_card": "Nothing beats the ultimate worn-in feel of this faded black vintage graphic hoodie, scored on Depop for just $26. Style it grungy with baggy denim and combat boots, or keep it balanced by layering it over a ribbed white tank with wide-leg khaki trousers and chunky sneakers. It has that perfectly distressed, lived-in look that instantly makes any outfit effortless.",
    "outfit_suggestion": "Here are two complete outfits centered around your new faded black graphic hoodie, built entirely from your wardrobe:\n\n### Outfit 1: 90s Grunge Streetwear\n*Lean into the worn-in texture of the hoodie with heavy denim and combat boots.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hoodie drape loosely over the high-waisted baggy jeans. Pair with the combat boots to lean into the grunge aesthetic, and throw on the black crossbody bag for an easy, utilitarian everyday look.\n\n### Outfit 2: Casual High-Low Contrast\n*Pair the slouchy, faded hoodie with structured earth-tone trousers for a balanced, laid-back streetwear look.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item) layered over the White ribbed tank top (`w_003`) peeking out the bottom\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Wear the white ribbed tank underneath so a bit of white pops at the hem. Tuck the wide-leg khaki trousers in at the waist using the brown leather belt for some contrast, and finish the outfit with the chunky white sneakers to keep it sporty and relaxed.",
    "parsed": {
      "description": "vintage hoodie",
      "max_price": 45.0,
      "size": null
    },
    "query": "vintage hoodie under $45",
    "search_results": [
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "navy"
        ],
        "condition": "good",
        "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
        "id": "lst_012",
        "platform": "thredUp",
        "price": 20.0,
        "size": "XL (fits oversized)",
        "style_tags": [
          "vintage",
          "basics",
          "oversized",
          "classic"
        ],
        "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "cream",
          "tan"
        ],
        "condition": "good",
        "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
        "id": "lst_030",
        "platform": "thredUp",
        "price": 25.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "knitwear",
          "dark academia",
          "earth tones"
        ],
        "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
      },
      {
        "brand": "Levi's",
        "category": "bottoms",
        "colors": [
          "blue",
          "indigo"
        ],
        "condition": "good",
        "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
        "id": "lst_001",
        "platform": "depop",
        "price": 38.0,
        "size": "W30 L30",
        "style_tags": [
          "vintage",
          "classic",
          "denim",
          "streetwear"
        ],
        "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown"
        ],
        "condition": "excellent",
        "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
        "id": "lst_014",
        "platform": "thredUp",
        "price": 12.0,
        "size": "One Size (adjustable)",
        "style_tags": [
          "vintage",
          "western",
          "classic",
          "earth tones"
        ],
        "title": "Leather Belt \u2014 Brown, Braided"
      },
      {
        "brand": null,
        "category": "accessories",
        "colors": [
          "brown",
          "tan",
          "plaid"
        ],
        "condition": "excellent",
        "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
        "id": "lst_034",
        "platform": "thredUp",
        "price": 14.0,
        "size": "One Size",
        "style_tags": [
          "90s",
          "streetwear",
          "vintage",
          "accessories"
        ],
        "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "burgundy",
          "wine"
        ],
        "condition": "excellent",
        "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
        "id": "lst_020",
        "platform": "thredUp",
        "price": 16.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "basics",
          "earth tones",
          "classic"
        ],
        "title": "Henley Long Sleeve \u2014 Washed Burgundy"
      },
      {
        "brand": null,
        "category": "tops",
        "colors": [
          "white",
          "pink",
          "purple"
        ],
        "condition": "excellent",
        "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
        "id": "lst_002",
        "platform": "depop",
        "price": 18.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "vintage",
          "graphic tee",
          "cottagecore"
        ],
        "title": "Y2K Baby Tee \u2014 Butterfly Print"
      },
      {
        "brand": "Ralph Lauren",
        "category": "tops",
        "colors": [
          "green",
          "forest green"
        ],
        "condition": "good",
        "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
        "id": "lst_024",
        "platform": "thredUp",
        "price": 18.0,
        "size": "M",
        "style_tags": [
          "vintage",
          "preppy",
          "classic",
          "earth tones"
        ],
        "title": "Vintage Polo Shirt \u2014 Forest Green"
      }
    ],
    "selected_item": {
      "brand": null,
      "category": "tops",
      "colors": [
        "black",
        "charcoal"
      ],
      "condition": "fair",
      "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
      "id": "lst_015",
      "platform": "depop",
      "price": 26.0,
      "size": "L",
      "style_tags": [
        "vintage",
        "grunge",
        "graphic",
        "streetwear"
      ],
      "title": "Vintage Graphic Hoodie \u2014 Faded Black"
    },
    "wardrobe": {
      "items": [
        {
          "category": "bottoms",
          "colors": [
            "dark blue",
            "indigo"
          ],
          "id": "w_001",
          "name": "Baggy straight-leg jeans, dark wash",
          "notes": "High-waisted, sits above the hip",
          "style_tags": [
            "denim",
            "streetwear",
            "baggy"
          ]
        },
        {
          "category": "bottoms",
          "colors": [
            "khaki",
            "tan"
          ],
          "id": "w_002",
          "name": "Wide-leg khaki trousers",
          "notes": null,
          "style_tags": [
            "earth tones",
            "minimal",
            "wide-leg"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "white"
          ],
          "id": "w_003",
          "name": "White ribbed tank top",
          "notes": "Goes with everything",
          "style_tags": [
            "basics",
            "minimal",
            "fitted"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "id": "w_004",
          "name": "Oversized grey crewneck sweatshirt",
          "notes": "Really oversized \u2014 drops below the hip",
          "style_tags": [
            "oversized",
            "basics",
            "cozy"
          ]
        },
        {
          "category": "tops",
          "colors": [
            "black"
          ],
          "id": "w_005",
          "name": "Black cropped zip hoodie",
          "notes": null,
          "style_tags": [
            "athletic",
            "streetwear",
            "cropped"
          ]
        },
        {
          "category": "outerwear",
          "colors": [
            "black"
          ],
          "id": "w_006",
          "name": "Vintage black denim jacket",
          "notes": "Slightly cropped",
          "style_tags": [
            "denim",
            "vintage",
            "classic"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "white"
          ],
          "id": "w_007",
          "name": "Chunky white sneakers",
          "notes": null,
          "style_tags": [
            "sneakers",
            "chunky",
            "streetwear"
          ]
        },
        {
          "category": "shoes",
          "colors": [
            "black"
          ],
          "id": "w_008",
          "name": "Black combat boots",
          "notes": "Lace-up, mid-ankle height",
          "style_tags": [
            "boots",
            "grunge",
            "classic"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "id": "w_009",
          "name": "Brown leather belt",
          "notes": null,
          "style_tags": [
            "classic",
            "earth tones",
            "accessories"
          ]
        },
        {
          "category": "accessories",
          "colors": [
            "black"
          ],
          "id": "w_010",
          "name": "Black crossbody bag",
          "notes": null,
          "style_tags": [
            "minimal",
            "accessories",
            "everyday"
          ]
        }
      ]
    }
  },
  "request_id": "6f1a9fd7ff65"
}
```

#### Criterion 2: graphic tee timeout

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
  "request_id": "42aa0b62a9ae"
}
```

#### Criterion 2: denim jacket timeout

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
  "request_id": "e2eecb692b1d"
}
```

#### Criterion 2: jeans timeout

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
  "request_id": "dcd890df4537"
}
```

#### Criterion 2: cardigan timeout

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
  "request_id": "a8255c4aeb87"
}
```

#### Criterion 2: hoodie timeout

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
  "request_id": "17ab25193c4b"
}
```

#### Criterion 3: graphic tee request is logged

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
      "parsed": {
        "description": "vintage graphic tee",
        "max_price": 30.0,
        "size": null
      },
      "query": "vintage graphic tee under $30",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "good",
          "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
          "id": "lst_006",
          "platform": "depop",
          "price": 24.0,
          "size": "L",
          "style_tags": [
            "graphic tee",
            "vintage",
            "grunge",
            "streetwear",
            "band tee"
          ],
          "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "white",
            "pink",
            "purple"
          ],
          "condition": "excellent",
          "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
          "id": "lst_002",
          "platform": "depop",
          "price": 18.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "vintage",
            "graphic tee",
            "cottagecore"
          ],
          "title": "Y2K Baby Tee \u2014 Butterfly Print"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "grey",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.",
          "id": "lst_033",
          "platform": "depop",
          "price": 19.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "band tee",
            "graphic tee",
            "streetwear"
          ],
          "title": "Vintage Band Tee \u2014 Faded Grey"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
          "id": "lst_015",
          "platform": "depop",
          "price": 26.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "graphic",
            "streetwear"
          ],
          "title": "Vintage Graphic Hoodie \u2014 Faded Black"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "navy"
          ],
          "condition": "good",
          "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
          "id": "lst_012",
          "platform": "thredUp",
          "price": 20.0,
          "size": "XL (fits oversized)",
          "style_tags": [
            "vintage",
            "basics",
            "oversized",
            "classic"
          ],
          "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "burgundy",
            "wine"
          ],
          "condition": "excellent",
          "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
          "id": "lst_020",
          "platform": "thredUp",
          "price": 16.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "basics",
            "earth tones",
            "classic"
          ],
          "title": "Henley Long Sleeve \u2014 Washed Burgundy"
        },
        {
          "brand": "Ralph Lauren",
          "category": "tops",
          "colors": [
            "green",
            "forest green"
          ],
          "condition": "good",
          "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
          "id": "lst_024",
          "platform": "thredUp",
          "price": 18.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "classic",
            "earth tones"
          ],
          "title": "Vintage Polo Shirt \u2014 Forest Green"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "good",
        "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
        "id": "lst_006",
        "platform": "depop",
        "price": 24.0,
        "size": "L",
        "style_tags": [
          "graphic tee",
          "vintage",
          "grunge",
          "streetwear",
          "band tee"
        ],
        "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "8b381725b6d1"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:58:08.957738+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "8b381725b6d1",
    "method": "POST",
    "path": "/ask",
    "query": "vintage graphic tee under $30",
    "status": 200,
    "duration_ms": 3178.31,
    "search_results": 10,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: denim jacket request is logged

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
      "fit_card": "Scored this vintage Wrangler cropped denim jacket on Poshmark for just $42, and it\u2019s the ultimate blank canvas for layering. I love pairing the light wash with dark baggy denim and fresh white sneakers for an effortless streetwear vibe. It also looks amazing thrown over an oversized grey crewneck and khaki trousers for an easy mix of cool and warm tones.",
      "outfit_suggestion": "Here are two complete outfits built around your new Wrangler light-wash cropped denim jacket using items from your wardrobe:\n\n### Outfit 1: Canadian Tuxedo / Streetwear Edge\n*Play with denim-on-denim by contrasting the light-wash jacket with dark bottoms.*\n\n* **Top:** White ribbed tank top (`w_003`) tucked in to highlight the cropped fit of the jacket.\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`) \u2014 the high waist pairs great with the cropped jacket.\n* **Shoes:** Chunky white sneakers (`w_007`) to tie in the white tank top.\n* **Accessories:** Black crossbody bag (`w_010`).\n\n### Outfit 2: Casual Earth Tones\n*Contrast the cool light blue of the jacket with warm, neutral trousers.*\n\n* **Top:** Oversized grey crewneck sweatshirt (`w_004`) worn underneath as a cozy layer, letting the hem peek out below the cropped jacket.\n* **Bottoms:** Wide-leg khaki trousers (`w_002`).\n* **Shoes:** Black combat boots (`w_008`) to ground the lighter tones of the outfit.\n* **Accessories:** Brown leather belt (`w_009`) threaded through the trousers to pull the earth tones together.",
      "parsed": {
        "description": "denim jacket",
        "max_price": 50.0,
        "size": null
      },
      "query": "denim jacket under $50",
      "search_results": [
        {
          "brand": "Wrangler",
          "category": "outerwear",
          "colors": [
            "light blue"
          ],
          "condition": "excellent",
          "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
          "id": "lst_007",
          "platform": "poshmark",
          "price": 42.0,
          "size": "S",
          "style_tags": [
            "denim",
            "vintage",
            "classic",
            "streetwear"
          ],
          "title": "Denim Jacket \u2014 Light Wash, Cropped"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "light blue",
            "blue"
          ],
          "condition": "good",
          "description": "DIY cutoff denim shorts from Levi's 501s. Raw hem, slightly frayed. High-waisted. Perfect summer length.",
          "id": "lst_016",
          "platform": "poshmark",
          "price": 24.0,
          "size": "W27",
          "style_tags": [
            "vintage",
            "denim",
            "summer",
            "classic"
          ],
          "title": "High-Waisted Denim Shorts \u2014 Cutoff"
        },
        {
          "brand": null,
          "category": "outerwear",
          "colors": [
            "medium blue"
          ],
          "condition": "good",
          "description": "Denim vest with silver stud detailing along the collar and pockets. Classic rock-inspired customization. Fits like a medium.",
          "id": "lst_038",
          "platform": "depop",
          "price": 27.0,
          "size": "M",
          "style_tags": [
            "grunge",
            "vintage",
            "denim",
            "customized",
            "rock"
          ],
          "title": "Denim Vest \u2014 Medium Wash, Studded"
        },
        {
          "brand": "Champion",
          "category": "outerwear",
          "colors": [
            "navy",
            "white"
          ],
          "condition": "excellent",
          "description": "Authentic 90s track jacket with stripe detail down the sleeves. Full zip. Lightweight \u2014 great for layering.",
          "id": "lst_004",
          "platform": "poshmark",
          "price": 45.0,
          "size": "M",
          "style_tags": [
            "90s",
            "vintage",
            "athletic",
            "streetwear"
          ],
          "title": "90s Track Jacket \u2014 Navy/White Stripe"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "black",
            "faded black"
          ],
          "condition": "good",
          "description": "Faded black straight-leg jeans. Sits at the hips, classic fit. Slightly cropped length. No rips, just natural fading.",
          "id": "lst_037",
          "platform": "thredUp",
          "price": 30.0,
          "size": "W28",
          "style_tags": [
            "vintage",
            "classic",
            "grunge",
            "denim"
          ],
          "title": "Straight Leg Black Jeans \u2014 Faded"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "blue",
            "indigo"
          ],
          "condition": "good",
          "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
          "id": "lst_001",
          "platform": "depop",
          "price": 38.0,
          "size": "W30 L30",
          "style_tags": [
            "vintage",
            "classic",
            "denim",
            "streetwear"
          ],
          "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
        }
      ],
      "selected_item": {
        "brand": "Wrangler",
        "category": "outerwear",
        "colors": [
          "light blue"
        ],
        "condition": "excellent",
        "description": "Cropped denim jacket in a light wash. Great structured shoulders. Blank canvas \u2014 no patches or pins but would be perfect to customize.",
        "id": "lst_007",
        "platform": "poshmark",
        "price": 42.0,
        "size": "S",
        "style_tags": [
          "denim",
          "vintage",
          "classic",
          "streetwear"
        ],
        "title": "Denim Jacket \u2014 Light Wash, Cropped"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "46634d1c74ff"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:58:12.853744+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "46634d1c74ff",
    "method": "POST",
    "path": "/ask",
    "query": "denim jacket under $50",
    "status": 200,
    "duration_ms": 3870.33,
    "search_results": 6,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: jeans request is logged

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
      "fit_card": "Every wardrobe needs a good sheer black mesh long-sleeve for effortless layering, and I've been living in this stretchy, Y2K-inspired staple lately. Throw it on with baggy dark-wash denim and chunky white sneakers for a textured streetwear look, or dress it down with wide-leg trousers and combat boots. Grab this excellent-condition piece for just $15 over on my Depop before it's gone!",
      "outfit_suggestion": "Here are two complete outfits centered around the thrifted sheer black mesh long-sleeve top, built entirely from your wardrobe:\n\n### Outfit 1: Y2K Streetwear Edge\n* **Base Layer:** Thrifted mesh long-sleeve top worn over the **White ribbed tank top** (w_003) for a textured, dimensional look.\n* **Bottoms:** **Baggy straight-leg jeans, dark wash** (w_001).\n* **Outerwear:** **Black cropped zip hoodie** (w_005) layered on top.\n* **Shoes:** **Chunky white sneakers** (w_007).\n* **Accessories:** **Black crossbody bag** (w_010).\n\n### Outfit 2: Grunge-Inspired Monochrome\n* **Base Layer:** Thrifted mesh long-sleeve top worn solo or layered over the white tank.\n* **Bottoms:** **Wide-leg khaki trousers** (w_002) paired with the **Brown leather belt** (w_009) to add definition at the waist.\n* **Outerwear:** **Vintage black denim jacket** (w_006) thrown over the shoulders.\n* **Shoes:** **Black combat boots** (w_008) to lean into the grunge aesthetic.\n* **Accessories:** **Black crossbody bag** (w_010).",
      "parsed": {
        "description": "black jeans",
        "max_price": 40.0,
        "size": "M"
      },
      "query": "black jeans size M under $40",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "excellent",
          "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
          "id": "lst_017",
          "platform": "depop",
          "price": 15.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "grunge",
            "goth",
            "layering"
          ],
          "title": "Mesh Long-Sleeve Top \u2014 Black"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black"
        ],
        "condition": "excellent",
        "description": "Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.",
        "id": "lst_017",
        "platform": "depop",
        "price": 15.0,
        "size": "S/M",
        "style_tags": [
          "y2k",
          "grunge",
          "goth",
          "layering"
        ],
        "title": "Mesh Long-Sleeve Top \u2014 Black"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "5168abd9eb34"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:58:14.774598+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "5168abd9eb34",
    "method": "POST",
    "path": "/ask",
    "query": "black jeans size M under $40",
    "status": 200,
    "duration_ms": 1900.29,
    "search_results": 1,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: cardigan request is logged

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
      "fit_card": "Nothing beats throwing on this super cozy chunky brown cardigan when the weather cools down, especially styled with wide-leg trousers or baggy denim. Grab it on Depop right now for just $35 to instantly level up your autumn layering game.",
      "outfit_suggestion": "Here are two complete outfits centered around your new chunky brown cardigan, built entirely from your wardrobe:\n\n### Outfit 1: Casual & Minimalist Earth Tones\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Wide-leg khaki trousers\n* **Accessories:** Brown leather belt\n* **Shoes:** Chunky white sneakers\n* **Styling details:** Tuck the white tank into the khaki trousers, secure with the brown leather belt to tie the earth tones together, and throw the oversized brown cardigan on top. Finish with chunky white sneakers for a clean, relaxed, everyday look.\n\n### Outfit 2: Contrast Denim & Edge\n* **Top:** White ribbed tank top\n* **Thrifted Item:** Chunky Brown Cardigan (layered over the tank)\n* **Bottoms:** Baggy straight-leg jeans, dark wash\n* **Shoes:** Black combat boots\n* **Accessories:** Black crossbody bag\n* **Styling details:** Pair the fitted white tank with the baggy dark wash jeans for a balanced silhouette. Layer the cozy brown cardigan over top for warmth and texture. Ground the outfit with black combat boots and add the black crossbody bag for an effortless, slightly grunge-leaning everyday fit.",
      "parsed": {
        "description": "brown cardigan",
        "max_price": 35.0,
        "size": null
      },
      "query": "brown cardigan under $35",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "tan"
          ],
          "condition": "excellent",
          "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
          "id": "lst_008",
          "platform": "depop",
          "price": 35.0,
          "size": "One Size / Oversized",
          "style_tags": [
            "cottagecore",
            "cozy",
            "oversized",
            "earth tones",
            "knitwear"
          ],
          "title": "Knit Cardigan \u2014 Chunky Brown"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "brown",
          "tan"
        ],
        "condition": "excellent",
        "description": "Super cozy oversized cardigan. Earth-tone brown, chunky knit. Hits at the hip. Perfect for layering over anything.",
        "id": "lst_008",
        "platform": "depop",
        "price": 35.0,
        "size": "One Size / Oversized",
        "style_tags": [
          "cottagecore",
          "cozy",
          "oversized",
          "earth tones",
          "knitwear"
        ],
        "title": "Knit Cardigan \u2014 Chunky Brown"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "056df5d5c683"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:58:17.617901+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "056df5d5c683",
    "method": "POST",
    "path": "/ask",
    "query": "brown cardigan under $35",
    "status": 200,
    "duration_ms": 2825.28,
    "search_results": 4,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 3: hoodie request is logged

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
      "fit_card": "Nothing beats the ultimate worn-in feel of this faded black vintage graphic hoodie, scored on Depop for just $26. Style it grungy with baggy denim and combat boots, or keep it balanced by layering it over a ribbed white tank with wide-leg khaki trousers and chunky sneakers. It has that perfectly distressed, lived-in look that instantly makes any outfit effortless.",
      "outfit_suggestion": "Here are two complete outfits centered around your new faded black graphic hoodie, built entirely from your wardrobe:\n\n### Outfit 1: 90s Grunge Streetwear\n*Lean into the worn-in texture of the hoodie with heavy denim and combat boots.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item)\n* **Bottoms:** Baggy straight-leg jeans, dark wash (`w_001`)\n* **Shoes:** Black combat boots (`w_008`)\n* **Accessories:** Black crossbody bag (`w_010`)\n* **Styling details:** Let the hoodie drape loosely over the high-waisted baggy jeans. Pair with the combat boots to lean into the grunge aesthetic, and throw on the black crossbody bag for an easy, utilitarian everyday look.\n\n### Outfit 2: Casual High-Low Contrast\n*Pair the slouchy, faded hoodie with structured earth-tone trousers for a balanced, laid-back streetwear look.*\n* **Top:** Vintage Graphic Hoodie \u2014 Faded Black (thrifting item) layered over the White ribbed tank top (`w_003`) peeking out the bottom\n* **Bottoms:** Wide-leg khaki trousers (`w_002`)\n* **Shoes:** Chunky white sneakers (`w_007`)\n* **Accessories:** Brown leather belt (`w_009`)\n* **Styling details:** Wear the white ribbed tank underneath so a bit of white pops at the hem. Tuck the wide-leg khaki trousers in at the waist using the brown leather belt for some contrast, and finish the outfit with the chunky white sneakers to keep it sporty and relaxed.",
      "parsed": {
        "description": "vintage hoodie",
        "max_price": 45.0,
        "size": null
      },
      "query": "vintage hoodie under $45",
      "search_results": [
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black",
            "charcoal"
          ],
          "condition": "fair",
          "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
          "id": "lst_015",
          "platform": "depop",
          "price": 26.0,
          "size": "L",
          "style_tags": [
            "vintage",
            "grunge",
            "graphic",
            "streetwear"
          ],
          "title": "Vintage Graphic Hoodie \u2014 Faded Black"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "navy"
          ],
          "condition": "good",
          "description": "Perfectly faded navy crewneck. Genuinely vintage \u2014 not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.",
          "id": "lst_012",
          "platform": "thredUp",
          "price": 20.0,
          "size": "XL (fits oversized)",
          "style_tags": [
            "vintage",
            "basics",
            "oversized",
            "classic"
          ],
          "title": "Oversized Crewneck Sweatshirt \u2014 Vintage Navy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "black"
          ],
          "condition": "good",
          "description": "Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.",
          "id": "lst_006",
          "platform": "depop",
          "price": 24.0,
          "size": "L",
          "style_tags": [
            "graphic tee",
            "vintage",
            "grunge",
            "streetwear",
            "band tee"
          ],
          "title": "Graphic Tee \u2014 2003 Tour Bootleg Style"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "brown",
            "cream",
            "tan"
          ],
          "condition": "good",
          "description": "Classic argyle knit vest in brown and cream. Fits medium. V-neck. Ideal for the dark academia or preppy vintage aesthetic.",
          "id": "lst_030",
          "platform": "thredUp",
          "price": 25.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "knitwear",
            "dark academia",
            "earth tones"
          ],
          "title": "Vintage Knit Vest \u2014 Argyle Brown/Cream"
        },
        {
          "brand": "Levi's",
          "category": "bottoms",
          "colors": [
            "blue",
            "indigo"
          ],
          "condition": "good",
          "description": "Classic 501s in a perfect medium wash. Some light fading at the knees which adds to the vintage look. No rips or stains.",
          "id": "lst_001",
          "platform": "depop",
          "price": 38.0,
          "size": "W30 L30",
          "style_tags": [
            "vintage",
            "classic",
            "denim",
            "streetwear"
          ],
          "title": "Vintage Levi's 501 Jeans \u2014 Medium Wash"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown"
          ],
          "condition": "excellent",
          "description": "Genuine leather braided belt. Adjustable, multiple holes. Classic Western buckle. Can be dressed up or down.",
          "id": "lst_014",
          "platform": "thredUp",
          "price": 12.0,
          "size": "One Size (adjustable)",
          "style_tags": [
            "vintage",
            "western",
            "classic",
            "earth tones"
          ],
          "title": "Leather Belt \u2014 Brown, Braided"
        },
        {
          "brand": null,
          "category": "accessories",
          "colors": [
            "brown",
            "tan",
            "plaid"
          ],
          "condition": "excellent",
          "description": "Reversible bucket hat \u2014 plaid on one side, solid tan on the other. Unstructured brim. One size fits most.",
          "id": "lst_034",
          "platform": "thredUp",
          "price": 14.0,
          "size": "One Size",
          "style_tags": [
            "90s",
            "streetwear",
            "vintage",
            "accessories"
          ],
          "title": "Bucket Hat \u2014 Reversible, Brown Plaid"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "burgundy",
            "wine"
          ],
          "condition": "excellent",
          "description": "Soft washed henley in a rich burgundy. Three-button placket. Slightly shrunken/cropped fit. 100% cotton.",
          "id": "lst_020",
          "platform": "thredUp",
          "price": 16.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "basics",
            "earth tones",
            "classic"
          ],
          "title": "Henley Long Sleeve \u2014 Washed Burgundy"
        },
        {
          "brand": null,
          "category": "tops",
          "colors": [
            "white",
            "pink",
            "purple"
          ],
          "condition": "excellent",
          "description": "Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.",
          "id": "lst_002",
          "platform": "depop",
          "price": 18.0,
          "size": "S/M",
          "style_tags": [
            "y2k",
            "vintage",
            "graphic tee",
            "cottagecore"
          ],
          "title": "Y2K Baby Tee \u2014 Butterfly Print"
        },
        {
          "brand": "Ralph Lauren",
          "category": "tops",
          "colors": [
            "green",
            "forest green"
          ],
          "condition": "good",
          "description": "Classic polo in forest green. Short sleeve, ribbed collar. Slightly boxy. The kind of piece that goes with everything.",
          "id": "lst_024",
          "platform": "thredUp",
          "price": 18.0,
          "size": "M",
          "style_tags": [
            "vintage",
            "preppy",
            "classic",
            "earth tones"
          ],
          "title": "Vintage Polo Shirt \u2014 Forest Green"
        }
      ],
      "selected_item": {
        "brand": null,
        "category": "tops",
        "colors": [
          "black",
          "charcoal"
        ],
        "condition": "fair",
        "description": "Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.",
        "id": "lst_015",
        "platform": "depop",
        "price": 26.0,
        "size": "L",
        "style_tags": [
          "vintage",
          "grunge",
          "graphic",
          "streetwear"
        ],
        "title": "Vintage Graphic Hoodie \u2014 Faded Black"
      },
      "wardrobe": {
        "items": [
          {
            "category": "bottoms",
            "colors": [
              "dark blue",
              "indigo"
            ],
            "id": "w_001",
            "name": "Baggy straight-leg jeans, dark wash",
            "notes": "High-waisted, sits above the hip",
            "style_tags": [
              "denim",
              "streetwear",
              "baggy"
            ]
          },
          {
            "category": "bottoms",
            "colors": [
              "khaki",
              "tan"
            ],
            "id": "w_002",
            "name": "Wide-leg khaki trousers",
            "notes": null,
            "style_tags": [
              "earth tones",
              "minimal",
              "wide-leg"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "white"
            ],
            "id": "w_003",
            "name": "White ribbed tank top",
            "notes": "Goes with everything",
            "style_tags": [
              "basics",
              "minimal",
              "fitted"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "grey",
              "charcoal"
            ],
            "id": "w_004",
            "name": "Oversized grey crewneck sweatshirt",
            "notes": "Really oversized \u2014 drops below the hip",
            "style_tags": [
              "oversized",
              "basics",
              "cozy"
            ]
          },
          {
            "category": "tops",
            "colors": [
              "black"
            ],
            "id": "w_005",
            "name": "Black cropped zip hoodie",
            "notes": null,
            "style_tags": [
              "athletic",
              "streetwear",
              "cropped"
            ]
          },
          {
            "category": "outerwear",
            "colors": [
              "black"
            ],
            "id": "w_006",
            "name": "Vintage black denim jacket",
            "notes": "Slightly cropped",
            "style_tags": [
              "denim",
              "vintage",
              "classic"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "white"
            ],
            "id": "w_007",
            "name": "Chunky white sneakers",
            "notes": null,
            "style_tags": [
              "sneakers",
              "chunky",
              "streetwear"
            ]
          },
          {
            "category": "shoes",
            "colors": [
              "black"
            ],
            "id": "w_008",
            "name": "Black combat boots",
            "notes": "Lace-up, mid-ankle height",
            "style_tags": [
              "boots",
              "grunge",
              "classic"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "brown"
            ],
            "id": "w_009",
            "name": "Brown leather belt",
            "notes": null,
            "style_tags": [
              "classic",
              "earth tones",
              "accessories"
            ]
          },
          {
            "category": "accessories",
            "colors": [
              "black"
            ],
            "id": "w_010",
            "name": "Black crossbody bag",
            "notes": null,
            "style_tags": [
              "minimal",
              "accessories",
              "everyday"
            ]
          }
        ]
      }
    },
    "request_id": "a73b872d330d"
  },
  "log_record": {
    "timestamp": "2026-11-16T19:58:20.447776+00:00",
    "level": "INFO",
    "event": "request_completed",
    "request_id": "a73b872d330d",
    "method": "POST",
    "path": "/ask",
    "query": "vintage hoodie under $45",
    "status": 200,
    "duration_ms": 2819.08,
    "search_results": 10,
    "model_calls": 0,
    "error": false
  }
}
```

#### Criterion 4: graphic tee listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_graphic_tee_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_graphic_tee_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: denim jacket listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_denim_jacket_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_denim_jacket_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: jeans listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_jeans_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_jeans_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: cardigan listing ID reaches suggest_outfit

- Source: `agent.py::run_agent`
- Pass: `True`
- Expected:
```json
"search_listings ID equals suggest_outfit ID"
```
- Actual output:
```json
{
  "selected_id": "test_cardigan_listing_ID_reaches_suggest_outfit",
  "suggested_id": "test_cardigan_listing_ID_reaches_suggest_outfit",
  "error": null
}
```

#### Criterion 4: hoodie listing ID reaches suggest_outfit

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

#### Criterion 5: missing query field

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
  "request_id": "21ce79c9f8e0"
}
```

#### Criterion 5: empty query string

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
  "request_id": "a824e2216668"
}
```

#### Criterion 5: whitespace-only query

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
  "request_id": "625ff6019afc"
}
```

#### Criterion 5: null query

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
  "request_id": "245359e4d7ec"
}
```

#### Criterion 5: query field omitted in alternate payload

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
  "request_id": "f1fcbc3acf3c"
}
```
