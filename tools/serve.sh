#!/bin/sh
# Serve the site locally.  (It also works by opening site/index.html directly —
# the data files are plain JS, not fetched JSON — but a server is tidier.)
PORT="${1:-8017}"
cd "$(dirname "$0")/../site" || exit 1
echo "Bourgain-pedia at http://localhost:$PORT/"
exec python3 -m http.server "$PORT"
