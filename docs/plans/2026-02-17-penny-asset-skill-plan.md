# Penny Asset Skill + CLI — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Consolidate Penny assets into `penny/` at repo root, add a zsh CLI for image generation and favicon packaging, and create a SKILL.md for cross-project agent use.

**Architecture:** All Penny files move from `docs/penny/` to `penny/`. A single executable zsh script (`penny/cli`) wraps Gemini generation and ImageMagick resizing. Secrets come from environment only — nothing committed references IPs or credential stores.

**Tech Stack:** zsh, ImageMagick 7, `gemini` CLI (nanobanana), OKLCH color tokens from `src/app.css`

---

### Task 1: Create .env.example and verify .gitignore

**Files:**
- Create: `.env.example`
- Verify: `.gitignore` (already has `.env` and `!.env.example` rules)

**Step 1: Create .env.example**

```bash
# Required for Penny image generation (Gemini backend)
GEMINI_API_KEY=

# Optional: override default Gemini model
# NANOBANANA_MODEL=gemini-3-pro-image-preview
```

**Step 2: Verify .gitignore handles .env correctly**

Check that `.gitignore` already has `.env` / `.env.*` / `!.env.example`. It does (lines 17-19), so no changes needed.

**Step 3: Commit**

```bash
git add .env.example
git commit -m "Add .env.example for Penny generation secrets"
```

---

### Task 2: Create penny/ directory and move assets

**Files:**
- Create: `penny/` directory structure
- Move: `docs/penny/PENNY.md` -> `penny/PENNY.md`
- Move: `docs/penny/GENERATION-NOTES.md` -> `penny/GENERATION-NOTES.md`
- Move: `docs/penny/character-sheet.png` -> `penny/character-sheet.png`
- Move: `docs/penny/reference/` -> `penny/reference/`
- Move: `docs/penny/poses/` -> `penny/poses/`
- Move: `docs/penny/generated/round-4/*.png` (not .sh) -> `penny/scenes/`
- Create: `penny/favicons/` (empty, with .gitkeep)

This is a pure move — all files are untracked (not yet committed), so `mv` works directly. No `git mv` needed.

**Step 1: Create directory structure**

```bash
mkdir -p penny/{reference,poses,scenes,favicons}
```

**Step 2: Move files**

```bash
mv docs/penny/PENNY.md penny/
mv docs/penny/GENERATION-NOTES.md penny/
mv docs/penny/character-sheet.png penny/
mv docs/penny/reference/* penny/reference/
mv docs/penny/poses/* penny/poses/
# Move only PNGs from round-4 (not the .sh scripts)
mv docs/penny/generated/round-4/*.png penny/scenes/
```

**Step 3: Add .gitkeep to favicons/**

```bash
touch penny/favicons/.gitkeep
```

**Step 4: Verify move**

```bash
ls penny/
# Expected: PENNY.md  GENERATION-NOTES.md  character-sheet.png  reference/  poses/  scenes/  favicons/

ls penny/poses/ | wc -l
# Expected: 26

ls penny/scenes/ | wc -l
# Expected: 18
```

**Step 5: Clean up empty docs/penny/**

```bash
rm -rf docs/penny/
```

**Step 6: Commit**

```bash
git add penny/
git commit -m "Move Penny assets from docs/penny/ to penny/ at repo root"
```

---

### Task 3: Clean generate scripts and save as examples

The old `generate.sh` and `generate-scenes.sh` had hardcoded 1P Connect IPs and `op read` references. Create cleaned versions as examples in `penny/examples/`.

**Files:**
- Create: `penny/examples/batch-generate-hoglets.sh`
- Create: `penny/examples/batch-generate-scenes.sh`
- Source: `docs/penny/generated/round-4/generate.sh` (reference only — already deleted in Task 2)

Note: The original .sh files were inside `docs/penny/generated/round-4/` which was removed in Task 2. We still have them in git history if needed, and we read them during planning. The cleaned versions below are rewritten from those.

**Step 1: Create examples directory**

```bash
mkdir -p penny/examples
```

**Step 2: Write batch-generate-hoglets.sh**

Cleaned version of the hoglets portion of generate.sh. No IPs, no `op read`. Sources `.env` for `GEMINI_API_KEY`.

```bash
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
```

**Step 3: Write batch-generate-scenes.sh**

Cleaned version of generate-scenes.sh. Same pattern — `.env` for secrets, short prompt format.

```bash
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
```

**Step 4: Make executable**

```bash
chmod +x penny/examples/*.sh
```

**Step 5: Commit**

```bash
git add penny/examples/
git commit -m "Add cleaned batch generation examples (no secrets)"
```

---

### Task 4: Write CLI core — help, env loading, subcommand routing

The main CLI script. This task covers the skeleton: argument parsing, `.env` loading, `help` output, and routing to subcommands.

**Files:**
- Create: `penny/cli`

**Step 1: Write the CLI skeleton**

```bash
#!/usr/bin/env zsh
# Penny asset CLI — generate, resize, and list Penny the Hedgehog assets
set -euo pipefail

SCRIPT_DIR="${0:a:h}"
REPO_ROOT="${SCRIPT_DIR}/.."

# Source .env if present (for GEMINI_API_KEY)
[[ -f "$REPO_ROOT/.env" ]] && source "$REPO_ROOT/.env"

# Paths
CHAR_SHEET="$SCRIPT_DIR/character-sheet.png"
POSES_DIR="$SCRIPT_DIR/poses"
SCENES_DIR="$SCRIPT_DIR/scenes"
FAVICONS_DIR="$SCRIPT_DIR/favicons"

# ── Helpers ──────────────────────────────────────────────────────────

die() { echo "error: $*" >&2; exit 1; }

require_gemini() {
  : "${GEMINI_API_KEY:?Set GEMINI_API_KEY in .env or environment}"
  export GEMINI_API_KEY
  export NANOBANANA_MODEL="${NANOBANANA_MODEL:-gemini-3-pro-image-preview}"
  command -v gemini &>/dev/null || die "gemini CLI not found — install nanobanana"
}

require_magick() {
  command -v magick &>/dev/null || die "ImageMagick 7 (magick) not found"
}

usage() {
  cat <<'USAGE'
penny/cli — Penny the Hedgehog asset toolkit

Usage: penny/cli <command> [options]

Commands:
  generate favicon   Generate favicon source images for a theme
  generate pose      Generate a new Penny pose via Gemini
  generate scene     Generate a themed scene via Gemini
  resize             Resize source image into favicon/icon set
  list poses         List available poses in library
  list scenes        List available scenes in library
  list themes        Show theme palettes with hex codes
  help               Show this message

Examples:
  penny/cli generate pose --activity "debugging code" --look nerdy
  penny/cli generate scene --theme lagoon --format banner --activity "reading by a pond"
  penny/cli generate favicon --theme lagoon
  penny/cli resize --input penny/favicons/lagoon.png --output ~/project/static/
  penny/cli list poses
USAGE
}

# ── Theme palettes (hex codes for Gemini prompts) ────────────────────

typeset -A THEME_COLORS THEME_LABELS
THEME_COLORS=(
  [lagoon]="#89b4fa (blue), #f5c2e7 (pink), #b4befe (lavender), #1e1e2e (navy), #94e2d5 (teal)"
  [meadow]="#d4a574 (sandstone), #8b7355 (golden brown), #c4956a (copper), #e8d5b7 (cream), #7a8b5c (olive)"
)
THEME_LABELS=(
  [lagoon]="Lagoon — Cool, polished, mysterious (Catppuccin)"
  [meadow]="Meadow — Warm, earthy, cozy (Desert)"
)

# ── Subcommand routing ───────────────────────────────────────────────

cmd="${1:-help}"
sub="${2:-}"
shift 2 2>/dev/null || true

case "$cmd" in
  generate)
    case "$sub" in
      favicon) cmd_generate_favicon "$@" ;;
      pose)    cmd_generate_pose "$@" ;;
      scene)   cmd_generate_scene "$@" ;;
      *)       die "Unknown generate target: $sub (try: favicon, pose, scene)" ;;
    esac
    ;;
  resize)    cmd_resize "$@" ;;
  list)
    case "$sub" in
      poses)   cmd_list_poses ;;
      scenes)  cmd_list_scenes ;;
      themes)  cmd_list_themes ;;
      *)       die "Unknown list target: $sub (try: poses, scenes, themes)" ;;
    esac
    ;;
  help|--help|-h) usage ;;
  *) die "Unknown command: $cmd (try: generate, resize, list, help)" ;;
esac
```

The subcommand functions (`cmd_generate_*`, `cmd_resize`, `cmd_list_*`) will be added in subsequent tasks. For now the routing calls them — they'll be defined above the routing block.

**Step 2: Make executable**

```bash
chmod +x penny/cli
```

**Step 3: Verify help works**

```bash
penny/cli help
# Expected: usage text prints cleanly
```

**Step 4: Commit**

```bash
git add penny/cli
git commit -m "Add penny/cli skeleton — env loading, routing, help"
```

---

### Task 5: Write CLI list subcommands

**Files:**
- Modify: `penny/cli`

Add `cmd_list_poses`, `cmd_list_scenes`, `cmd_list_themes` functions. These are pure discovery — no external dependencies.

**Step 1: Write cmd_list_poses**

Reads filenames from `penny/poses/`, extracts the name portion. Each pose is named `NN-description.png`.

```bash
cmd_list_poses() {
  echo "Available poses (penny/poses/):"
  echo ""
  for f in "$POSES_DIR"/*.png(N); do
    local base="${f:t:r}"  # filename without extension
    local num="${base%%-*}"
    local name="${base#*-}"
    printf "  %s  %s\n" "$num" "${name//-/ }"
  done
  echo ""
  echo "$(ls "$POSES_DIR"/*.png 2>/dev/null | wc -l | tr -d ' ') poses total"
}
```

**Step 2: Write cmd_list_scenes**

```bash
cmd_list_scenes() {
  echo "Available scenes (penny/scenes/):"
  echo ""
  for f in "$SCENES_DIR"/*.png(N); do
    local base="${f:t:r}"
    # Parse: theme-format-description-variant (e.g., lagoon-banner-dock-1)
    if [[ "$base" =~ '^(hoglets|lagoon|meadow)-(.+)-([0-9]+)$' ]]; then
      local theme="${match[1]}"
      local desc="${match[2]}"
      local variant="${match[3]}"
      printf "  %-8s %s (v%s)\n" "$theme" "${desc//-/ }" "$variant"
    else
      printf "  %s\n" "$base"
    fi
  done
  echo ""
  echo "$(ls "$SCENES_DIR"/*.png 2>/dev/null | wc -l | tr -d ' ') scenes total"
}
```

**Step 3: Write cmd_list_themes**

```bash
cmd_list_themes() {
  echo "Available themes:"
  echo ""
  for theme in lagoon meadow; do
    echo "  ${THEME_LABELS[$theme]}"
    echo "  Colors: ${THEME_COLORS[$theme]}"
    echo ""
  done
}
```

**Step 4: Verify**

```bash
penny/cli list poses
penny/cli list scenes
penny/cli list themes
# Check output looks reasonable
```

**Step 5: Commit**

```bash
git add penny/cli
git commit -m "Add list subcommands to penny/cli"
```

---

### Task 6: Write CLI resize subcommand

The favicon/icon packaging pipeline. Takes a source PNG and outputs a complete set.

**Files:**
- Modify: `penny/cli`

**Step 1: Write cmd_resize**

```bash
cmd_resize() {
  local input="" output="."

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --input|-i)  input="$2"; shift 2 ;;
      --output|-o) output="$2"; shift 2 ;;
      *) die "Unknown resize option: $1" ;;
    esac
  done

  [[ -n "$input" ]] || die "resize requires --input <source.png>"
  [[ -f "$input" ]] || die "Input file not found: $input"
  require_magick

  mkdir -p "$output"

  echo "Resizing $input -> $output/"

  # PNG icons at standard sizes
  local -A SIZES
  SIZES=(
    [favicon-16x16.png]=16
    [favicon-32x32.png]=32
    [apple-touch-icon.png]=180
    [icon-192.png]=192
    [icon-512.png]=512
  )

  for name size in "${(@kv)SIZES}"; do
    magick "$input" -resize "${size}x${size}" -gravity center -extent "${size}x${size}" "$output/$name"
    echo "  $name (${size}x${size})"
  done

  # ICO with 16 and 32 embedded
  magick "$input" -resize 16x16 -gravity center -extent 16x16 "$output/favicon-16.tmp.png"
  magick "$input" -resize 32x32 -gravity center -extent 32x32 "$output/favicon-32.tmp.png"
  magick "$output/favicon-16.tmp.png" "$output/favicon-32.tmp.png" "$output/favicon.ico"
  rm -f "$output/favicon-16.tmp.png" "$output/favicon-32.tmp.png"
  echo "  favicon.ico (16+32)"

  echo ""
  echo "Done. $(ls "$output"/favicon* "$output"/icon-* "$output"/apple-* 2>/dev/null | wc -l | tr -d ' ') files written to $output/"
}
```

**Step 2: Test with an existing pose image**

```bash
mkdir -p /tmp/penny-resize-test
penny/cli resize --input penny/poses/01-sitting.png --output /tmp/penny-resize-test/
ls -la /tmp/penny-resize-test/
# Expected: favicon.ico, favicon-16x16.png, favicon-32x32.png, apple-touch-icon.png, icon-192.png, icon-512.png
identify /tmp/penny-resize-test/favicon-32x32.png
# Expected: PNG 32x32
rm -rf /tmp/penny-resize-test
```

**Step 3: Commit**

```bash
git add penny/cli
git commit -m "Add resize subcommand — favicon/icon packaging pipeline"
```

---

### Task 7: Write CLI generate helpers

Shared generation function used by all `generate` subcommands. Wraps the proven `gemini --yolo -p "/edit ..."` pattern.

**Files:**
- Modify: `penny/cli`

**Step 1: Write the shared generate_image function**

```bash
# Generates an image via Gemini edit, saves to target path
# Usage: generate_image <target_path> <prompt>
generate_image() {
  local target="$1" prompt="$2"

  if [[ -f "$target" ]]; then
    echo "SKIP $target (already exists)"
    return 0
  fi

  echo "Generating $target ..."
  cd "$REPO_ROOT"
  gemini --yolo -p "/edit $CHAR_SHEET \"$prompt\"" 2>&1 | tail -3

  local newest=$(ls -t nanobanana-output/*.png 2>/dev/null | head -1)
  if [[ -n "$newest" ]]; then
    cp "$newest" "$target"
    echo "Saved $target"
    return 0
  else
    echo "Failed — no output image produced"
    return 1
  fi
}
```

**Step 2: Commit**

```bash
git add penny/cli
git commit -m "Add shared generate_image helper to penny/cli"
```

---

### Task 8: Write CLI generate pose subcommand

**Files:**
- Modify: `penny/cli`

**Step 1: Write cmd_generate_pose**

```bash
cmd_generate_pose() {
  local activity="" look="" count=2 name=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --activity|-a) activity="$2"; shift 2 ;;
      --look|-l)     look="$2"; shift 2 ;;
      --count|-c)    count="$2"; shift 2 ;;
      --name|-n)     name="$2"; shift 2 ;;
      *) die "Unknown generate pose option: $1" ;;
    esac
  done

  [[ -n "$activity" ]] || die "generate pose requires --activity <description>"
  require_gemini

  # Build the name from activity if not provided
  if [[ -z "$name" ]]; then
    # Next number in sequence
    local last=$(ls "$POSES_DIR"/*.png 2>/dev/null | sort | tail -1)
    local next_num=1
    if [[ -n "$last" ]]; then
      local last_base="${last:t:r}"
      next_num=$(( ${last_base%%-*} + 1 ))
    fi
    local slug="${activity// /-}"
    slug="${slug:l}"  # lowercase
    name="$(printf '%02d' $next_num)-${slug}"
  fi

  # Build prompt
  local identity='This is a character reference sheet for a baby hedgehog named Penny. Using the exact same character shown — same proportions, same face, same art style, same coloring — generate a SINGLE NEW IMAGE of just this one character.'
  local scene="She is ${activity}."
  if [[ -n "$look" ]]; then
    scene="She is wearing her ${look} look. ${scene}"
  fi
  local guard='No whiskers. Output ONLY the new single pose on a white background. Do NOT include the reference sheet or any of the original poses. Just one hedgehog in one new pose, filling the frame.'

  local prompt="${identity} ${scene} ${guard}"

  echo "Generating pose: $activity"
  [[ -n "$look" ]] && echo "Look: $look"
  echo "Variants: $count"
  echo ""

  for num in $(seq 1 "$count"); do
    generate_image "$POSES_DIR/${name}-v${num}.png" "$prompt"
    echo ""
  done

  echo "Done. Check $POSES_DIR/ for results."
}
```

**Step 2: Verify help path works (no actual generation)**

```bash
penny/cli generate pose 2>&1 || true
# Expected: error about --activity required
```

**Step 3: Commit**

```bash
git add penny/cli
git commit -m "Add generate pose subcommand to penny/cli"
```

---

### Task 9: Write CLI generate scene subcommand

**Files:**
- Modify: `penny/cli`

**Step 1: Write cmd_generate_scene**

```bash
cmd_generate_scene() {
  local activity="" theme="" format="banner" count=2 name=""

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --activity|-a) activity="$2"; shift 2 ;;
      --theme|-t)    theme="$2"; shift 2 ;;
      --format|-f)   format="$2"; shift 2 ;;
      --count|-c)    count="$2"; shift 2 ;;
      --name|-n)     name="$2"; shift 2 ;;
      *) die "Unknown generate scene option: $1" ;;
    esac
  done

  [[ -n "$activity" ]] || die "generate scene requires --activity <description>"
  [[ -n "$theme" ]] || die "generate scene requires --theme <lagoon|meadow>"
  [[ -n "${THEME_COLORS[$theme]:-}" ]] || die "Unknown theme: $theme (try: lagoon, meadow)"
  require_gemini

  if [[ -z "$name" ]]; then
    local slug="${activity// /-}"
    slug="${slug:l}"
    name="${theme}-${format}-${slug}"
  fi

  # Format instruction
  local fmt_instruction=""
  case "$format" in
    banner) fmt_instruction="Wide horizontal 3:1 banner format." ;;
    square) fmt_instruction="Square 1:1 composition." ;;
    *) die "Unknown format: $format (try: banner, square)" ;;
  esac

  # Short scene prompt (proven to outperform verbose ones)
  local colors="${THEME_COLORS[$theme]}"
  local prompt="Same character as reference sheet. Penny ${activity}. Use colors: ${colors}. ${fmt_instruction} No whiskers. One scene, no reference sheet in output."

  echo "Generating scene: $activity"
  echo "Theme: $theme | Format: $format"
  echo "Variants: $count"
  echo ""

  for num in $(seq 1 "$count"); do
    generate_image "$SCENES_DIR/${name}-${num}.png" "$prompt"
    echo ""
  done

  echo "Done. Check $SCENES_DIR/ for results."
}
```

**Step 2: Verify error path**

```bash
penny/cli generate scene 2>&1 || true
# Expected: error about --activity required
penny/cli generate scene --activity "test" 2>&1 || true
# Expected: error about --theme required
```

**Step 3: Commit**

```bash
git add penny/cli
git commit -m "Add generate scene subcommand to penny/cli"
```

---

### Task 10: Write CLI generate favicon subcommand

Initial version — prompt will need iteration later. Mark as starting point.

**Files:**
- Modify: `penny/cli`

**Step 1: Write cmd_generate_favicon**

```bash
cmd_generate_favicon() {
  local theme="" count=2

  while [[ $# -gt 0 ]]; do
    case "$1" in
      --theme|-t) theme="$2"; shift 2 ;;
      --count|-c) count="$2"; shift 2 ;;
      *) die "Unknown generate favicon option: $1" ;;
    esac
  done

  [[ -n "$theme" ]] || die "generate favicon requires --theme <lagoon|meadow|default>"
  require_gemini

  local name="$theme"

  # Build favicon-specific prompt
  # NOTE: This prompt is a starting point. Iterate through actual generation
  # sessions to find what produces the best icon-friendly results at small sizes.
  local colors=""
  if [[ "$theme" != "default" ]]; then
    [[ -n "${THEME_COLORS[$theme]:-}" ]] || die "Unknown theme: $theme (try: lagoon, meadow, default)"
    colors="Background: soft wash of theme colors ${THEME_COLORS[$theme]}."
  else
    colors="Clean white background."
  fi

  local prompt="Same character as reference sheet. A close-up of Penny's face, centered, looking directly at the viewer with a warm friendly expression. Tight crop — just head and upper body filling the frame. Simple composition that reads clearly at small sizes. Bold shapes, minimal fine detail. ${colors} No whiskers. No reference sheet in output. Just one image."

  echo "Generating favicon source: $theme"
  echo "Variants: $count"
  echo "NOTE: Favicon prompts are a starting point — curate results and iterate."
  echo ""

  for num in $(seq 1 "$count"); do
    generate_image "$FAVICONS_DIR/${name}-${num}.png" "$prompt"
    echo ""
  done

  echo "Done. Check $FAVICONS_DIR/ for results."
  echo "Use 'penny/cli resize --input $FAVICONS_DIR/<chosen>.png --output <target>/' to package."
}
```

**Step 2: Verify error path**

```bash
penny/cli generate favicon 2>&1 || true
# Expected: error about --theme required
```

**Step 3: Commit**

```bash
git add penny/cli
git commit -m "Add generate favicon subcommand (initial prompt, needs iteration)"
```

---

### Task 11: Write SKILL.md

The agent-facing skill file that other projects load.

**Files:**
- Create: `penny/SKILL.md`

**Step 1: Write SKILL.md**

Key sections: what's available, how to generate, how to package, prompt guidance, character reference.

The skill should be concise — agents load it for context, not as a tutorial. Point to PENNY.md for full character details.

```markdown
---
name: penny
description: Penny the Hedgehog asset toolkit. Generate poses, scenes, and favicon sets. Use when a project needs Penny branding — favicons, app icons, banners, or new illustrations.
---

# Penny Asset Toolkit

Generate, browse, and package Penny the Hedgehog assets for any project.

## Quick Start

```bash
# Browse available assets
penny/cli list poses
penny/cli list scenes
penny/cli list themes

# Generate a new pose
penny/cli generate pose --activity "debugging code with a laptop" --look nerdy

# Generate a themed scene
penny/cli generate scene --theme lagoon --format banner --activity "reading by a pond"

# Generate favicon source images
penny/cli generate favicon --theme lagoon

# Package into favicon/icon set for a project
penny/cli resize --input penny/favicons/lagoon-1.png --output ~/develop/myproject/static/
```

All commands run from the Bramble repo root (`/home/<user>/develop/bramble`).

## What's Available

### Poses (penny/poses/)
26 curated white-background character poses. Numbered `01-sitting.png` through `26-yoga.png`. Activities include: sitting, peeking, walking, sleeping, reading, explorer, cozy, sporty, professional, hiking, geek, gardening, celebrating, building, painting, stargazing, cooking, yoga.

### Scenes (penny/scenes/)
18 themed background scenes. Formats: banner (3:1) and square (1:1). Themes: lagoon (cool blue/pink), meadow (warm sandstone/golden). Also includes hoglet scenes (Penny with baby hedgehogs).

### Favicons (penny/favicons/)
Generated face close-ups optimized for small-size display. Per-theme tinted backgrounds.

## Generation

Requires `GEMINI_API_KEY` — set in `.env` at repo root or export directly.

### Poses
Best for: app illustrations, UI elements, empty states, loading screens.

```bash
penny/cli generate pose --activity "planting a seedling" --look default --count 2
```

Options:
- `--activity` (required): what Penny is doing
- `--look`: nerdy, cozy, sporty, professional, explorer, geek, default
- `--count`: variants to generate (default 2, curate the best)
- `--name`: override output filename

### Scenes
Best for: banners, hero images, README headers.

```bash
penny/cli generate scene --theme meadow --format banner --activity "picnic on a hillside"
```

Options:
- `--activity` (required): scene description
- `--theme` (required): lagoon or meadow
- `--format`: banner (3:1) or square (1:1)
- `--count`: variants (default 2)

### Favicons
Best for: project favicon source images.

```bash
penny/cli generate favicon --theme lagoon
```

Favicon prompts are a starting point — curate results and iterate on the prompt if needed.

## Resize / Packaging

Convert any source PNG into a complete favicon + app icon set:

```bash
penny/cli resize --input penny/favicons/lagoon-1.png --output ~/develop/myproject/static/
```

Outputs:
- `favicon.ico` (16+32 embedded)
- `favicon-16x16.png`, `favicon-32x32.png`
- `apple-touch-icon.png` (180x180)
- `icon-192.png`, `icon-512.png` (PWA)

## Character Reference

Full character bible: `penny/PENNY.md`
Generation history and learnings: `penny/GENERATION-NOTES.md`
Character sheet (generation input): `penny/character-sheet.png`

## Theme Palettes

**Lagoon** (Catppuccin): #89b4fa (blue), #f5c2e7 (pink), #b4befe (lavender), #1e1e2e (navy), #94e2d5 (teal)

**Meadow** (Desert): #d4a574 (sandstone), #8b7355 (golden brown), #c4956a (copper), #e8d5b7 (cream), #7a8b5c (olive)
```

**Step 2: Commit**

```bash
git add penny/SKILL.md
git commit -m "Add penny/SKILL.md — agent-facing asset toolkit reference"
```

---

### Task 12: Update AGENTS.md and VISION.md references

Update all internal references from `docs/penny/` to `penny/`.

**Files:**
- Modify: `AGENTS.md`
- Modify: `VISION.md`

**Step 1: Update AGENTS.md**

In the "For Other Projects" section, add a bullet pointing to `penny/SKILL.md`. Also update any `docs/penny/` references.

Add after the VISION.md bullet:
```markdown
- **`penny/SKILL.md`** — Penny asset toolkit: generate poses/scenes/favicons, resize for projects. CLI reference.
- **`penny/PENNY.md`** — full character bible, prompt templates, generation guidelines.
```

In the "Key Files" section, add:
```markdown
- `penny/` — all Penny assets, generation CLI, and agent skill
```

**Step 2: Update VISION.md**

The Penny brand section references image generation guidelines. These now live in `penny/PENNY.md` instead of being inline. Update the "Image Generation Guidelines" section to point there instead of duplicating content. Leave the existing guidelines as-is since they're still accurate — just add a note pointing to the full reference.

Add at the end of the "Image Generation Guidelines" section:
```markdown
Full prompt templates, variant definitions, and generation history: see `penny/PENNY.md` and `penny/GENERATION-NOTES.md`.
```

**Step 3: Commit**

```bash
git add AGENTS.md VISION.md
git commit -m "Update AGENTS.md and VISION.md to reference penny/ directory"
```

---

### Task 13: Final verification and cleanup

**Step 1: Verify directory structure**

```bash
ls penny/
# Expected: SKILL.md  PENNY.md  GENERATION-NOTES.md  character-sheet.png  cli  examples/  reference/  poses/  scenes/  favicons/

ls docs/penny/ 2>&1
# Expected: No such file or directory
```

**Step 2: Verify CLI works end-to-end**

```bash
penny/cli help
penny/cli list poses
penny/cli list scenes
penny/cli list themes
```

**Step 3: Verify resize works**

```bash
mkdir -p /tmp/penny-test
penny/cli resize --input penny/poses/01-sitting.png --output /tmp/penny-test/
ls /tmp/penny-test/
# Expected: 6 files (favicon.ico + 5 PNGs)
rm -rf /tmp/penny-test
```

**Step 4: Verify error handling**

```bash
penny/cli generate pose 2>&1 || true
# Expected: error about --activity
penny/cli generate scene --activity "test" 2>&1 || true
# Expected: error about --theme
penny/cli generate favicon 2>&1 || true
# Expected: error about --theme
penny/cli resize 2>&1 || true
# Expected: error about --input
```

**Step 5: Check nothing leaks secrets**

```bash
grep -r 'op read\|op://' penny/ .env.example || echo "Clean — no 1P references"
grep -r '100\.\|10\.10\.' penny/ .env.example || echo "Clean — no IPs"
```

**Step 6: Final commit if any cleanup needed**

Only if previous steps revealed issues to fix.
