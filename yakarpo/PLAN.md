# YakarPo (יקר פה): Israel vs. Europe price comparison

> **The voice can be angry. The numbers can't be wrong.**
> Every sourced claim gets shared. Every mistake gets screenshotted by the people who profit from high prices.
> Being credible is what gives the project any power.

---

## 1. Premise

Israelis pay far more for everyday goods than Europeans do, and most of the gap comes from **policy and market structure**, not fate.
The platform shows the gap in real prices, explains where it comes from, and turns public anger into pressure on specific decision-makers.

### Headline facts to anchor on (re-verify before publishing)

| Claim | Source |
|---|---|
| Food prices in Israel are ~51% above the EU and ~37% above the OECD | Israeli State Comptroller, cost-of-living report ([mevaker.gov.il](https://www.mevaker.gov.il/en/media/magazine/cost-of-living)) |
| Food & beverage prices are 52% above the OECD average, 2nd highest after South Korea (2024 data) | OECD data via [Times of Israel](https://www.timesofisrael.com/food-and-beverage-prices-in-israel-52-higher-than-oecd-average-report/) |
| The "What's good for Europe is good for Israel" import reform (phased 2025–2028) has so far struggled to lower prices | [State Comptroller 2025 audit](https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/2025/2025-10/EN/2025-102025.10-202-Import-Taktzir-EN.pdf), [Compliance & Risks review](https://www.complianceandrisks.com/blog/whats-good-for-europe-is-good-for-israel-qa-reviewing-the-import-reform-one-year-in/) |

The founder's own experience in the Netherlands, that groceries cost about half of what they cost in Israel, is **in line with the official ~51% EU gap**.
That's the story: it's not just a feeling, the state's own auditor says so.

### Positioning: "Explained, not excused"

The strongest version of the argument doesn't claim there's *no* reason for the gap. It shows each reason, how much it plausibly explains, and **whether it could be fixed by policy**.
Once the costs that can't be avoided (small market, no land trade with neighbors) are accounted for, the gap that's left is the scandal.

---

## 2. Core features

### 2.1 Receipt Shock (the flagship)
The user uploads a receipt from any store in any country and gets back "this basket would cost X in Israel".

**Pipeline**
1. **Extract.** A vision LLM (Claude) reads the receipt image into structured line items: raw text, brand, product, size/unit, quantity, price, currency, store, date.
2. **Scrub.** Remove PII (card digits, loyalty IDs, cashier names, exact store address). Don't store the image by default (GDPR, since many users are in the EU).
3. **Normalize.** Canonical product plus unit price (per kg / liter / unit). Translate Dutch, German, French and other labels.
4. **Match to Israel** in three tiers, each shown with a confidence badge:
   - **Exact:** same barcode or same brand, product and size, found in Israeli price-transparency data.
   - **Equivalent:** same category and spec (e.g. "1L 3% milk", "500g spaghetti").
   - **Cheapest Israeli alternative:** the most generous comparison, which heads off the "you picked the expensive brand" rebuttal.
5. **Price in Israel.** Show both the **median** and the **cheapest** chain price (e.g. Rami Levy vs. Shufersal), converted at the ECB daily rate on the receipt date.
6. **Output.** A shareable card (image plus link), a line-by-line breakdown, and a "you'd pay ₪X more" total.
7. **Correction loop.** Users can fix wrong matches, which improves the matcher. With consent, the anonymized foreign prices go into an open **European price database**. The more people use it, the more data we have.

### 2.2 Fair-comparison lenses (toggle on every comparison)
- **Nominal** (converted at the exchange rate)
- **Minutes of work.** How long a median earner, or a minimum-wage earner, works to buy the item in each country. This is usually the most viral and the hardest to argue with.
- **VAT removed.** Separates tax policy from market pricing.
- **PPP-adjusted.** For the economists.

### 2.3 "For & Against" factor panel
For each factor: what it is, which direction it pushes prices, a rough estimate of how much of the gap it explains, whether policy can fix it, and the source.

| Factor | Direction | Fixable by policy? |
|---|---|---|
| Average / median net wage | Context: affordability | – |
| Minimum wage | Context | – |
| Rent as a share of income | Context: squeezes the budget further | Partly |
| VAT: IL 18% (fresh fruit & veg 0%) vs. NL 9% on food | Raises IL prices | **Yes** |
| Income tax / tax wedge at median wage | Context | Yes |
| Retail concentration (share of the top 3 chains, HHI) | Raises IL prices | **Yes** (competition law) |
| Supplier concentration (a few big importers and manufacturers) | Raises IL prices | **Yes** |
| Import tariffs and quotas (dairy, eggs, meat, some produce) | Raises IL prices | **Yes** |
| Import standards and bureaucracy (pre-reform and in transition) | Raises IL prices | **Yes** (reform in progress) |
| Exclusive importers / barriers to parallel import | Raises IL prices | **Yes** |
| Kashrut certification and supervision costs | Raises IL prices, modestly | Partly |
| Small market, no land trade with neighbors ("island economy") | Raises IL prices | Mostly no |
| Strong shekel | Makes IL look pricier in EUR | No (macro) |
| Security / war-time costs and disruptions | Raises IL prices | Mostly no |

### 2.4 Product Wall of Shame
The same branded products (Coca-Cola, Nutella, Barilla, Heinz, Pampers, Nescafé…) priced in Israel vs. NL, DE, FR, ES, GR, CY and others.
Name the **importer or manufacturer** responsible, using only verifiable facts (see Legal).

### 2.5 Reform Tracker
Did the prices of products covered by "What's good for Europe is good for Israel" actually fall after each phase came into force? Track the price before and after for every affected category.
This keeps the pressure on after the headlines fade.

### 2.6 Open data & journalist kit
A public API and CSV downloads, a methodology page, and a "cite us" button. Journalists turn this into coverage, and coverage is what builds up lasting pressure.

---

## 3. Data sources

**Israel**
- **Price Transparency Law (2014).** Chains with 3+ stores must publish full price, promotion and store files (XML) several times a day. Official, complete and free.
  Existing open-source tooling: [OpenIsraeliSupermarkets scrapers](https://github.com/OpenIsraeliSupermarkets/israeli-supermarket-scarpers), [`israeli-prices` (PyPI)](https://pypi.org/project/israeli-prices/0.2.0/).
- CBS (Central Bureau of Statistics): CPI, wages, rent.
- State Comptroller, Competition Authority and Knesset Research Center reports.

**Europe / world**
- Eurostat: comparative price levels / PPPs (`prc_ppp_ind`), HICP, wages, minimum wages.
- OECD: price levels, wages, tax wedge, Israel economic surveys.
- **Open Food Facts / Open Prices:** crowdsourced product prices and barcodes (open license).
- Retailer websites (Albert Heijn, Jumbo, Lidl, Carrefour, Mercadona…). Check each site's terms before scraping, and prefer receipts and Open Prices.
- **Our own receipts**, with consent. This grows into the project's biggest data asset.

**Rules:** Every number carries a source and a date. Stale data is flagged automatically.

---

## 4. Social media & distribution

### What *not* to do: fake personas
Networks of AI accounts posing as real people count as **coordinated inauthentic behavior** on Meta, X and TikTok. They get banned in bulk and would let critics dismiss the whole project as a bot campaign or foreign influence operation. That would destroy the credibility the project depends on.

### What to do instead
- **One official, openly AI-assisted account per platform.** Claude drafts content from the live data. A human approves it at first; once the templates are trusted, some post types can go out automatically.
- **Content formats:** "Receipt of the day" from real users (with consent), a "Product of the week" shame card, "Minutes of work" comparisons, reform tracker updates, and myth-busting ("Is it really because of kashrut?").
- **A WhatsApp / Telegram bot is the key interactive channel.** Israelis live on WhatsApp. "Send a photo of your receipt to this number" and get a share card back within seconds. It's easy to forward, and forwarding is how it spreads.
- **Deep links in every post**, straight to the upload screen, pre-filled with the country.
- **Instagram / TikTok:** short videos of the same basket bought in Amsterdam vs. Tel Aviv, and duets or stitches of users opening their own results.

---

## 5. Creating buzz and a lasting effect

1. **Mobilize Israelis living abroad.** Hundreds of thousands of Israelis live in Europe, and every one of them has had "the supermarket shock". Seed the project in expat groups in Berlin, Amsterdam, London, Lisbon, Athens and Cyprus.
2. **Focus beats spread.** The 2011 cottage-cheese boycott worked because it targeted *one* product. Run one-product campaigns with a clear ask and a clear target.
3. **Timing.** Launch campaigns before holiday shopping peaks (Pesach, Rosh Hashana) and during election campaigns. Ask candidates to sign a specific, measurable pledge. Stay strictly **non-partisan**.
4. **Accountability dossiers.** Send quarterly data packs to the Knesset Economic Committee, the Competition Authority, the Consumer Council and journalists at TheMarker, Calcalist, Globes and Ynet.
5. **Name the lever, not just the pain.** Each campaign ends with a concrete ask, e.g. "cut tariff X", "open parallel import in category Y", "enforce reform phase Z".
6. **Leaderboards.** "Most expensive basket gap of the week", and rankings by city and country.

---

## 6. Legal & trust guardrails

- **Defamation (Israeli law):** Publish verifiable facts and sourced prices. Don't make claims about intent ("cartel", "robbery") unless an authority has found it.
- **Privacy (GDPR / Israeli Privacy Protection Law):** Scrub receipts of personal details, delete images after processing, make data sharing opt-in, and provide a privacy policy.
- **Data licenses / scraping terms of service:** Honor them. Prefer official and open data.
- **AI accuracy:** Show match confidence, let users correct matches, and never present an AI guess as a verified price.
- **Transparency:** Disclose AI use on social accounts. Publish the methodology and a changelog of data corrections.

---

## 7. MVP roadmap

| Phase | Scope | Goal |
|---|---|---|
| **0: Landing (≈2 wks)** | Static site: 30-product IL vs. NL/DE/FR comparison, "minutes of work" lens, factor panel, sources | Credible, shareable proof |
| **1: Receipt Shock (≈4 wks)** | Upload → Claude vision → matching against IL price-transparency data → share card | The viral loop |
| **2: Bots (≈3 wks)** | WhatsApp + Telegram receipt bots, auto-generated social cards | Distribution |
| **3: Accountability** | Reform tracker, open API, journalist kit, quarterly dossiers | Lasting effect |

**Suggested stack:** Next.js (Vercel) front end · Postgres (Supabase / Neon) · Python worker for Israeli XML ingestion (reuse the open-source scrapers) · Claude API for receipt extraction, translation and product matching · ECB rates API.

---

## 8. Decisions

- **Name:** YakarPo (יקר פה).
- **Language:** Hebrew only (RTL). The audience is Israelis, in Israel and abroad.
- **Comparison countries:** all of Europe, not a short list. Every receipt is compared from the country it came from.
- **Repository:** moving to a dedicated `YakarPo` repo. This folder is self-contained so it can be moved as is.

## 9. First receipt (21-09-2026, Lidl Harderwijk, NL)

- Data: `data/receipts/2026-09-21-lidl-harderwijk.json` (personal and card details removed).
- Page: `web/receipt-2026-09-21-lidl-harderwijk.html`, built with `python3 tools/render_receipt.py <json> <out.html>`.
- Result: 27 of the 40 product lines matched (€113.82). In Israel the same items cost **+23%** at the cheapest prices found and **+58%** at typical shelf prices. Dairy and eggs are the biggest gap, at **+93%**. Israel is cheaper for several vegetables and for bottled water.
- Israeli prices were collected by hand from price-comparison sites through web search. This sandbox cannot reach Israeli retailer sites directly, so the next step is ingesting the official price-transparency files.

## 10. Open questions

- Budget for LLM calls and the WhatsApp Business API.
- Solo project or collaborators, and who approves content before it's published?
