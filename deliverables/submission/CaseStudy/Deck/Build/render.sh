#!/bin/bash
# usage: render.sh  -> work/slide-NN.png
cd "$(dirname "$0")"
SK="/Users/perisricharan/.claude/skills/synced/639d251c-b7f1-490c-9a9e-4f6969b8ef19_ca26e898-02d8-40f1-bdf1-2895265d7862/pptx/scripts"
python3 prep.py
NODE_PATH="$PWD/node_modules" node build.js 2>&1 | grep -v "NO BUILDER"
rm -f work/*.pdf work/slide-*.png
/opt/homebrew/bin/soffice --headless --convert-to pdf --outdir work ../The_Breakfast_Paradox.pptx >/dev/null 2>&1
pdftoppm -r 110 -png work/The_Breakfast_Paradox.pdf work/slide
ls work | grep -c slide
