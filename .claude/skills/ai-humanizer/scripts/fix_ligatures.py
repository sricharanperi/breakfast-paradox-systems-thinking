#!/usr/bin/env python3
"""Repair ligatures (fi, fl, ff, ffi, ffl) dropped by PDF text extraction.

Usage: fix_ligatures.py IN OUT [EXTRA_VOCAB_FILE ...]

PDF text from Pages, Word or InDesign often loses ligature glyphs. Inside a word
the glyph becomes a space ("con rmed" for "confirmed"). At the start of a word it
vanishes ("rst" for "first", "ve" for "five"). This script repairs both against a
word list: /usr/share/dict/words, plus words that already appear intact in the
document, plus any EXTRA_VOCAB_FILE given (e.g. the document's markdown source).
It prints every repair it makes, so the result can be reviewed.
"""
import re, sys
from collections import Counter

LIGS = ["fi", "fl", "ff", "ffi", "ffl"]
SUFFIXES = ("s", "es", "ed", "d", "ing", "ly", "er", "ers", "ion", "ions", "ment", "ments", "al", "ally", "ity")


def build_vocab(text, extra_paths):
    vocab = set()
    try:
        with open("/usr/share/dict/words") as f:
            vocab |= {w.strip() for w in f if len(w.strip()) > 1 and w.strip().islower()}
    except OSError:
        pass
    for p in extra_paths:
        try:
            vocab |= {w.lower() for w in re.findall(r"[A-Za-z]+", open(p, encoding="utf-8").read())}
        except OSError:
            pass
    counts = Counter(w.lower() for w in re.findall(r"[A-Za-z]+", text))
    vocab |= {w for w, c in counts.items() if c >= 2 and len(w) > 3}
    vocab |= {"a", "i", "an", "as", "at", "be", "by", "do", "go", "he", "if", "in", "is", "it", "me", "my", "no", "of", "on", "or", "so", "to", "up", "us", "we"}
    return vocab


def known(w, vocab):
    b = w.lower()
    if b in vocab:
        return True
    return any(b.endswith(s) and len(b) - len(s) > 2 and b[: -len(s)] in vocab for s in SUFFIXES)


def fix(text, vocab):
    fixes = Counter()
    # Pass 1: gap inside a word. "con rmed" -> "confirmed", "de ne" -> "define".
    exact = lambda w: w.lower() in vocab
    def pair(m):
        a, b = m.group(1), m.group(2)
        # 1. the gap is inside one word: "con rmed" -> "confirmed"
        for lig in LIGS:
            if exact(a + lig + b):
                fixes[f"{a} {b} -> {a + lig + b}"] += 1
                return a + lig + b
        # 2. a real word, then a word that lost its leading ligature: "a xed" -> "a fixed"
        if exact(a) and not exact(b):
            for lig in LIGS:
                if exact(lig + b):
                    fixes[f"{a} {b} -> {a} {lig + b}"] += 1
                    return f"{a} {lig + b}"
        return m.group(0)
    text = re.sub(r"(?<![A-Za-z])([A-Za-z]+) ([a-z]+)(?![A-Za-z])", pair, text)

    # Pass 2: ligature lost at the start of a word. "rst" -> "first", "ve" -> "five".
    def lead(m):
        w = m.group(2)
        if known(w, vocab):
            return m.group(0)
        for lig in LIGS:
            cand = lig + w
            if cand.lower() in vocab:
                fixes[f"{w} -> {cand}"] += 1
                return m.group(1) + cand
        return m.group(0)
    text = re.sub(r"(^|[\s(\"'“‘/-])([a-z]+)(?![A-Za-z])", lead, text, flags=re.M)
    return text, fixes


if __name__ == "__main__":
    src, dst, extra = sys.argv[1], sys.argv[2], sys.argv[3:]
    t = open(src, encoding="utf-8").read()
    vocab = build_vocab(t, extra)
    out, fixes = fix(t, vocab)
    open(dst, "w", encoding="utf-8").write(out)
    for k, v in fixes.most_common():
        print(f"{v:4d}  {k}")
    left = Counter(w for w in re.findall(r"[A-Za-z]+", out) if len(w) > 2 and not known(w, vocab))
    if left:
        print("\nStill unknown (check against the page images):", ", ".join(f"{w}({c})" for w, c in left.most_common(40)))
