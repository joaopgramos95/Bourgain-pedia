#!/bin/sh
# Serve the site locally.
#
# The repository root is the document root, not site/, so that links from a
# page to material outside site/ -- a paper's digestion under <year>/<slug>/ --
# resolve the same way they do when site/index.html is opened over file://.
PORT="${1:-8017}"
cd "$(dirname "$0")/.." || exit 1
echo "Bourgain-pedia at http://localhost:$PORT/site/"
exec python3 "$(dirname "$0")/serve.py" "$PORT"
