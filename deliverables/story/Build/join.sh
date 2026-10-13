#!/bin/sh
# Join the three source parts into one file, with blank lines between them.
cd "$(dirname "$0")/../Source" && { cat partA.md; printf '\n\n'; cat partB.md; printf '\n\n'; cat partC.md; printf '\n'; } > book.md
