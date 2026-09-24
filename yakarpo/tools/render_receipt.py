"""Render a receipt comparison page from a receipt JSON file.

Usage: python3 tools/render_receipt.py data/receipts/<id>.json out.html
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def main(src, out):
    data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = (ROOT / "web" / "receipt-template.html").read_text(encoding="utf-8")
    pathlib.Path(out).write_text(template.replace("/*__DATA__*/", payload), encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:3])
