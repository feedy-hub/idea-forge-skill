#!/usr/bin/env python3
"""Reconstruct the packaged skill ZIP from base64 split parts."""
from pathlib import Path
import base64
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "packages"
MANIFEST = PKG / "SHA256SUMS.md"

text = MANIFEST.read_text(encoding="utf-8")
filename = re.search(r"^filename:\s*(.+)$", text, re.M).group(1).strip()
expected_sha = re.search(r"^sha256:\s*([0-9a-f]+)$", text, re.M).group(1).strip()

parts = sorted(PKG.glob("package.part-*.b64"))
if not parts:
    raise SystemExit("No package.part-*.b64 files found under packages/.")

b64 = "".join(p.read_text(encoding="ascii").strip() for p in parts)
data = base64.b64decode(b64)
actual_sha = hashlib.sha256(data).hexdigest()
if actual_sha != expected_sha:
    raise SystemExit(f"SHA256 mismatch: expected {expected_sha}, got {actual_sha}")

out = ROOT / filename
out.write_bytes(data)
print(f"wrote {out} ({len(data)} bytes)")
print(f"sha256 {actual_sha}")
