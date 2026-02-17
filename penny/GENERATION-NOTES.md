# Penny — Generation Notes

Findings from image generation sessions. Reference for future prompt work.

## Round 1 — Establishing Default Penny (2026-02-16)

### Backend Comparison: Gemini vs OpenAI

**Test:** Same text-only prompt through both backends (no reference image).

| | Gemini | OpenAI |
|---|---|---|
| Style fidelity | Closer to storybook/watercolor. More defined pencil lines. | Softer, more painterly. Greeting-card cute. |
| Character accuracy | Better hedgehog proportions, distinct quill texture | More generic — could be any round animal |
| Detail | More facial detail, visible cheeks, rosy blush | Simpler, bigger smile, less nuance |

**Test:** Same edit prompt (remove glasses/bowtie from reference image).

| | Gemini | OpenAI |
|---|---|---|
| Faithfulness | Very faithful — same pose, same proportions | Changed the pose slightly, lost detail |
| Style preservation | Maintained watercolor/pencil style | Softer, different line quality |
| Accessory removal | Clean, natural-looking | Clean, but altered surrounding areas |

**Verdict:** Gemini `/edit` is the best tool for Penny work. Best at preserving character consistency and art style from reference images.

### Approach Comparison

| Approach | Style Fidelity | Angle Variety | Consistency |
|---|---|---|---|
| Gemini `/edit` single ref | Best | Low (same-angle bias) | Best |
| Gemini `/edit` character sheet | Good | Better | Good (sometimes leaks sheet into output) |
| Gemini `/nanobanana` multi-ref | Drifts — softer, more generic | Good | OK |
| OpenAI edit multi-image | Different style entirely | Good | Poor for Penny |

**Winner: Gemini `/edit` from single reference** for style fidelity. Character sheet as input when angle variety matters, with explicit "output only the new pose" instruction.

### Prompt Learnings

1. **Reference image > text description.** Text-only prompts produce hedgehogs that don't look like Penny. Always use a reference.

2. **Edit from reference > generate from scratch.** Starting from an existing Penny image and editing the pose/accessories produces much more consistent results.

3. **Don't over-specify eye detail.** Prompting for "visible white sclera" causes wide-eyed/startled expressions. The eyes look most natural when NOT explicitly prompted — let the model infer from the reference.

4. **Gemini gravitates to the source angle.** When editing from a single image, most outputs default to similar compositions. The character sheet mitigates this somewhat.

5. **Specify facing direction.** "Facing right" produces forward-motion energy. Flipping images with ImageMagick (`-flop`) is a reliable fallback.

6. **Anthropomorphize movement.** Without explicit instruction, Gemini defaults to naturalistic hedgehog movement (all fours). Specify "walking upright on two legs."

7. **No whiskers.** Gemini sometimes adds them. Explicitly exclude.

8. **Don't mention watercolor in edit prompts.** When editing, saying "watercolor" can shift the style away from the original. The style carries forward from the reference image — just say "same art style."

### File Organization

```
docs/penny/
  PENNY.md                    — character bible, prompt templates
  GENERATION-NOTES.md         — this file
  character-sheet.png         — composite of all canonical poses (use as reference)
  reference/                  — original source images from TinyLedger
    nerdy-sitting.png
    nerdy-sitting-transparent.png
  poses/                      — all canonical Penny poses (numbered sequentially)
    01-sitting.png            — Round 1: Default poses
    02-peeking.png
    03-walking.png
    04-sleeping.png
    05-reading.png
    06-explorer.png
    07-cozy.png               — Round 2: Look variants
    08-cozy-v2.png
    09-sporty.png
    10-professional.png
    11-hiking.png
    12-hiking-v2.png
    13-geek.png
    14-sleeping-v2.png
    15+                       — Round 3: Activity scenarios (see below)
  generated/                  — raw generation output (emptied after curation)
```

## Round 2 — Look Variants (2026-02-16)

### Approach

Used **Gemini `/edit` with character sheet** as input for all generations. This was the clear winner from Round 1 for balancing style fidelity with pose variety.

### Batch Generation Process

Created a reusable `generate.sh` script pattern:

1. Source API key from 1Password Connect
2. Define a base prompt + per-variant scene description + suffix
3. Loop through variants, running `/edit character-sheet.png "full prompt"` for each
4. Copy newest `nanobanana-output/*.png` to target filename after each generation

This pattern generates ~1 image per minute. Running 2 per variant gives options to curate from.

### Prompt Structure That Works

The winning prompt formula (high consistency, ~80% keeper rate):

```
[IDENTITY] This is a character reference sheet for a baby hedgehog named Penny.
Using the exact same character shown — same proportions, same face, same art
style, same coloring — generate a SINGLE NEW IMAGE of just this one character.

[SCENE] She is [detailed activity description with specific props and posture].
[Expression description]. [Posture note: "standing upright on two legs" when needed].

[GUARDRAILS] No whiskers. Output ONLY the new single pose on a white background.
Do NOT include the reference sheet or any of the original poses. Just one hedgehog
in one new pose, filling the frame.
```

**Key elements:**
- "Same proportions, same face, same art style, same coloring" — hammers consistency
- "SINGLE NEW IMAGE of just this one character" — prevents sheet leakage
- Specific props and posture in the scene description — gives Gemini concrete targets
- "Upright on two legs" — required for any standing/walking pose or Gemini defaults to all fours
- "Filling the frame" — keeps the output zoomed in on Penny, not a wide scene

### Variants Generated

| Variant | Prompt Summary | Keepers |
|---------|---------------|---------|
| Cozy | Scarf, blanket, steaming mug, warm expression | 2/2 |
| Sporty | Basketball, headband, sneakers, athletic pose | 1/2 |
| Professional | Clipboard, confident stance | 1/2 |
| Explorer/Hiking | Backpack, hiking boots, compass | 2/2 |
| Geek | Laptop, headphones, coding session | 1/2 (needed laptop lid fix) |
| Sleeping | Curled in ball, peaceful | 1/2 |

**8 of 12 kept** — 67% keeper rate. Higher quality than Round 1 experiments.

### Post-Processing

- **Geek laptop fix:** The laptop back showed code like a monitor. Used `/edit` on the output to fix the lid to metallic shell + replace Apple logo with pinecone emblem. Worked in one pass.
- **Naming:** Curated images moved to `poses/` with sequential `NN-name.png` naming.

### New Learnings

9. **Batch scripts are reliable.** The sequential generate-and-rename pattern works well. Gemini occasionally gives odd text responses ("try again with correct filename") but still produces unique output images.

10. **Character sheet > single ref for variants.** When adding accessories/props that don't exist in any single reference, the character sheet gives Gemini more angles to work from. Every variant came out on-model.

11. **Two generations per variant is the sweet spot.** Gives enough options to curate without wasting API calls. ~67% keeper rate means most come out usable.

12. **Post-edit fixes work.** Running `/edit` on a generated image to fix specific details (laptop lid, logos) produces clean results without disrupting the rest of the image.

## Round 3 — Activity Scenarios (2026-02-16)

Same approach as Round 2. Seven new activity-based poses using the character sheet + batch script.

| Scenario | Prompt Summary | Keepers |
|----------|---------------|---------|
| Gardening | Planting seedling, watering can | 2/2 |
| Celebrating | Jumping, confetti, arms raised | 2/2 |
| Building | Workbench, hammer, wood pieces | 2/2 |
| Painting | Easel, brush, palette | 2/2 |
| Stargazing | Lying on back, telescope, looking up | 2/2 |
| Cooking | Apron, stirring pot, wooden spoon | 1/2 |
| Yoga | Cross-legged meditation, eyes closed | 1/2 (1 was dupe) |

**12 of 13 unique kept** — ~92% keeper rate. The white-background + activity prompt formula is extremely reliable.

### New Learnings

13. **Activity prompts work better than accessory prompts.** Describing what Penny is *doing* (gardening, building, painting) produces more varied and natural results than describing what she's *wearing*.

14. **Gemini can occasionally duplicate output.** Yoga-2 was byte-identical to yoga-1. The Gemini session can get confused on longer runs — appears to replay a cached result. Running each generation as a fresh `gemini` invocation helps but doesn't eliminate this.

## Round 4 — Themed Scenes & Hoglets (2026-02-17)

### Hoglets (Penny with babies)

Inspired by the children's book "A Little Hedgehog" — mama Penny with tiny hoglets who "slept and nuzzled and grew."

**Prompt approach:** Same character sheet reference + a new guardrail block for hoglets:

```
[IDENTITY] Same as standard.

[SCENE] Penny with [2-3] tiny hoglets [activity]. [Emotional tone].
[Background: soft cream].

[GUARDRAILS] No whiskers. Keep the same art style — soft pencil lines,
gentle shading. The hoglets should be tiny versions of Penny, same coloring
but smaller and rounder. Do NOT include the reference sheet. Just one scene
filling the frame.
```

**Key differences from standard prompts:**
- Explicitly describe hoglets as "tiny versions of Penny, same coloring but smaller and rounder"
- "Soft pencil lines, gentle shading" — reinforces the art style since multi-character scenes can drift
- Cream background instead of white — warmer, more storybook feel

| Scenario | Prompt Summary | Keepers |
|----------|---------------|---------|
| Sleeping | Curled up in nest, hoglets nuzzled against belly | 1/2 |
| Nuzzling | Hoglets nuzzling against Penny, loving expression | 1/2 |
| Growing | Hoglets taking first wobbly steps, Penny watching | 1/2 |
| Reading | Bedtime story, hoglets in lap | 1/2 |

**4 of 8 kept** — 50% keeper rate. Multi-character scenes are harder to get right — the hoglets sometimes lose Penny's proportions or style. But the keepers are very charming.

### Themed Scenes (Lagoon & Meadow)

First attempt at scene-background images (not white/cream backgrounds). Two categories: wide banners (3:1) and square scenes (1:1).

**Prompt approach — shorter is better for scenes:**

```
Same character as reference sheet. Penny [activity in scene].
[1-2 color hex codes from theme palette]. [Mood/lighting].
[Format: "Wide horizontal 3:1 banner format" or "Square 1:1 composition"].
No whiskers. One scene, no reference sheet in output.
```

This is significantly shorter than the standard pose prompt. Why:
- Scene descriptions add length; the identity block must shrink to compensate
- "Same character as reference sheet" is sufficient — the character sheet does the heavy lifting
- Theme colors as hex codes in the scene description guide the palette without being verbose
- Aspect ratio as a simple instruction at the end

#### Lagoon Theme (Catppuccin palette)

Colors used: `#89b4fa` (blue), `#f5c2e7` (pink), `#b4befe` (lavender), `#1e1e2e` (navy), `#94e2d5` (teal)

| Type | Scene | Keepers |
|------|-------|---------|
| Banner | Dock over twilight water, blue/pink reflections | 1/2 |
| Banner | Reading in window nook, lavender lighting, rain | 1/2 |
| Banner | Bioluminescent forest, blue/teal glow | 1/2 |
| Banner | Hilltop aurora, navy sky | 1/2 |
| Banner | Tending garden, lavender/blue flowers | 1/2 |
| Square | Cozy blue/lavender room, pink pillows | 1/2 |
| Square | Peeking over pond, teal lily pads | 1/2 |

**7 of 14 kept** — 50% keeper rate.

#### Meadow Theme (Desert palette)

Colors used: `#d4a574` (sandstone), `#8b7355` (golden brown), `#c4956a` (copper)

| Type | Scene | Keepers |
|------|-------|---------|
| Banner | Golden wheat fields at sunset | 1/2 |
| Banner | Sandstone archway, wildflowers | 1/2 |
| Banner | Sunlit forest path, autumn leaves | 1/2 |
| Banner | Picnic on hillside, golden hour | 1/2 |
| Banner | Desert garden, terracotta pots | 1/2 |
| Square | Among sunflowers, golden light | 1/2 |
| Square | Reading under oak tree, autumn leaves | 1/2 |

**7 of 14 kept** — 50% keeper rate.

### Operational Learnings

15. **Gemini sessions can stall on long batch runs.** After ~25 sequential generations, the session hung on one image (generating multiple internal attempts without returning). Fix: kill and restart for the remaining images. Consider breaking batches at ~20 images.

16. **50% keeper rate for scenes vs 67-92% for white-background poses.** Scenes have more variables (background composition, lighting, color integration) that can go wrong. The 2-per-prompt strategy is essential for scenes.

17. **Hex colors in prompts work.** Including 2-3 hex codes from the theme palette produces images that feel on-theme. Don't overload with all colors — pick the 2-3 most distinctive.

18. **Aspect ratio hints are inconsistent.** "Wide horizontal 3:1 banner format" sometimes produces wider images, sometimes not. The `/edit` command inherits the input image dimensions, which limits aspect ratio control. Future approach: generate at default ratio, then crop/extend with ImageMagick for exact banner dimensions.

19. **Shorter scene prompts outperform longer ones.** The verbose Round 4 v1 prompts (identity block + colors block + format block + guardrails) caused Gemini to lose focus. The condensed v2 format ("Same character as reference sheet. [Scene]. [Colors]. [Format]. No whiskers.") worked reliably.

## Keeper Rate Summary

| Round | Type | Kept | Total | Rate |
|-------|------|------|-------|------|
| 2 | White bg + accessories | 8 | 12 | 67% |
| 3 | White bg + activities | 12 | 13* | 92% |
| 4 | Hoglets (cream bg) | 4 | 8 | 50% |
| 4 | Themed scenes | 14 | 28 | 50% |
| **All** | | **38** | **61** | **62%** |

*Round 3 had 1 duplicate, so 13 unique of 14.

## File Organization

```
docs/penny/
  PENNY.md                    — character bible, prompt templates
  GENERATION-NOTES.md         — this file
  character-sheet.png         — composite of 6 default poses (primary generation input)
  reference/                  — original source images from TinyLedger
    nerdy-sitting.png
    nerdy-sitting-transparent.png
  poses/                      — curated white-background poses (26 images)
    01-06                     — Round 1: Default poses (sitting, peeking, walking, sleeping, reading, explorer)
    07-14                     — Round 2: Look variants (cozy, sporty, professional, hiking, geek, sleeping-v2)
    15-26                     — Round 3: Activities (gardening, celebrating, building, painting, stargazing, cooking, yoga)
  generated/round-4/          — curated themed scenes + hoglets (18 images)
    hoglets-*.png             — Penny with baby hedgehogs (4 scenes)
    lagoon-banner-*.png       — Lagoon theme wide banners (5 scenes)
    lagoon-square-*.png       — Lagoon theme square scenes (2 scenes)
    meadow-banner-*.png       — Meadow theme wide banners (5 scenes)
    meadow-square-*.png       — Meadow theme square scenes (2 scenes)
```
