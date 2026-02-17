# Penny Asset Skill + CLI — Design

## Summary

Consolidate all Penny assets into `penny/` at repo root. Add a zsh CLI for generating new images (poses, scenes, favicons) and packaging them into favicon/icon sets. Add a SKILL.md so agents from other projects can reference Penny assets and invoke generation.

## Directory Structure

```
penny/
  SKILL.md              — agent skill file (other projects load this)
  PENNY.md              — character bible (moved from docs/penny/)
  GENERATION-NOTES.md   — generation history (moved from docs/penny/)
  character-sheet.png   — primary Gemini generation reference
  cli                   — executable zsh CLI
  reference/            — original source images from TinyLedger
  poses/                — 26 curated white-bg poses (01-sitting.png, etc.)
  scenes/               — themed scenes (lagoon-banner-dock-1.png, etc.)
  favicons/             — generated favicon source images (per-theme)

bramble/
  .env                  — gitignored, sources GEMINI_API_KEY locally
  .env.example          — committed, documents required vars
```

`docs/penny/` is removed after migration. AGENTS.md and VISION.md updated to point at `penny/`.

## Secrets Handling

Nothing committed references IPs, 1Password, or `op read`. The CLI reads `GEMINI_API_KEY` from environment. A gitignored `.env` at repo root handles local secret loading.

`.env.example`:
```bash
GEMINI_API_KEY=
NANOBANANA_MODEL=gemini-3-pro-image-preview
```

The CLI sources `.env` if present, then requires `GEMINI_API_KEY` for generation commands.

Old generate.sh scripts are cleaned of secrets references and kept as batch generation examples.

## CLI Design

```
penny/cli <command> [options]

Commands:
  generate favicon   Generate favicon source images for a theme
  generate pose      Generate a new Penny pose via Gemini
  generate scene     Generate a themed scene via Gemini
  resize             Resize source image into favicon/icon set
  list poses         List available poses
  list scenes        List available scenes
  list themes        Show theme palettes with hex codes
  help               Show usage
```

### generate favicon

Prompts Gemini with character sheet to create a tight face close-up suitable for small sizes. Theme-tinted background (soft wash of 1-2 theme colors). Generates 2 variants for curation, saves to `penny/favicons/`.

**Follow-up:** Favicon prompt needs iteration through actual generation sessions to find what produces icon-friendly results at small resolutions. Start with a reasonable prompt, refine later.

### generate pose / generate scene

Wraps proven prompt templates from PENNY.md. Parameters:
- `--activity "gardening"` — what Penny is doing
- `--look nerdy` — which accessory variant
- `--theme lagoon` — theme palette for scenes
- `--format banner|square` — aspect ratio for scenes
- `--count 2` — number of variants (default 2)

### resize

Takes a source PNG, outputs a complete icon set to a target directory:
- `favicon.ico` (16+32 embedded)
- `favicon-16x16.png`
- `favicon-32x32.png`
- `apple-touch-icon.png` (180x180)
- `icon-192.png` (PWA)
- `icon-512.png` (PWA)

Uses ImageMagick 7 for all resizing + ICO creation.

```
penny/cli resize --input penny/favicons/lagoon.png --output ~/develop/myproject/static/
```

### list

Discovery commands for agents:
- `list poses` — filename + description for each pose
- `list scenes` — filename + theme + format for each scene
- `list themes` — theme name + hex palette

## SKILL.md

Agent-facing skill file. Covers:
1. What's available (pose/scene library, theme palettes)
2. How to generate new assets (CLI invocation)
3. How to package for a project (resize command)
4. Prompt guidance (condensed from PENNY.md)
5. Character bible reference (points to PENNY.md)

Other projects reference: `@/home/<user>/develop/bramble/penny/SKILL.md`

## Not In Scope

- Web UI for browsing (Bramble showcase already exists)
- Auto-cropping full-body poses to face (purpose-built favicon images instead)
- PWA manifest generation (project-specific config)
- Font/CSS bundling (separate static theme exports task)
- Perfecting favicon prompts (follow-up iteration task)
