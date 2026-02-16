# Bramble — Agent Instructions

Personal design system, component showcase, and brand guide.

## For Other Projects

If you're referencing Bramble from another project (not working on Bramble itself), here's what to read:

- **`VISION.md`** — the design system reference: themes, colors, typography, icons, Penny brand guide, mobile patterns, CSS conventions. This is your primary source.
- **`src/app.css`** — exact OKLCH token values for each theme (copy these into your project)
- **`src/lib/styles/transitions.css`** — portable interaction CSS (press feedback, focus transitions). Works with any shadcn-svelte project — drop it in and import.

Everything below this section is for contributors working on Bramble itself.

---

## Tech Stack
- SvelteKit 2, Svelte 5, TypeScript
- shadcn-svelte (Bits UI) for components
- Tailwind 4 (inside components), CSS custom properties (theming)
- mode-watcher for light/dark toggle (Svelte 5 rune API — use `mode.current`, NOT `$mode`)
- Iconify Solar icons, Fontsource fonts

## Themes
- Themes defined in `src/app.css` as CSS custom properties (OKLCH)
- Theme switching via `data-theme` attribute on `<html>`
- Each theme sets colors + font families
- Currently: `lagoon` (default, Catppuccin-based), `meadow` (Desert-based)
- Adding a theme: add `html[data-theme="name"]` + `.dark` blocks in app.css, add entry to `src/lib/themes.ts`

## Conventions
- Use `data-section`, `data-component`, `data-action`, `data-state` attributes on HTML elements
- Heading font: `font-serif` class, body: `font-sans`, code: `font-mono`
- Safari/WebKit is first-class — test CSS features for Safari support before using
- Dark mode selectors must be compound: `html[data-theme="name"].dark` (no space before `.dark`)

## Component Architecture
shadcn-svelte files in `$ui/` are **never modified**. Customizations use two layers:

1. **`src/lib/styles/transitions.css`** — interaction behavior (press, transitions) applied via `[data-slot]` selectors. Portable to any shadcn-svelte project.
2. **Wrapper components in `$lib/components/`** — color/variant overrides (e.g. `Button.svelte`, `Toggle.svelte`). Import these instead of `$ui/` originals.

Components without wrappers are imported directly from `$ui/` (Card, Badge, Input, etc.).

**`shadcn add` is safe** — it only touches `$ui/` files, which we don't customize. Never pass `--overwrite` unless you want to reset a component to defaults.

## Development
```bash
pnpm dev          # dev server
pnpm build        # production build
pnpm check        # type checking
```

## Docker
Multi-platform build (linux/amd64, linux/arm64). Node adapter, port 3000.

CI: `.github/workflows/docker.yml` builds and pushes to `ghcr.io/noahkiss/bramble:latest` on every push to main.

## Key Files
- `src/app.css` — theme definitions (all CSS custom properties)
- `src/lib/styles/transitions.css` — shared interaction behavior (portable)
- `src/lib/components/Button.svelte` — button wrapper with color overrides
- `src/lib/components/Toggle.svelte` — toggle wrapper with color overrides
- `src/lib/themes.ts` — theme metadata for UI
- `src/routes/+layout.svelte` — shell with theme/mode switcher
- `src/routes/+page.svelte` — component showcase
- `VISION.md` — full design philosophy and brand guide
