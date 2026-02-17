#!/usr/bin/env zsh
# Example: batch generate themed Penny scenes
# Requires: GEMINI_API_KEY in environment or .env file
set -euo pipefail

SCRIPT_DIR="${0:a:h}"
REPO_ROOT="${SCRIPT_DIR}/../.."
cd "$REPO_ROOT"

[[ -f .env ]] && source .env
: "${GEMINI_API_KEY:?Set GEMINI_API_KEY in .env or environment}"
export GEMINI_API_KEY
export NANOBANANA_MODEL="${NANOBANANA_MODEL:-gemini-3-pro-image-preview}"

OUTDIR="penny/scenes"
REF="penny/character-sheet.png"

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

echo "=== Lagoon Banners ==="

declare -a NAMES PROMPTS
NAMES=(lagoon-banner-dock lagoon-banner-reading)
PROMPTS=(
  "Same character as reference sheet. Penny sitting on a wooden dock over calm twilight water. Cool blue #89b4fa and pink #f5c2e7 reflections. Moonlight. Wide horizontal 3:1 banner format. No whiskers. One scene, no reference sheet in output."
  "Same character as reference sheet. Penny reading in a cozy window nook. Lavender #b4befe lighting, pink cushions, rain outside. Wide horizontal 3:1 banner format. No whiskers. One scene, no reference sheet in output."
)

for i in {1..${#NAMES}}; do
  for num in 1 2; do
    generate_one "${NAMES[$i]}" "$num" "${PROMPTS[$i]}"
  done
done

echo "=== Done ==="
