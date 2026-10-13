#!/usr/bin/env python3
"""Every heading of the original Phase 1 submission must survive, at the same level and in the same order.
New headings are allowed. Usage: check_headings.py"""
import json, re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(os.path.dirname(HERE), "Source")
sk = json.load(open(os.path.join(HERE, "skeleton_original.json")))
def norm(s):
    s = s.replace("—", ":").replace("–", "-").replace("’", "'").replace("‘", "'")
    s = re.sub(r"\s*:\s*", ": ", s)
    return re.sub(r"\s+", " ", s).strip().lower()
bad = 0
for name, orig in sk.items():
    path = os.path.join(SRC, name)
    new = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^(#{1,3}) (.*)", line.rstrip())
        if m: new.append((len(m.group(1)), norm(m.group(2))))
    i = 0; missing = []
    for lvl, h in orig:
        key = (lvl, norm(h))
        found = False
        while i < len(new):
            if new[i] == key: found = True; i += 1; break
            i += 1
        if not found:
            missing.append(h)
            i = 0  # restart scan so later headings are still checked fairly
    added = [h for l, h in new if (l, h) not in {(a, norm(b)) for a, b in orig} and l <= 2]
    print(f"{name}: original {len(orig)} headings, missing {len(missing)}, added {len(added)}")
    for m in missing: print("   MISSING:", m); bad += 1
    for a in added: print("   added:", a)
sys.exit(1 if bad else 0)
