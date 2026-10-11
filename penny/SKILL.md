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

# Generate a new pose (saves to penny/poses/ by default)
penny/cli generate pose --activity "debugging code with a laptop" --look nerdy

# Generate a themed scene
penny/cli generate scene --theme lagoon --format banner --activity "reading by a pond"

# Generate favicon source images
penny/cli generate favicon --theme lagoon

# Save generated assets to YOUR project instead of Bramble
penny/cli generate favicon --theme lagoon --output-dir ~/develop/myproject/assets/
penny/cli generate pose --activity "waving hello" --output-dir ~/develop/myproject/images/

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
- `--output-dir`: save to a different directory (default: penny/poses/)

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
- `--output-dir`: save to a different directory (default: penny/scenes/)

### Favicons
Best for: project favicon source images.

```bash
penny/cli generate favicon --theme lagoon
```

Options:
- `--theme` (required): lagoon, meadow, or default
- `--count`: variants (default 2)
- `--output-dir`: save to a different directory (default: penny/favicons/)

## Resize / Packaging

Convert any source PNG into a complete favicon + app icon set. Non-square sources are center-cropped to square automatically. Small sizes (16, 32) are sharpened.

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
