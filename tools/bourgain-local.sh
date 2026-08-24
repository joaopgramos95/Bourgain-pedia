#!/bin/sh
# Open the Bourgain-pedia site locally.
#
# Installed as the commands `Bourgain.local` and `Bourgan.local` (symlinks in
# ~/.local/bin, which is already on PATH).  Starts a static server rooted at the
# repository -- not at site/, so that a paper's digestion under <year>/<slug>/
# resolves -- then opens the browser.  A server already serving this repository
# on the port is reused rather than restarted.
#
#   Bourgain.local            start if needed, then open
#   Bourgain.local stop       stop the server
#   Bourgain.local status     report
#   Bourgain.local -p 9000    use another port
set -u

PORT=8017
CMD=open

while [ $# -gt 0 ]; do
  case "$1" in
    stop|status|open) CMD="$1"; shift ;;
    -p|--port) PORT="${2:-8017}"; shift 2 ;;
    -h|--help) sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Bourgain.local: unknown argument '$1' (try --help)" >&2; exit 2 ;;
  esac
done

# Resolve the repository root from this script's location, following symlinks.
SELF="$0"
while [ -L "$SELF" ]; do
  LINK=$(readlink "$SELF")
  case "$LINK" in /*) SELF="$LINK" ;; *) SELF="$(dirname "$SELF")/$LINK" ;; esac
done
ROOT=$(cd "$(dirname "$SELF")/.." && pwd)
URL="http://localhost:$PORT/site/"
PIDFILE="${TMPDIR:-/tmp}/bourgain-pedia-$PORT.pid"

serving() {
  # 200 on the site index means something useful is on the port
  [ "$(curl -s -o /dev/null -m 2 -w '%{http_code}' "$URL" 2>/dev/null)" = "200" ]
}

case "$CMD" in
  stop)
    if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null; then
      kill "$(cat "$PIDFILE")" && rm -f "$PIDFILE"
      echo "Bourgain-pedia: stopped (port $PORT)."
    else
      pkill -f "http.server $PORT" 2>/dev/null \
        && echo "Bourgain-pedia: stopped (port $PORT)." \
        || echo "Bourgain-pedia: nothing running on port $PORT."
      rm -f "$PIDFILE"
    fi
    exit 0 ;;
  status)
    if serving; then echo "Bourgain-pedia: serving $URL from $ROOT"
    else echo "Bourgain-pedia: not running on port $PORT."; fi
    exit 0 ;;
esac

if serving; then
  echo "Bourgain-pedia: already serving $URL"
else
  if ! command -v python3 >/dev/null 2>&1; then
    echo "Bourgain.local: python3 not found." >&2; exit 1
  fi
  ( cd "$ROOT" && nohup python3 -m http.server "$PORT" >/dev/null 2>&1 & echo $! > "$PIDFILE" )
  n=0
  while [ $n -lt 40 ]; do
    serving && break
    sleep 0.1; n=$((n+1))
  done
  if serving; then
    echo "Bourgain-pedia: serving $URL from $ROOT"
  else
    echo "Bourgain.local: server did not come up on port $PORT." >&2
    echo "  (something else may be using it -- try: Bourgain.local -p 8018)" >&2
    exit 1
  fi
fi

if command -v open >/dev/null 2>&1; then open "$URL"
elif command -v xdg-open >/dev/null 2>&1; then xdg-open "$URL"
else echo "  open it yourself: $URL"; fi
