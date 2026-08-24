#!/bin/sh
# Install the `Bourgain.local` command.
#
#   sh tools/install.sh
#
# Creates a symlink to tools/bourgain-local.sh in a directory on your PATH, so
# that typing `Bourgain.local` in a terminal serves this clone and opens the
# site in your browser.  Nothing is copied: the link points back into this
# repository, so `git pull` updates the command too.
#
# Git deliberately has no post-clone hook -- cloning a repository must never run
# code -- so this one command after cloning is the closest thing to automatic.
set -u

ROOT=$(cd "$(dirname "$0")/.." && pwd)
TARGET="$ROOT/tools/bourgain-local.sh"
NAMES="Bourgain.local Bourgan.local"

[ -x "$TARGET" ] || chmod +x "$TARGET" 2>/dev/null || true

# Pick a writable directory that is already on PATH; ~/.local/bin is created if
# it is on PATH but missing.  We never use sudo and never edit shell rc files
# without saying so.
BIN=""
for d in "$HOME/.local/bin" "$HOME/bin" /usr/local/bin; do
  case ":$PATH:" in *":$d:"*) ;; *) continue ;; esac
  [ -d "$d" ] || mkdir -p "$d" 2>/dev/null || continue
  [ -w "$d" ] || continue
  BIN="$d"; break
done

if [ -z "$BIN" ]; then
  mkdir -p "$HOME/.local/bin" 2>/dev/null || true
  if [ -w "$HOME/.local/bin" ]; then
    BIN="$HOME/.local/bin"
    cat <<EOF

  Note: $BIN is not on your PATH. Add this line to your shell profile
  (~/.zshrc for zsh, ~/.bashrc for bash) and open a new terminal:

      export PATH="\$HOME/.local/bin:\$PATH"

EOF
  else
    echo "install.sh: found no writable directory on PATH." >&2
    echo "  Run the site with:  sh $ROOT/tools/serve.sh" >&2
    exit 1
  fi
fi

for name in $NAMES; do
  existing=$(command -v "$name" 2>/dev/null || true)
  if [ -n "$existing" ] && [ "$(readlink "$existing" 2>/dev/null)" != "$TARGET" ] \
     && [ "$existing" != "$BIN/$name" ]; then
    echo "  skipped $name — a different command of that name already exists at $existing"
    continue
  fi
  ln -sfn "$TARGET" "$BIN/$name"
  echo "  installed $BIN/$name -> tools/bourgain-local.sh"
done

cat <<EOF

Done. From any directory:

    Bourgain.local          serve this clone and open the site
    Bourgain.local status   is it running?
    Bourgain.local stop     stop it

The repository is the document root, so a paper's digestion under
<year>/<slug>/ resolves from the site. If port 8017 is taken, the next free
port is used automatically.
EOF
