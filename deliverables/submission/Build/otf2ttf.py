import sys
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
def convert(src, dst):
    f = TTFont(src); gs = f.getGlyphSet(); order = f.getGlyphOrder()
    glyf = {}
    for n in order:
        pen = TTGlyphPen(gs); gs[n].draw(Cu2QuPen(pen, 1.0, reverse_direction=True)); glyf[n] = pen.glyph()
    f["loca"] = newTable("loca"); t = f["glyf"] = newTable("glyf"); t.glyphOrder = order; t.glyphs = glyf
    del f["CFF "]
    if "VORG" in f: del f["VORG"]
    f["maxp"] = newTable("maxp"); m = f["maxp"]; m.tableVersion = 0x00010000
    for k in ("maxZones","maxTwilightPoints","maxStorage","maxFunctionDefs","maxInstructionDefs","maxStackElements","maxSizeOfInstructions","maxComponentElements"): setattr(m, k, 0)
    m.maxZones = 1; m.maxPoints = m.maxContours = m.maxCompositePoints = m.maxCompositeContours = m.maxComponentDepth = 0
    f["head"].glyphDataFormat = 0; f["post"].formatType = 2.0; f["post"].extraNames = []; f["post"].mapping = {}
    f.sfntVersion = "\x00\x01\x00\x00"; f.save(dst)
if __name__ == "__main__": convert(sys.argv[1], sys.argv[2])
