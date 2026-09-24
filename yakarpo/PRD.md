# YakarPo (יקר פה): Product Requirements Document

| | |
|---|---|
| **Product** | YakarPo (יקר פה): the price gap between Israel and Europe, receipt by receipt |
| **Status** | Draft v1.0, 24 September 2026 |
| **Owner** | Founder (idluxman) |
| **UI language** | Hebrew only (RTL). Receipts can be in any European language. |
| **Scope** | Israel compared with every European country |

---

## 1. Summary

Israelis pay far more for everyday groceries than Europeans. Israel's State Comptroller puts food prices about **51% above the EU**, and OECD data ranks Israel's food prices second highest in the OECD. Most Israelis know prices are high but have no concrete, personal proof, and no clear picture of *why*.

YakarPo turns any European supermarket receipt into a line-by-line answer to "what would this cost in Israel?" The answer is backed by Israel's official price-transparency data. The platform then explains the causes (taxes, tariffs, import rules, market concentration) and puts the anger that follows behind specific, winnable policy demands.

**The rule for everything we build:** the voice can be angry, but the numbers can't be wrong. Credibility is the product. One sloppy number, screenshotted by an importer's PR team, costs more than a hundred good ones earn.

---

## 2. Problem

1. **The gap is abstract.** "Food is 51% more expensive" is a headline people forget. "My €114 Lidl basket would cost ₪622 in Israel" is personal and easy to share.
2. **The debate lacks facts.** Retailers blame suppliers, suppliers blame regulation, politicians blame everyone. No public tool shows the gap per product along with its causes.
3. **Israelis abroad see it every day, and that experience goes nowhere.** Hundreds of thousands of Israelis live in or travel to Europe. Their shock in the supermarket is powerful evidence that currently ends up in WhatsApp rants.
4. **Reforms go unmeasured.** Reforms like "What's good for Europe is good for Israel" (phased in 2025–2028) promise lower prices, and no one is tracking at product level whether prices actually fall.

---

## 3. Goals and non-goals

### Goals
- **G1. Proof:** Produce credible, sourced, per-product comparisons between Israel and any European country.
- **G2. Participation:** Make it effortless for anyone to add evidence by uploading a receipt from the web, WhatsApp or Telegram.
- **G3. Understanding:** Explain the gap with objective factors, and state for each one whether policy can fix it.
- **G4. Spread:** Every result should be designed to be shared, and our social channels should consistently bring people back to upload.
- **G5. Impact:** Turn the data into specific demands aimed at specific decision-makers, and track whether anything changes.

### Non-goals
- A shopping or coupon app for Israelis. We may show where it's cheapest in Israel, but that isn't the point.
- Partisan politics. We never endorse a party or candidate.
- Fake grassroots activity. No AI personas posing as real people.
- Non-food categories in v1 (electronics, cars, housing). We may add them later.
- Any UI language other than Hebrew.

---

## 4. Users

| Persona | Who | What they want | What they do |
|---|---|---|---|
| **The expat** (primary) | Israeli living in or visiting Europe, like the founder in the Netherlands | Proof that they're not imagining it, and to show friends back home | Uploads receipts and shares result cards |
| **The Israeli at home** | Pays the high prices and is angry but vague about why | To see the gap on products they buy, and to understand why | Reads, shares, joins campaigns |
| **The journalist or researcher** | Economics desks at TheMarker, Calcalist, Globes, Ynet; academics | Clean, citable data and method | Uses datasets, the API and dossiers |
| **The policy staffer** | Knesset Economic Committee, Competition Authority, Consumer Council | Product-level evidence tied to specific policy levers | Reads dossiers and the reform tracker |
| **The editor** (internal) | Founder or a volunteer moderator | To publish quickly without mistakes | Approves AI-drafted posts, reviews flagged matches |

---

## 5. Product principles

1. **Conservative by default.** When uncertain, assume the option that makes Israel look *cheaper*. Always show both the cheapest Israeli price and the typical one.
2. **Show every assumption.** Every line shows its source, the date, the matched product, any size assumption, and a confidence level.
3. **Show where Israel wins too.** When Israel is cheaper (for example many vegetables and bottled water), say so prominently. Honesty about this is what makes the rest believable.
4. **Explained, not excused.** For each cause of the gap, show how much it explains and whether it could be fixed by policy.
5. **Keep personal data to a minimum.** Receipts carry card digits and transaction IDs. We never store them.
6. **Disclose AI.** Our AI-assisted content is labeled and published only from official accounts.
7. **Hebrew first.** RTL is designed in from the start, not added afterwards. Numbers and currencies stay readable inside Hebrew text.

---

## 6. Success metrics

| Metric | Definition | 6-month target |
|---|---|---|
| **North star: verified receipts / week** | Receipts processed with at least 60% of lines matched | 1,000 / week |
| Share rate | Share-card taps ÷ results viewed | ≥ 25% |
| Viral coefficient | New uploaders who came from a share ÷ uploaders | ≥ 0.4 |
| Match quality | Lines corrected by users ÷ lines shown | ≤ 5% |
| Coverage | Receipt lines matched to an Israeli product | ≥ 70% |
| Time to result | Upload → result page (p50 / p95) | ≤ 30s / ≤ 60s |
| Countries covered | European countries with at least 20 receipts | ≥ 15 |
| Media and policy | Media citations; mentions in the Knesset or by regulators | 20 citations; 1 formal mention |
| Cost per receipt | AI plus infrastructure cost for each processed receipt | ≤ $0.25 |

---

## 7. Scope by release

| Release | Contents | Target |
|---|---|---|
| **M0: Foundations** | Ingest Israeli price-transparency data, build the product catalogue, process receipts by hand, launch a landing page with receipt #1 and a curated basket of exact matches | Weeks 1–3 |
| **M1: Receipt Shock MVP** | Web upload, AI extraction, matching, result page, share card, corrections | Weeks 4–8 |
| **M2: Distribution** | WhatsApp and Telegram bots, social content engine, dynamic share images, deep links | Weeks 9–12 |
| **M3: Depth** | Fair-comparison lenses, factor panel, Wall of Shame, country pages | Weeks 13–18 |
| **M4: Accountability** | Reform tracker, open data and API, journalist kit, campaigns, dossiers | Weeks 19+ |

---

## 8. Functional requirements

Priority: **P0** is required for its release, **P1** should ship, **P2** is nice to have.

### F1. Receipt upload (web): M1
**User story:** As an expat, I photograph my receipt and within a minute see what it would cost in Israel.

| ID | Requirement | Priority |
|---|---|---|
| FR-1.1 | Upload by file picker or drag-and-drop. JPG, PNG, HEIC and PDF; up to 3 images per receipt, for long receipts. | P0 |
| FR-1.2 | No account needed to upload or see a result. | P0 |
| FR-1.3 | A progress screen with real steps: reading the receipt → identifying products → comparing with Israel. | P0 |
| FR-1.4 | Reject images that aren't receipts, with a clear Hebrew message ("זו לא נראית כמו קבלה. נסו לצלם שוב, ישר ובתאורה טובה"). | P0 |
| FR-1.5 | Consent checkbox, on by default and explained: "תרמו את המחירים (ללא פרטים אישיים) למאגר הפתוח". | P0 |
| FR-1.6 | Detect duplicate receipts (same store, date, total and time) and warn. | P1 |
| FR-1.7 | Optional product photos (for example the Philadelphia tub) to raise match confidence through the barcode or the label. | P2 |

**Acceptance:** Receipt #1 (Lidl Harderwijk, 52 items) produces at least 25 matched lines, a total within ±5% of the hand-built baseline in Appendix A, and a p95 time under 60 seconds.

### F2. Receipt extraction (AI): M1
| ID | Requirement | Priority |
|---|---|---|
| FR-2.1 | Extract store, chain, city, country, date, time, currency, total, VAT breakdown and line items into a strict JSON schema (§11.2). | P0 |
| FR-2.2 | Handle retailer quirks: discount lines ("Goedkoper", "In prijs verlaagd", "Korting", "Rabatt", "Remise"), multi-buy lines ("2 x 1,10"), weighed items ("1,210 kg x 3,49"), deposits (statiegeld, Pfand, consigne) and VAT codes (A/B/C → rate). | P0 |
| FR-2.3 | Apply each discount to the line above it. The paid price is what gets compared. | P0 |
| FR-2.4 | Drop personal data at extraction time: card number, terminal, merchant and transaction IDs, AID, loyalty IDs, names. It never reaches storage. | P0 |
| FR-2.5 | Check the math: the sum of lines must equal the receipt total within €0.05. If not, show a warning and a manual edit mode. | P0 |
| FR-2.6 | Expand abbreviated product names ("Philadelphia origin." → Philadelphia Original) using the retailer's catalogue when one is available. | P1 |

### F3. Product matching and pricing: M1
The core engine. The algorithm is in §11.3.

| ID | Requirement | Priority |
|---|---|---|
| FR-3.1 | Resolve the pack size for each line: from the receipt, then the retailer's catalogue, then Open Food Facts, then a category default. Record which source was used. | P0 |
| FR-3.2 | Match to an Israeli product using three tiers: **exact** (same brand, variant and size), **equivalent** (same category and spec) and **cheapest alternative**. | P0 |
| FR-3.3 | Give each match a confidence level (high, medium or low) with a one-line Hebrew explanation. | P0 |
| FR-3.4 | Israeli price: **low** is the minimum across chains in the last 7 days, promotions included. **Typical** is the median regular (non-promo) price at the 5 largest chains. Both are scaled to the Dutch pack size. | P0 |
| FR-3.5 | Currency conversion uses the ECB reference rate on the receipt date. The rate is shown on the result. | P0 |
| FR-3.6 | Exclude with a stated reason: deposits, non-food, unidentified items, and items with no Israeli equivalent (e.g. kruidnoten). | P0 |
| FR-3.7 | When uncertain, choose the assumption that lowers the Israeli price (principle 1). Tests must enforce this. | P0 |
| FR-3.8 | Every matched line keeps a reference to the exact Israeli price rows used, so it can be audited. | P0 |

### F4. Result page and share card: M1
Reference implementation: `web/receipt-template.html`.

| ID | Requirement | Priority |
|---|---|---|
| FR-4.1 | Headline: "אותה עגלה. +X% בישראל." with totals for the Dutch paid price, the cheapest Israeli price and the typical Israeli price. | P0 |
| FR-4.2 | Gap by category (diverging bars, so categories where Israel is cheaper are visible). | P0 |
| FR-4.3 | Line-by-line list: the name as printed on the receipt, the Hebrew name, the Israeli match, the size assumption, both Israeli prices, the gap and a confidence chip. | P0 |
| FR-4.4 | Filter "only reliable matches" (high and medium confidence). The totals recalculate. | P0 |
| FR-4.5 | A section of excluded lines, each with its reason and amount. | P0 |
| FR-4.6 | Share card: a 1080×1350 image and a 1200×630 link preview with the headline number, the country flag and the 3 biggest gaps. A permanent public URL per receipt. | P0 |
| FR-4.7 | "Something's wrong?" on each line opens the correction flow (F5). | P0 |
| FR-4.8 | Minutes-of-work view (F7). | P1 |
| FR-4.9 | A call to action at the bottom: upload another receipt, join the campaign, follow the channel. | P1 |

### F5. Corrections and moderation: M1
| ID | Requirement | Priority |
|---|---|---|
| FR-5.1 | Users can fix a line's size, the Israeli match (from a search list) or flag the line as wrong. | P0 |
| FR-5.2 | A correction applies to that receipt at once and goes into a moderation queue before it affects the shared catalogue. | P0 |
| FR-5.3 | An editor console lists flagged lines, low-confidence matches with high traffic, and posts waiting for approval. | P0 |
| FR-5.4 | A public corrections log (what changed and why). | P1 |

### F6. WhatsApp and Telegram bots: M2
**User story:** I forward a photo of my receipt to the YakarPo number and get the result card back in the same chat.

| ID | Requirement | Priority |
|---|---|---|
| FR-6.1 | WhatsApp Business (Cloud API) number and a Telegram bot. Both accept one or more receipt photos. | P0 |
| FR-6.2 | Reply with the share-card image plus a short Hebrew summary and a link to the full result. | P0 |
| FR-6.3 | Ask 1–2 quick questions when the confidence is too low ("כמה ביצים היו באריזה? 6 / 10 / 12 / 15"). | P1 |
| FR-6.4 | Opt-in weekly digest ("יקר השבוע"). | P1 |
| FR-6.5 | Official YakarPo channels on WhatsApp and Telegram for one-way updates. | P0 |

### F7. Fair-comparison lenses: M3
| ID | Requirement | Priority |
|---|---|---|
| FR-7.1 | **Nominal** (default): converted at the exchange rate. | P0 |
| FR-7.2 | **Minutes of work**: basket cost ÷ net hourly wage, at the median wage and at the minimum wage, for each country. | P0 |
| FR-7.3 | **Without VAT**: removes VAT from both sides (Israel 18%, with fresh fruit and vegetables exempt; each EU country at its food rate). This separates tax from pricing. | P1 |
| FR-7.4 | **PPP-adjusted**, for economists. | P2 |
| FR-7.5 | Every lens shows its formula and data source when tapped. | P0 |

### F8. Factor panel, "explained, not excused": M3
For each factor: a one-line explanation, which direction it pushes prices, an estimated share of the gap (where evidence exists), whether policy can fix it, and sources.

Factors in v1: VAT on food; retail concentration (share of the top 3 chains); supplier and importer concentration; import tariffs and quotas (dairy, eggs, meat); import standards and the status of the reform; exclusive importers and barriers to parallel import; kashrut costs; small market and no land trade with neighbors; exchange rate; security and wartime costs; context indicators (median wage, minimum wage, rent as a share of income, income tax).

| ID | Requirement | Priority |
|---|---|---|
| FR-8.1 | A factor page per factor, with sources and a "last reviewed" date. | P0 |
| FR-8.2 | Link factors to products (e.g. the Greek yogurt line → dairy quotas and tariffs). | P1 |
| FR-8.3 | Myth-busting cards ("זה בגלל הכשרות?") with a sourced answer. | P1 |

### F9. Wall of Shame and product pages: M3
| ID | Requirement | Priority |
|---|---|---|
| FR-9.1 | A page per product: the Israeli price over time compared with European countries (from receipts plus open data). | P0 |
| FR-9.2 | A leaderboard of the biggest gaps for identical products (exact tier only). | P0 |
| FR-9.3 | Name the Israeli importer or manufacturer, as a verifiable fact only. The wording must pass legal review (§13). | P1 |
| FR-9.4 | Country pages ("ישראל מול יוון") with basket comparisons. | P1 |

### F10. Reform tracker: M4
| ID | Requirement | Priority |
|---|---|---|
| FR-10.1 | List each reform milestone (e.g. each phase of "What's good for Europe is good for Israel"), its effective date and the product categories it affects. | P0 |
| FR-10.2 | Price before and after for the affected products, with a clear verdict: prices fell, didn't change, or rose. | P0 |
| FR-10.3 | Alerts to followers when a milestone passes with no price change. | P1 |

### F11. Open data and journalist kit: M4
| ID | Requirement | Priority |
|---|---|---|
| FR-11.1 | Anonymized CSV and JSON downloads (receipt lines, matches, prices), under an open license such as CC BY 4.0. | P0 |
| FR-11.2 | A read-only public API with rate limits. | P1 |
| FR-11.3 | A methodology page with version history. | P0 |
| FR-11.4 | A press kit: key charts, citation text, contact. | P1 |

### F12. Campaigns: M4
| ID | Requirement | Priority |
|---|---|---|
| FR-12.1 | A campaign page: one product or category, one demand, one target (e.g. "cancel the tariff on X, addressed to the Minister of Economy"). | P0 |
| FR-12.2 | A public sign-up counter; supporters add receipts as evidence. | P0 |
| FR-12.3 | A pledge tracker for candidates and ministers (non-partisan, the same demand to everyone). | P1 |
| FR-12.4 | An auto-generated quarterly dossier (PDF plus web) for the Knesset Economic Committee, the Competition Authority and the Consumer Council. | P1 |

### F13. Social content engine: M2
| ID | Requirement | Priority |
|---|---|---|
| FR-13.1 | Official accounts on Instagram, TikTok, Facebook, X, Telegram and WhatsApp channels, all openly run by YakarPo. **No personas.** | P0 |
| FR-13.2 | Claude drafts posts from live data in fixed formats: Receipt of the day (with the user's consent), Product of the week, Minutes of work, Israel wins (where Israel is cheaper), Reform watch, Myth-busting. | P0 |
| FR-13.3 | Every draft cites the dataset rows behind it. An editor approves it before it's published. After 4 weeks without corrections, a template can be set to publish automatically. | P0 |
| FR-13.4 | Every post has a link or button that goes straight to the upload screen or the bot, with UTM tracking. | P0 |
| FR-13.5 | An "AI-assisted content" label as each platform requires. | P0 |
| FR-13.6 | A wording linter blocks words that imply wrongdoing without a ruling ("קרטל", "גנבים", "הונאה") and unsourced numbers. | P0 |

---

## 9. Non-functional requirements

| Area | Requirement |
|---|---|
| **Language and RTL** | Hebrew only in the UI. Correct bidirectional text: numbers, ₪ and € amounts and percentages are isolated, so "+58%" never shows as "58%+". |
| **Accessibility** | WCAG 2.2 AA. Color is never the only signal (gaps have a sign and a label). Charts have a table view. Keyboard and screen reader support. |
| **Performance** | Result page LCP under 2.5s on a 4G phone. Share images render within 3s. |
| **Availability** | 99.5% monthly for upload and results. Bots queue messages during outages and reply later. |
| **Scale** | 10,000 receipts a day by M2 without redesign. |
| **Security** | OWASP ASVS L1. Uploads scanned by type and size, with EXIF data removed. Secrets managed by the platform. Rate limits per IP and per phone number. |
| **Data freshness** | Israeli prices: full refresh daily, updates at least every 6 hours. Exchange rates: daily. Indicators: quarterly review. |
| **Auditability** | Every published number can be traced to source rows. The methodology is versioned, and each result is tied to a methodology version. |
| **Cost** | ≤ $0.25 per processed receipt at the 95th percentile. |

---

## 10. Data sources

### Israel
| Source | What | Notes |
|---|---|---|
| **Price transparency law (Food Act, 2014)** | Full price, promotion and store files from every chain with 3+ stores, published several times a day as XML (usually gzipped) on about 30 chain portals | The primary source. Reuse open-source scrapers (e.g. OpenIsraeliSupermarkets, `israeli-prices` on PyPI). Some portals need logins or block foreign IPs, so ingestion may need an Israeli-region host. |
| CBS (Central Bureau of Statistics) | CPI, wages, rent | Indicators |
| State Comptroller, Competition Authority, Knesset Research Center | Reports and findings | Factor panel |
| Price-comparison sites (Pricez, CHP) | Checking and backfill only | Check terms of use; never the primary source |

### Europe
| Source | What | Notes |
|---|---|---|
| **Receipts** (ours) | Prices actually paid, by country, chain and date | Our main European data, grows with use |
| Open Food Facts / Open Prices | Barcodes, product sizes, crowdsourced prices (open license) | Size lookup and extra prices; we contribute back |
| Retailer online catalogues (Albert Heijn, Jumbo, Lidl, Aldi, Carrefour, Mercadona, Rewe, Tesco…) | Full product names and pack sizes | Terms of service and legal review per retailer. Used for resolving sizes, not bulk price scraping. |
| Eurostat, OECD | Comparative price levels, HICP, wages, minimum wages, tax wedge | Lenses and context |
| ECB | Daily reference exchange rates | Currency conversion |

---

## 11. System design

### 11.1 Architecture
```
Web (Next.js, Hebrew RTL, Vercel) ─┐
WhatsApp Cloud API webhook ────────┼─> API / job queue ─> Receipt pipeline
Telegram Bot API webhook ──────────┘                       │ 1. Extract (Claude, vision)
                                                          │ 2. Resolve sizes (catalogues, Open Food Facts)
                                                          │ 3. Find Israeli candidates (Postgres trigram and full-text)
                                                          │ 4. Choose match (Claude, structured output)
                                                          │ 5. Price and convert
                                                          v
                     Postgres (Supabase or Neon): catalogue, prices, receipts, matches
                                                          ^
IL ingestion workers (Python, scheduled, Israeli region) ─┘
Content engine (scheduled): drafts → editor console → platform APIs
Object storage: receipt images, deleted after 24 hours unless donated
```

### 11.2 Receipt extraction schema (abridged)
```json
{
  "store": {"chain": "Lidl", "city": "Harderwijk", "country": "NL"},
  "date": "2026-09-21", "currency": "EUR", "total": 139.39,
  "vat": [{"code": "B", "rate": 9, "gross": 122.92}],
  "lines": [{
    "raw": "Griekse yoghurt 4x15", "qty": 1, "unit_price": 2.19,
    "discount": -0.20, "paid": 1.99, "vat_code": "B",
    "weight_kg": null, "kind": "product | deposit | non_food"
  }]
}
```
Personal fields aren't in the schema, so they can't be stored even by mistake.

### 11.3 Matching algorithm
1. **Normalize** (Claude): brand, product type, variant, fat or flavor, size if printed, category, language.
2. **Resolve size:** receipt, then the retailer catalogue (by line text), then Open Food Facts, then the category default. Store `size_source`.
3. **Find candidates:** barcode (if a product photo was added), otherwise brand + name trigram + category over the Israeli catalogue, top 20.
4. **Choose** (Claude, structured output): pick the best candidate, the tier (exact, equivalent or alternative), the confidence, and a Hebrew reason. The prompt includes principle 1 (the conservative bias).
5. **Price:** low and typical per FR-3.4, scaled by size ratio.
6. **Store** the match with references to the source price rows and the methodology version.

### 11.4 AI models and cost
- Model: **Claude Opus 5** (`claude-opus-5`), with adaptive thinking, for extraction and matching. Use structured outputs (`output_config.format`) for the JSON. Enable server-side refusal fallbacks.
- A cheaper model (`claude-sonnet-5`) is worth testing on extraction once there's an evaluation set. Switch only if quality holds; the founder decides.
- Rough cost per receipt: about 5k input and 3k output tokens for extraction, and a similar amount for matching. At $5 / $25 per million tokens that's about **$0.10–0.20 per receipt**. Prompt caching of the fixed instructions lowers it further.
- Build an evaluation set from the first 50 hand-checked receipts before switching models or prompts.

### 11.5 Data model (core tables)
`country`, `chain`, `store`, `product` (canonical), `listing` (a product at a chain, with barcode, name, size and unit), `price_point` (listing, store, price, is_promo, observed_at, source), `fx_rate`, `receipt`, `receipt_line`, `match` (line → listing, tier, confidence, size_assumption, size_source, price_refs, methodology_version), `correction`, `indicator` (country, metric, value, period, source), `factor`, `reform_milestone`, `campaign`, `content_post` (draft, approved or published, with citations).

---

## 12. Privacy and security

- **What we never store:** card numbers (even partial), terminal, merchant and transaction IDs, AID, loyalty IDs, customer names, exact store address (we keep the city), faces or anything else in the photo that isn't the receipt.
- **Images:** processed and then deleted within 24 hours. If the user chose to donate, the image is cropped to the receipt and personal fields are blacked out before it's kept.
- **Phone numbers (bots):** stored as a salted hash for rate limiting only. Never shown or shared.
- **Law:** GDPR (EU users; legal basis is consent; a data protection impact assessment before M1; a data processing agreement with every processor, including the AI provider). Israel's Privacy Protection Law and its current amendments. A plain-Hebrew privacy page.
- **Access:** editors need two-factor login. Admin actions are logged.

---

## 13. Legal and trust guardrails

| Risk | Guardrail |
|---|---|
| Defamation (Israeli law) | Only verifiable facts with sources. The wording linter (FR-13.6). Legal review before any campaign that names a company. A fast corrections process. |
| Retailer terms of service and scraping | Official transparency data for Israel. Receipts and open data for Europe. Catalogue lookups only after legal sign-off. |
| Platform rules on fake accounts | Official accounts only, AI use disclosed, no fake engagement, no personas. |
| AI errors | Confidence chips, conservative bias, user corrections, an evaluation set, editor approval for published content. |
| Being framed as partisan or foreign-run | Transparent "about" page, founder named, funding disclosed, same demand to every party. |
| Trademarks | Brand names used only to identify products (nominative use), with no logos. |

---

## 14. Go-to-market

1. **Seed (M0–M1):** the founder's receipts plus 20–30 friends in the Netherlands, Germany, Greece, Cyprus and Portugal. Launch posts in Israeli expat groups (Facebook, WhatsApp, Telegram) with real result cards.
2. **Receipt challenge (M2):** "העלו קבלה מחו״ל" with a weekly leaderboard of the biggest gap and the most countries covered.
3. **Press (M2–M3):** exclusive data stories for one economics desk per month. Every story links to a result page.
4. **One product at a time (M4):** follow the 2011 cottage-cheese protest, which worked because it was about one product. One product, one demand, one target, plus a counter and receipts as evidence.
5. **Timing:** holiday shopping peaks (Pesach, Rosh Hashana), budget debates, election periods (strictly non-partisan).

---

## 15. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| A viral wrong number | Medium | High | Conservative bias, confidence filter, editor approval, public corrections log |
| Israeli portals block ingestion from abroad | Medium | High | Host ingestion in Israel; fall back to the open-source community mirrors |
| Low upload volume | Medium | High | Bots with one-tap forwarding, the challenge, expat seeding |
| AI cost grows faster than usage | Low | Medium | Prompt caching, an evaluation set before any model change, limits per user |
| Legal threats from importers or retailers | Medium | Medium | Facts-only wording, legal review, insurance, a lawyer lined up before M4 |
| The strong shekel inflates the gap | High | Low | Show the exchange rate, the VAT-free lens and the minutes-of-work lens, and explain the effect |
| Burnout (solo founder) | Medium | High | Volunteer editors, automation after templates are trusted, a narrow scope per release |

---

## 16. Open questions

1. Budget: AI calls, the WhatsApp Business API, hosting, legal review.
2. Team: will there be volunteer editors or co-founders? Who approves content?
3. Legal structure: a nonprofit (עמותה), an informal project, or a company? This affects donations, liability and credibility.
4. Should the cheapest Israeli price include club-card-only promotions?
5. Should the Israeli side be split by region (Eilat has no VAT)?
6. Should we publish donated receipt images, or only the extracted lines?

---

## Appendix A: Receipt #1 (baseline)

**Lidl, Harderwijk, NL · 21-09-2026 · 52 items · €139.39**

- 27 of 40 product lines matched (€113.82, about ₪395 at 3.47). 13 excluded (€25.57): deposit, non-food, Dutch products with no Israeli equivalent, unidentified items.
- Israel: **₪486 at the cheapest prices found (+23%)**, **₪622 at typical shelf prices (+58%)**.
- Reliable matches only (15 lines): +21% at the cheapest prices, +64% at typical prices.
- By category (typical): dairy and eggs **+93%**, deli +52%, produce +35%, meat and fish +35%, pantry +32%, sweets +25%, alcohol +160%.
- Israel is cheaper for cucumbers, peppers, cherry tomatoes and bottled water.
- Files: `data/receipts/2026-09-21-lidl-harderwijk.json`, `web/receipt-2026-09-21-lidl-harderwijk.html`.

**What it taught us:**
1. Receipts don't print pack sizes, so size resolution (FR-3.1) is essential.
2. Product names are cut short ("Philadelphia origin.", "Kipfiletblokjes BL"), so catalogue expansion is needed (FR-2.6).
3. Discount lines follow the item they apply to and must be attached to it (FR-2.3).
4. Deposits and VAT codes are printed on their own lines and must be classified (FR-2.2).
5. The payment block holds personal data (card digits, terminal, AID) and must be dropped (FR-2.4).
6. National specialties (kruidnoten, chocolate letters) need an explicit "no equivalent" rule.
7. Prices gathered by hand from comparison sites are too slow and too uncertain for production, so official data ingestion comes first (M0).

## Appendix B: Hebrew UI copy (core strings)

| Key | Hebrew |
|---|---|
| Hero CTA | העלו קבלה מחו״ל וגלו כמה היא עולה בישראל |
| Upload button | העלאת קבלה |
| Progress | קוראים את הקבלה… · מזהים מוצרים… · משווים לישראל… |
| Result headline | אותה עגלה. ‎+X%‎ בישראל. |
| Low / typical | הכי זול שמצאנו / מחיר מדף רגיל |
| Confidence | אמינות גבוהה / אמינות בינונית / הערכה |
| Israel cheaper | כאן ישראל זולה יותר |
| Excluded | לא נכלל בהשוואה |
| Correction | משהו לא נכון? תקנו אותנו |
| Share | שתפו את הקבלה |
| AI label | תוכן בסיוע AI · הנתונים והמקורות בקישור |

## Appendix C: Glossary

- **Price transparency files:** the price files Israeli chains must publish by law under the 2014 Food Act.
- **Exact / equivalent / alternative:** the three match tiers (FR-3.2).
- **Low / typical:** the two Israeli prices shown for every line (FR-3.4).
- **Methodology version:** the version of the calculation rules each published result was computed with.
