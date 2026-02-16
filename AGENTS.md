# Bramble — Agent Instructions

Personal design system, component showcase, and brand guide.

## Tech Stack
- SvelteKit 2, Svelte 5, TypeScript
- shadcn-svelte (Bits UI) for components
- Tailwind 4 (inside components), CSS custom properties (theming)
- mode-watcher for light/dark toggle
- Iconify Solar icons, Fontsource fonts

## Themes
- Themes defined in `src/app.css` as CSS custom properties (OKLCH)
- Theme switching via `data-theme` attribute on `<html>`
- Each theme sets colors + font families
- Currently: `catppuccin` (default), `desert`
- Adding a theme: add `html[data-theme="name"]` + `.dark` blocks in app.css, add entry to `src/lib/themes.ts`

## Conventions
- Use `data-section`, `data-component`, `data-action`, `data-state` attributes on HTML elements
- Components from `$ui/` (shadcn-svelte), custom components in `$lib/components/`
- Heading font: `font-serif` class, body: `font-sans`, code: `font-mono`
- Safari/WebKit is first-class — test CSS features for Safari support before using

## Development
```bash
pnpm dev          # dev server
pnpm build        # production build
pnpm check        # type checking
```

## Docker
Multi-platform build (linux/amd64, linux/arm64). Node adapter, port 3000.

## Key Files
- `src/app.css` — theme definitions (all CSS custom properties)
- `src/lib/themes.ts` — theme metadata for UI
- `src/routes/+layout.svelte` — shell with theme/mode switcher
- `src/routes/+page.svelte` — component showcase
- `VISION.md` — full design philosophy and brand guide
