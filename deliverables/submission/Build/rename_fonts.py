#!/usr/bin/env python3
"""Make three stand-alone families (LM Roman 10, LM Roman 10 Bold, LM Roman 10 Italic) from the converted
Latin Modern TTFs. Word for Mac ignores embedded bold and italic faces, so each face is embedded as its own family.
Input: ../Fonts/LatinModernRoman10-{regular,bold,italic}.ttf produced by otf2ttf.py. Output: ../Fonts/LMRoman10-*.ttf."""
import os
from fontTools.ttLib import TTFont
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Fonts')
for src, fam, fn in [('regular', 'LM Roman 10', 'LMRoman10-Regular'), ('bold', 'LM Roman 10 Bold', 'LMRoman10-Bold'), ('italic', 'LM Roman 10 Italic', 'LMRoman10-Italic')]:
    f = TTFont(os.path.join(F, f'LatinModernRoman10-{src}.ttf')); nm = f['name']
    for r in list(nm.names):
        if r.nameID in (16, 17, 21, 22): nm.removeNames(nameID=r.nameID)
    for pid, eid, lid in ((1, 0, 0), (3, 1, 0x409)):
        nm.setName(fam, 1, pid, eid, lid); nm.setName('Regular', 2, pid, eid, lid); nm.setName(fam, 4, pid, eid, lid)
        nm.setName(fn, 6, pid, eid, lid); nm.setName(fam + ';Regular', 3, pid, eid, lid)
    f['OS/2'].fsSelection = 0x40 | (f['OS/2'].fsSelection & 0xFF80); f['OS/2'].usWeightClass = 400
    f['head'].macStyle = 0; f['OS/2'].fsType = 0
    f.save(os.path.join(F, fn + '.ttf'))
