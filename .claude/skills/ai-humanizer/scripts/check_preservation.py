#!/usr/bin/env python3
"""Check that a humanized document kept every section and fact.

Usage:
  check_preservation.py BEFORE            # baseline: sections, facts, tell counts
  check_preservation.py BEFORE AFTER      # compare; exit 1 if a heading or ID is lost

Works on markdown or plain text. Headings are markdown '#' lines, or numbered
lines like '1.2 Title' in extracted text.
"""
import re, sys
from collections import Counter

TELLS = {
    "not X but Y": r"\bnot (?:just|only|merely|simply)\b|\bisn'?t\b[^.]{0,60}\bit'?s\b|\brather than\b",
    "signposting": r"\b(?:it is worth noting|importantly|crucially|notably|in other words|put simply|let us (?:now )?(?:turn|look)|it should be noted|needless to say)\b",
    "AI words": r"\b(?:additionally|align(?:s|ed)? with|bolster\w*|crucial|delve\w*|deep dive|enhanc\w+|foster\w*|garner\w*|highlight(?:s|ed|ing)?|holistic|interplay|intricate\w*|landscape|meticulous\w*|navigat\w+|nuanced|pivotal|robust|seamless\w*|showcas\w+|streamlin\w+|tapestry|testament|underscor\w+|vital|vibrant|comprehensive|multifaceted|paramount|synergy|empower\w*|unlock\w*|realm|ever-evolving|key (?:insight|takeaway|factor|role|driver))\b",
    "is-avoidance": r"\b(?:serves as|stands as|functions as|acts as a|boasts)\b",
    "-ing rider": r",\s+(?:highlighting|underscoring|emphasizing|ensuring|reflecting|fostering|showcasing|contributing to|signalling|signaling)\b",
    "summary filler": r"\b(?:in summary|in conclusion|overall,|to sum up|in short,|ultimately,)\b",
    "self-reference": r"\b(?:this (?:section|document|report|chapter) (?:explains|describes|shows|sets out|presents|covers)|the table below|as (?:discussed|noted|shown) (?:above|earlier))\b",
    "dash": r"[—–]| -- ",
}
ID_RE = r"\b(?:LP|IP|P|L|RC|SC|CM|K|G|O|DP|D|S)\d+[a-z]?\b|\b(?:Table|Figure|Chain|Stage|Scenario|Concept|Prototype|Deliverable|Activity|Phase|Place) \d+\b"
NUM_RE = r"(?:₹\s?)?\d[\d,]*(?:\.\d+)?\s?(?:%|percent|lakh|crore|kg|g\b|am|pm|minutes?|hours?|days?|weeks?)?"
LABELS = r"\b(?:confirmed|single-sourced|candidate|assumed|projected|simulated|planned)\b"


def load(path):
    t = open(path, encoding="utf-8").read()
    return t


def headings(t):
    hs = []
    for line in t.splitlines():
        s = line.strip()
        m = re.match(r"^(#{1,6})\s+(.*)", s)
        if m:
            hs.append(m.group(2).strip())
            continue
        m = re.match(r"^(\d+(?:\.\d+){0,3})\s+([A-Z].{2,90})$", s)
        if m and not s.endswith("."):
            hs.append(s)
    return hs


def facts(t):
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    nums = Counter(re.sub(r"\s+", " ", n.strip()) for n in re.findall(NUM_RE, body) if re.search(r"\d", n))
    ids = Counter(re.findall(ID_RE, body))
    labels = Counter(x.lower() for x in re.findall(LABELS, body, re.I))
    return nums, ids, labels


def tells(t):
    return {k: len(re.findall(v, t, re.I)) for k, v in TELLS.items()}


def words(t):
    return len(re.findall(r"\b\w[\w'-]*\b", t))


def report(path):
    t = load(path)
    hs = headings(t)
    nums, ids, labels = facts(t)
    print(f"== {path}")
    print(f"words: {words(t)}  headings: {len(hs)}  distinct numbers: {len(nums)}  distinct IDs: {len(ids)}")
    print("tells:", tells(t))
    print("confidence labels:", dict(labels))
    return t, hs, nums, ids, labels


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    a = report(sys.argv[1])
    if len(sys.argv) < 3:
        for h in a[1]:
            print("  #", h)
        return
    b = report(sys.argv[2])
    ta, ha, na, ia, la = a
    tb, hb, nb, ib, lb = b
    norm = lambda h: re.sub(r"[^a-z0-9]+", " ", h.lower()).strip()
    missing_h = [h for h in ha if norm(h) not in {norm(x) for x in hb}]
    missing_ids = sorted(set(ia) - set(ib))
    missing_nums = sorted(set(na) - set(nb))
    new_nums = sorted(set(nb) - set(na))
    wa, wb = words(ta), words(tb)
    print("\n== comparison")
    print(f"words: {wa} -> {wb} ({(wb - wa) / max(wa, 1) * 100:+.1f}%)")
    print("missing headings:", missing_h or "none")
    print("missing IDs:", missing_ids or "none")
    print("numbers no longer present:", missing_nums or "none")
    print("numbers that are new (check none are invented):", new_nums or "none")
    for k in la:
        if lb.get(k, 0) < la[k]:
            print(f"confidence label '{k}': {la[k]} -> {lb.get(k, 0)} (check each dropped use was a duplicate)")
    ok = not missing_h and not missing_ids
    print("\nRESULT:", "PASS (headings and IDs intact; review numbers listed above)" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
