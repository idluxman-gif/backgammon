# YakarPo (יקר פה)

Compares the price of a European supermarket receipt with what the same items cost in Israel.

- `PRD.md`: product requirements (start here)
- `PLAN.md`: background, strategy and first decisions
- `data/receipts/`: processed receipts (personal details removed)
- `web/receipt-template.html`: Hebrew result page template
- `tools/render_receipt.py`: builds a result page from a receipt file

```
python3 tools/render_receipt.py data/receipts/<id>.json web/<id>.html
```
