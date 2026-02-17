#!/usr/bin/env zsh
# Example: batch generate Penny hoglet scenes
# Requires: GEMINI_API_KEY in environment or .env file
set -euo pipefail

SCRIPT_DIR="${0:a:h}"
REPO_ROOT="${SCRIPT_DIR}/../.."
cd "$REPO_ROOT"

# Source .env if present
[[ -f .env ]] && source .env
: "${GEMINI_API_KEY:?Set GEMINI_API_KEY in .env or environment}"
export GEMINI_API_KEY
export NANOBANANA_MODEL="${NANOBANANA_MODEL:-gemini-3-pro-image-preview}"

OUTDIR="penny/scenes"
REF="penny/character-sheet.png"
IDENTITY='This is a character reference sheet for a baby hedgehog named Penny. Using the exact same character shown — same proportions, same face, same art style, same coloring — generate a SINGLE NEW IMAGE.'
GUARD='No whiskers. Keep the same art style — soft pencil lines, gentle shading. The hoglets should be tiny versions of Penny, same coloring but smaller and rounder. Do NOT include the reference sheet. Just one scene filling the frame.'

generate_one() {
  local name="$1" num="$2" prompt="$3"
  local target="$OUTDIR/${name}-${num}.png"

  if [[ -f "$target" ]]; then
    echo "SKIP $target (already exists)"
    return 0
  fi

  echo "GENERATING $target ..."
  gemini --yolo -p "/edit $REF \"$prompt\"" 2>&1 | tail -3

  local newest=$(ls -t nanobanana-output/*.png 2>/dev/null | head -1)
  if [[ -n "$newest" ]]; then
    cp "$newest" "$target"
    echo "SAVED $target"
  else
    echo "FAILED $target — no output found"
  fi
}

echo "=== Hoglet Generation ==="

declare -A HOGLETS
HOGLETS=(
  [hoglets-sleeping]="$IDENTITY Penny is curled up in a cozy nest of soft blankets with three tiny hoglets nuzzled against her belly. Warm, tender scene on a soft cream background. $GUARD"
  [hoglets-nuzzling]="$IDENTITY Penny is sitting with two tiny hoglets nuzzling up against her. Gentle loving expression. Warm, intimate moment on a soft cream background. $GUARD"
)

for name in "${(@k)HOGLETS}"; do
  for num in 1 2; do
    generate_one "$name" "$num" "${HOGLETS[$name]}"
  done
done

echo "=== Done ==="
