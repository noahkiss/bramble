<!-- TODO: 3:1 banner image with Penny + Bramble branding -->
<!-- ![Bramble](static/brand/hero-banner.png) -->

<h1 align="center">Bramble</h1>

<p align="center"><em>A personal design system, component showcase, and brand guide.</em></p>

<p align="center">
  <a href="#overview">overview</a> ·
  <a href="#themes">themes</a> ·
  <a href="#components">components</a> ·
  <a href="#penny">penny</a> ·
  <a href="#mobile">mobile</a> ·
  <a href="#develop">develop</a>
</p>

---

## Overview

Bramble is the source of truth for how things look, feel, and behave across all projects. It's a living style guide built with SvelteKit and shadcn-svelte — browse real components with real themes applied, switch palettes on the fly, and reference patterns for mobile-native feel.

<!-- TODO: screenshot of the component showcase with theme switcher -->

## Themes

Multiple switchable color palettes, each with its own font pairings and personality.

**Lagoon** — clean, polished, slightly formal. For dashboards, financial tools, and productivity apps. Pairs Syne headings with Inter body text.

**Meadow** — warm, earthy, small-town cozy. For community apps, personal tools, and life management. Pairs Lora headings with Nunito Sans body text.

<!-- TODO: side-by-side screenshot of both themes -->

Themes are pure CSS custom properties — switch instantly, no page reload.

## Components

shadcn-svelte components with our themes applied. Buttons, cards, dialogs, forms, navigation, data display, and more. Each component shows all variants across all themes.

<!-- TODO: screenshot of a few key components -->

## Penny

Penny the Hedgehog is the mascot across all projects. Bramble documents her identity — base character traits, look variants (nerdy, cozy, sporty), poses, and guidelines for generating consistent images of her across different contexts and color palettes.

See [VISION.md](VISION.md) for the full brand guide.

## Mobile

iOS-native-feeling patterns documented as reusable guidelines. Bottom tab bars, safe area handling, touch targets, spring animations, PWA configuration, and standalone mode detection.

## Develop

```bash
# Prerequisites: Node.js via fnm
fnm use --install-if-missing

# Install dependencies
pnpm install

# Dev server
pnpm dev

# Build
pnpm build

# Docker
docker build -t bramble .
docker run -p 3000:3000 bramble
```

---

<p align="center">
  <sub>Built with SvelteKit + shadcn-svelte.</sub>
</p>
