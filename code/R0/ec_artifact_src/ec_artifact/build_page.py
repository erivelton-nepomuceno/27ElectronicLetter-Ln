#!/usr/bin/env python3
"""Build web/index.html (the "Efficient Chaos" interactive table) from the template and data."""
import json, pathlib
root = pathlib.Path(__file__).parent
t = (root / "web/template.html").read_text(encoding="utf-8")
rows = json.loads((root / "data/rows.json").read_text(encoding="utf-8"))
prof = json.loads((root / "data/profiles.json").read_text(encoding="utf-8"))
html = t.replace("__ROWS__", json.dumps(rows, ensure_ascii=False)).replace("__PROFILES__", json.dumps(prof, ensure_ascii=False))
(root / "web/index.html").write_text(html, encoding="utf-8")
print(f"web/index.html: {len(rows)} rows, {len(prof)} full profiles, {len(html):,} bytes")
