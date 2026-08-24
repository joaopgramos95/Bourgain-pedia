#!/bin/sh
# Open the Bourgain-pedia site locally.
#
# Installed as the command `Bourgain.local` (and `Bourgan.local`) by
# tools/install.sh.  Serves the repository -- not site/, so that a paper's
# digestion under <year>/<slug>/ resolves -- and opens the browser.
#
#   Bourgain.local            start if needed, then open
#   Bourgain.local stop       stop the server this repo started
#   Bourgain.local status     report
#   Bourgain.local -p 9000    force a particular port
#
# If the preferred port is busy, the next free one is used automatically; if a
# server for THIS repository is already up, it is reused rather than restarted.
set -u

PORT=""
DEFAULT_PORT=8017
CMD=open

while [ $# -gt 0 ]; do
  case "$1" in
    stop|status|open) CMD="$1"; shift ;;
    -p|--port) PORT="${2:-}"; shift 2 ;;
    -h|--help) sed -n '2,17p' "$0" | sed 's/^#\{0,1\} \{0,1\}//'; exit 0 ;;
    *) echo "Bourgain.local: unknown argument '$1' (try --help)" >&2; exit 2 ;;
  esac
done

# Resolve the repository root from this script, following symlinks, so the
# command works from any clone location without configuration.
SELF="$0"
while [ -L "$SELF" ]; do
  LINK=$(readlink "$SELF")
  case "$LINK" in /*) SELF="$LINK" ;; *) SELF="$(dirname "$SELF")/$LINK" ;; esac
done
ROOT=$(cd "$(dirname "$SELF")/.." && pwd)
STATE="${TMPDIR:-/tmp}/bourgain-pedia.$(printf '%s' "$ROOT" | cksum | cut -d' ' -f1)"

# Is something serving *this* repository on $1?  We look for a file only this
# repository has, so we never adopt an unrelated server on the same port.
serving_us() {
  code=$(curl -s -o /dev/null -m 1 -w '%{http_code}' \
         "http://localhost:$1/site/data/papers.js" 2>/dev/null) || return 1
  [ "$code" = "200" ]
}

# Ask python (already required) for the first free port at or after $1.
# Portable, and it cannot hang the way a /dev/tcp probe can under sh.
first_free_port() {
  python3 - "$1" <<'PYEOF'
import socket, sys
start = int(sys.argv[1])
for port in range(start, start + 40):
    # A port is in use if something accepts a connection on it.  Do not test by
    # binding: with SO_REUSEADDR a bind can succeed alongside a live listener,
    # and without it the check is still wrong when the listener holds 0.0.0.0.
    with socket.socket() as probe:
        probe.settimeout(0.25)
        if probe.connect_ex(("127.0.0.1", port)) == 0:
            continue
    print(port)
    break
PYEOF
}

case "$CMD" in
  stop)
    if [ -f "$STATE" ]; then
      read -r pid oldport < "$STATE" 2>/dev/null || true
      if [ -n "${pid:-}" ] && kill "$pid" 2>/dev/null; then
        echo "Bourgain-pedia: stopped (port ${oldport:-?})."
      else
        echo "Bourgain-pedia: nothing of ours was running."
      fi
      rm -f "$STATE"
    else
      echo "Bourgain-pedia: nothing of ours was running."
    fi
    exit 0 ;;
  status)
    if [ -f "$STATE" ]; then
      read -r pid oldport < "$STATE" 2>/dev/null || true
      if [ -n "${oldport:-}" ] && serving_us "$oldport"; then
        echo "Bourgain-pedia: serving http://localhost:$oldport/site/ from $ROOT"; exit 0
      fi
    fi
    echo "Bourgain-pedia: not running (repository $ROOT)."
    exit 0 ;;
esac

# Reuse a server we already started for this repository.
if [ -f "$STATE" ]; then
  read -r pid oldport < "$STATE" 2>/dev/null || true
  if [ -n "${oldport:-}" ] && serving_us "$oldport"; then
    URL="http://localhost:$oldport/site/"
    echo "Bourgain-pedia: already serving $URL"
    exec_open=1
  fi
fi

if [ "${exec_open:-0}" != "1" ]; then
  command -v python3 >/dev/null 2>&1 || {
    echo "Bourgain.local: python3 is required but was not found." >&2; exit 1; }

  # A server for this repo may already be up on the preferred port, started
  # some other way; adopt it rather than starting a second one.
  probe=${PORT:-$DEFAULT_PORT}
  if serving_us "$probe"; then
    chosen="$probe"
  else
    n=$(first_free_port "$probe")
    if [ -z "${n:-}" ]; then
      echo "Bourgain.local: no free port in $probe..$((probe + 39))." >&2
      echo "  try: Bourgain.local -p 9123" >&2
      exit 1
    fi
    # Detach every descriptor, including stdin: otherwise the server inherits
    # the caller's stdout and a pipeline such as `Bourgain.local | tee log`
    # never sees end-of-file.
    ( cd "$ROOT" && nohup python3 -m http.server "$n" </dev/null >/dev/null 2>&1 &
      echo "$! $n" > "$STATE" ) </dev/null >/dev/null 2>&1
    i=0
    while [ $i -lt 30 ]; do
      serving_us "$n" && break
      sleep 0.2; i=$((i + 1))
    done
    if serving_us "$n"; then
      chosen="$n"
    else
      rm -f "$STATE"
      echo "Bourgain.local: the server did not come up on port $n." >&2
      exit 1
    fi
  fi
  URL="http://localhost:$chosen/site/"
  echo "Bourgain-pedia: serving $URL from $ROOT"
fi

if   command -v open      >/dev/null 2>&1; then open "$URL"
elif command -v xdg-open  >/dev/null 2>&1; then xdg-open "$URL"
elif command -v powershell >/dev/null 2>&1; then powershell -c "Start-Process '$URL'"
else echo "  open it yourself: $URL"; fi
