# Bramble — Design System Vision

A personal design system, component showcase, and brand guide. Bramble is the source of truth for how things look, feel, and behave across all projects.

## What This Is

- **Living style guide** — browse components with real themes applied
- **Theme system** — multiple switchable palettes with per-theme font pairings
- **Brand guide** — Penny the Hedgehog identity, banner templates, prompt guidelines
- **Mobile patterns** — iOS-native-feeling patterns documented as reusable guidelines
- **Agent context** — structured so Claude (and humans) can reference it from any project

Hosted as a Docker container on Komodo. Public GitHub repo.

---

## CSS Philosophy

Tailwind is fine as **plumbing inside components** (shadcn-svelte handles this). It's also acceptable scattered lightly in app code for one-off layout tweaks. But the priority is:

1. **Components for reuse** — `<Button variant="primary">` over `class="bg-blue-500 text-white..."`. Components enforce consistency and are self-documenting.
2. **Design tokens for theming** — colors, fonts, radii, spacing defined as CSS custom properties. Change the tokens, the whole app updates.
3. **Semantic identification** — use `data-*` attributes so humans and agents can grep for intent:
   - `data-section="pricing"` — page sections
   - `data-component="feature-card"` — component instances
   - `data-action="submit-order"` — interactive elements
   - `data-state="empty"` — state indicators

The test: can someone read the markup and understand what each piece *does*, not just how it *looks*?

---

## Themes

### Architecture

Themes are sets of CSS custom properties in OKLCH color space (shadcn-svelte standard). Each theme defines colors, fonts, and radii. Switching themes swaps all variables at once via `data-theme` attribute on `<html>`.

Each theme includes:
- Light and dark mode variants
- Recommended heading + body font pairing
- Semantic color mapping (primary, secondary, accent, success, warning, error, etc.)

### Theme: Catppuccin (Primary)

Based on the Catppuccin palette (Latte for light, Mocha for dark). Clean, slightly formal, polished.

**Vibe:** Professional dashboard, financial tool, productivity app.

**Font pairing (recommended):**
- Heading: **Syne** — geometric, distinctive personality without being flashy
- Body: **Inter** — high x-height, excellent screen readability, tabular numbers for data
- Mono: **JetBrains Mono** — code blocks, technical content

**Color foundation:**
- Light: `#eff1f5` background, `#4c4f69` foreground
- Dark: `#1e1e2e` background, `#cdd6f4` foreground
- Primary: blue (`#1e66f5` light / `#89b4fa` dark)
- Accent: pink (`#ea76cb` light / `#f5c2e7` dark)

(Full OKLCH token definitions in the codebase.)

### Theme: Desert (Secondary)

Earthy, warm, small-town cozy. Inspired by desert landscapes, aged paper, and local coffee shops.

**Vibe:** Community app, personal journal, cozy life tools, Cleaver Manor.

**Font pairing (recommended):**
- Heading: **Lora** — warm serif with calligraphic roots, literary feel
- Body: **Nunito Sans** — soft, rounded, friendly without being childish
- Mono: **JetBrains Mono** — consistent across themes

**Color foundation:** (to be refined during implementation)
- Warm tans, terracotta, sage green, dusty rose
- Muted earth tones with intentional pops of warmth
- Think: sandstone, dried herbs, sunset ochre

### Future Themes

The system is extensible. Add a new `html[data-theme='name']` block with the full variable set. Possible future directions:
- Fallout/retro-terminal (green phosphor, amber CRT)
- Ocean/nautical
- Forest/woodland

---

## Typography

Fonts are design tokens, not hardcoded. Each theme recommends a heading + body + mono pairing, but projects can override.

**Rules:**
- Body text: minimum 16px on mobile
- Line height: 1.5-1.75 for body
- Line length: 65-75 characters max
- Tabular numbers (`font-variant-numeric: tabular-nums`) for financial/numeric data
- Load via Fontsource CDN or self-host

**Font loading:**
```css
@import url('https://cdn.jsdelivr.net/fontsource/fonts/inter/index.min.css');
@import url('https://cdn.jsdelivr.net/fontsource/fonts/syne/index.min.css');
@import url('https://cdn.jsdelivr.net/fontsource/fonts/lora/index.min.css');
@import url('https://cdn.jsdelivr.net/fontsource/fonts/nunito-sans/index.min.css');
```

---

## Icons

Solar icon set via Iconify. Consistent across all projects.

```html
<script src="https://code.iconify.design/iconify-icon/3.0.0/iconify-icon.min.js"></script>
<iconify-icon icon="solar:settings-bold"></iconify-icon>
```

**Rules:**
- One variant style per project (bold, linear, or outline)
- Consistent sizing (24x24 default)
- No emojis as UI icons
- Brand logos from Simple Icons when needed

---

## Penny the Hedgehog — Brand Identity

### Base Character

Penny is a baby hedgehog in a children's book illustration style. She is the mascot across all projects, adapted to fit each project's personality.

**Core traits (always present):**
- Baby hedgehog, small and round
- Warm browns and tans (natural hedgehog coloring)
- Big, expressive eyes
- Soft, friendly expression
- Storybook illustration style — soft pencil lines, watercolor wash, gentle shading
- Beatrix Potter-esque aesthetic

**What changes per project:**
- Accessories (glasses, bowtie, hat, scarf, etc.)
- Pose and angle
- Color palette adaptation
- Context/setting

### Looks / Variants

| Look | Accessories | Used For |
|------|------------|----------|
| **Nerdy** | Round glasses + red polka-dot bowtie | TinyLedger, financial/data apps |
| **Sporty** | Headband, sneakers, or jersey | Fitness/activity apps |
| **Cozy** | Scarf, mug, blanket | Cleaver Manor, home/life apps |
| **Professional** | Tiny briefcase or clipboard | Productivity/business tools |
| **Explorer** | Backpack, compass, hiking boots | Adventure/travel apps |
| **Default** | None — just Penny being herself | Brand materials, favicon base |

### Poses & Angles

To avoid the "pasted in" look, maintain a library of reference images across:
- **Sitting** (current primary — relaxed, approachable)
- **Walking/trotting** (active, purposeful)
- **Peeking** (around a corner, over an edge — playful)
- **Waving** (welcoming, greeting)
- **Working** (at a tiny desk, reading, writing)
- **Sleeping/curled up** (404 pages, empty states, loading)

### Image Generation Guidelines

When generating new Penny images:
- Reference approved images for consistency
- Use the base character description + specific look
- Specify the project's color palette in hex codes
- Request watercolor/storybook style explicitly
- Avoid: photorealistic, 3D rendered, anime, flat vector styles
- Iterate: generate 3-4 variants, pick the ones that feel right

**Prompt template:**
```
A baby hedgehog character in children's book illustration style.
Soft pencil lines, watercolor wash, gentle shading.
Warm browns and tans, big expressive eyes, friendly expression.
[LOOK: wearing round glasses and a red polka-dot bowtie]
[POSE: sitting and looking at the viewer]
[SETTING: cozy desk with tiny books]
[PALETTE: use colors #1e1e2e, #89b4fa, #f5c2e7 as accents in the scene]
```

### Banner Image Standards

Project banners follow a consistent format:
- **Aspect ratio:** 3:1 (e.g., 1800x600)
- **Composition:** Penny on one side (usually right), project branding on the other
- **Background:** Uses the project's color theme (not white/generic)
- **Style:** Matches the storybook illustration aesthetic
- **Text:** Project name in the theme's heading font (added in post if needed)
- **Resolution:** 300 DPI for print, 72 DPI for web (provide both when possible)

### Palette Adaptation

Penny's core coloring (browns, tans) is neutral enough to sit in any palette. Adapt the *scene and accents* to match the project theme:
- **Catppuccin:** Cool blue/pink accents in the background, clean surfaces
- **Desert:** Warm sandstone setting, earth-tone props, golden light
- **Any theme:** Pull 2-3 accent colors from the theme into the scene's props/background

---

## Mobile Patterns (iOS-Native Feel)

Document patterns, not framework dependencies. These are CSS/HTML/JS guidelines for making web apps feel native on iOS.

### Bottom Tab Bar
- Height: 54px + `env(safe-area-inset-bottom)` for home indicator
- Backdrop blur for iOS glass effect
- Icon: 24px, label: 10px, one word max
- 3-5 tabs optimal
- Active state with theme primary color

### Safe Areas
- `viewport-fit=cover` in viewport meta tag
- `env(safe-area-inset-*)` for notch/home indicator padding
- Apply to headers (top), tab bars (bottom), fullscreen layouts (all sides)

### Touch Targets
- Minimum 44x44px (Apple HIG)
- 12px minimum spacing between interactive elements

### Animations & Transitions
- Page transitions: 300-500ms, slide preferred over fade on mobile
- Micro-interactions: 150-300ms
- Use `transform`/`opacity` for GPU acceleration
- Spring easing for playful feel: `cubic-bezier(0.34, 1.56, 0.64, 1)`
- Always respect `prefers-reduced-motion`

### PWA Meta Tags
```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
```

### Standalone Mode
- Detect with `window.navigator.standalone` (iOS) or `matchMedia('(display-mode: standalone)')`
- Adapt UI: hide browser-specific elements, adjust padding for status bar

---

## README Standards

Every project README follows a consistent layout:

1. **Banner image** — 3:1, includes Penny + project colors/branding
2. **Centered project name** — `<h1 align="center">Project Name</h1>`
3. **Centered tagline** — one sentence, italic
4. **Centered TOC** — `overview · themes · install · develop · license` format, short words, spaced with `·`
5. **Content sections** — standard markdown
6. **Screenshots** — at least 2-3 showing key views, captioned

---

## Tech Stack

- **Framework:** SvelteKit 2 + Svelte 5
- **Components:** shadcn-svelte (Bits UI underneath)
- **Styling:** Tailwind 4 (inside components) + CSS custom properties (theming)
- **Theme switching:** mode-watcher
- **Icons:** Iconify (Solar set)
- **Fonts:** Fontsource CDN
- **Build:** Vite, Node adapter
- **Deployment:** Docker (multi-platform: linux/amd64, linux/arm64), Komodo

---

## What Bramble Is Not

- Not a npm package others install (it's a reference + showcase)
- Not a copy of shadcn-svelte docs (it's *our* theme and patterns applied to those components)
- Not a generic template (it's opinionated toward our projects and preferences)
