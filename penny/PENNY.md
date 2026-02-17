# Penny the Hedgehog — Character Bible

Penny is the mascot across all projects. This document is the source of truth for her visual identity.

## Reference Images

See `reference/` for canonical images. The primary reference is `nerdy-sitting-transparent.png` — Penny in her Nerdy look, sitting, isolated on transparent background.

## Physical Description

### Body
- **Shape:** Round and plump, almost egg-shaped when sitting. Baby proportions — head is large relative to body (roughly 40% of total height).
- **Size:** Small. When placed in scenes, she should look like she'd fit in your cupped hands.
- **Belly/front:** Cream to warm tan, smooth, lighter than the quills. Soft gradient from lighter center to slightly warmer edges.
- **Paws:** Small, simple, rounded shapes. Tan/light brown, slightly darker than the belly. Four visible when sitting (two front resting in lap area, two at base). No defined fingers/toes — just soft rounded ends.

### Quills
- **Coverage:** Fan out from the crown of her head backward and downward, covering the entire back and sides.
- **Color:** Medium brown base with darker brown tips. Some variation in individual quill shading gives texture.
- **Texture:** Rendered as individual fine strokes radiating outward. Not smooth or geometric — slightly messy, natural. Denser at the crown, looser at the edges.
- **Style note:** The quills should look hand-drawn, not patterned. Each one is a small brushstroke.

### Face
- **Shape:** Round, soft, framed by the quill line above and the cream belly below.
- **Eyes:** Large and round. Dark brown iris with **visible white sclera** around it — this is critical to Penny looking like Penny. Solid black dots with just a highlight look generic; the whites of her eyes must be visible. Prominent white highlight dots (usually upper-left of each eye) give life and warmth. Eyes are the most expressive feature — they carry the emotion.
- **Nose:** Tiny, dark brown/black, round. Centered, sits just above the mouth line.
- **Mouth:** Small, subtle. Usually a gentle closed-mouth smile — a soft curved line. Not toothy, not wide.
- **Cheeks:** Subtle rosy pink blush spots, soft-edged. Warm, not cartoonishly bright.
- **Ears:** Small, rounded, poking out from the quill line at the top-sides of the head. Same tan/brown as the face, slightly darker at the edges.
- **Eyebrows:** Very subtle — thin, short strokes above the glasses (when wearing them) or above the eyes. Expressive but not heavy.

### Expression
Default expression is warm, friendly, slightly shy. She looks like she's happy to see you but wouldn't interrupt. The combination of big eyes, small smile, and rosy cheeks creates approachability.

## Art Style

- **Medium:** Watercolor wash with soft pencil/ink lines
- **Line quality:** Thin, slightly imperfect, hand-drawn feel. Not crisp vector lines.
- **Shading:** Gentle, warm. Watercolor-style gradients, not hard shadows.
- **Palette:** Muted, warm. Browns, tans, creams. Even accent colors should feel like they belong in a storybook.
- **Reference artists:** Beatrix Potter, classic children's book illustrators. Cozy, not flashy.

## Looks / Variants

The base character stays the same. Only accessories and context change.

| Look | Accessories | Used For |
|------|------------|----------|
| **Default** | None — just Penny being herself | Brand materials, favicon base, Bramble |
| **Nerdy** | Round wire-frame glasses + red polka-dot bowtie | TinyLedger, financial/data apps |
| **Cozy** | Scarf, mug, blanket | Cleaver Manor, home/life apps |
| **Sporty** | Headband, sneakers, or jersey | Fitness/activity apps |
| **Professional** | Tiny briefcase or clipboard | Productivity/business tools |
| **Explorer** | Backpack, compass, hiking boots | Adventure/travel apps |
| **Geek** | Oversized headphones, laptop (pinecone logo on lid) | Dev tools, coding contexts |

### Nerdy Look Details
- **Glasses:** Round, thin wire frames. Circular lenses. Sit on the nose, slightly oversized for her face (cute effect). Dark brown/gunmetal frame color.
- **Bowtie:** Red with white/cream polka dots. Small, tied at the neck where quills meet belly. Classic butterfly bowtie shape.

## Poses

| Pose | Description | Use Cases |
|------|-------------|-----------|
| **Sitting** | Relaxed, slightly leaning, paws in front. Facing slightly left with head turned toward viewer. | Primary/default, avatars, social |
| **Peeking** | Peering around a corner or over an edge. Only head and one paw visible. | Playful UI elements, tooltips, empty states |
| **Waving** | One paw raised in greeting. Friendly, welcoming. | Onboarding, welcome screens, greetings |
| **Walking** | Trotting forward, purposeful but not rushed. | Active states, progress indicators |
| **Working** | At a tiny desk, reading, or writing. | Productivity contexts, loading states |
| **Sleeping** | Curled into a ball, quills out, peaceful. | 404 pages, maintenance mode, empty states |
| **Gardening** | Planting a seedling, watering can nearby. | Onboarding, "getting started", growth metaphors |
| **Celebrating** | Jumping with arms raised, confetti. | Success states, milestones, achievements |
| **Building** | At workbench with tiny hammer, crafting. | Under construction, building features, progress |
| **Painting** | At easel with brush and palette. | Creative/design contexts, customization |
| **Stargazing** | Lying on back, telescope nearby, looking up. | Roadmaps, "looking ahead", dreamy empty states |
| **Cooking** | Apron, stirring a pot, wooden spoon. | Warm/homey contexts, "cooking something up" |
| **Meditating** | Cross-legged, eyes closed, peaceful. | Loading states, patience, "taking a moment" |

## Theme Adaptation

Penny's core coloring (browns, tans, cream) is neutral and sits well in any palette. Adapt the **scene and accents** — not Penny herself — to match the project theme.

| Theme | Scene Treatment |
|-------|----------------|
| **Lagoon** (Catppuccin) | Cool blue/pink accents in background. Clean, minimal surfaces. Colors: `#89b4fa`, `#f5c2e7`, `#1e1e2e` |
| **Meadow** (Desert) | Warm sandstone setting, earth-tone props, golden light. Colors: `#d4a574`, `#8b7355`, `#c4956a` |

Pull 2-3 accent colors from the theme into the scene's props and background. Never recolor Penny herself.

## Prompt Templates

All prompts use **Gemini `/edit`** with `character-sheet.png` as input. This is the proven approach — best balance of character consistency and pose variety.

### Pose / Activity (white background) — ~80% keeper rate

Best for: standalone character poses, app-specific illustrations, UI elements.

```
This is a character reference sheet for a baby hedgehog named Penny.
Using the exact same character shown — same proportions, same face,
same art style, same coloring — generate a SINGLE NEW IMAGE of just
this one character.
She is [detailed activity with specific props and posture].
[Expression]. [Posture: "standing upright on two legs" if needed].
No whiskers. Output ONLY the new single pose on a white background.
Do NOT include the reference sheet or any of the original poses.
Just one hedgehog in one new pose, filling the frame.
```

**Example (gardening):**
> She is kneeling on the ground planting a small seedling in a tiny pot, with a miniature watering can beside her. Gentle, nurturing expression. Upright posture, on two legs.

### Themed Scene (background) — ~50% keeper rate

Best for: banners, hero images, README headers, marketing material.

**Keep it short.** Longer scene prompts cause Gemini to lose focus. The character sheet carries the identity — just describe the scene.

```
Same character as reference sheet. Penny [activity in scene].
[2-3 hex colors from theme]. [Mood/lighting].
[Format: "Wide horizontal 3:1 banner format" / "Square 1:1 composition"].
No whiskers. One scene, no reference sheet in output.
```

**Example (Lagoon banner):**
> Same character as reference sheet. Penny sitting on a wooden dock over calm twilight water. Cool blue #89b4fa and pink #f5c2e7 reflections. Moonlight. Wide horizontal 3:1 banner format. No whiskers. One scene, no reference sheet in output.

**Example (Meadow square):**
> Same character as reference sheet. Penny sitting among tall sunflowers in warm golden light. Rich amber and golden #8b7355 tones. Square 1:1 composition. No whiskers. One scene, no reference sheet in output.

### Hoglets (Penny with babies) — ~50% keeper rate

Best for: personal/family use, children's storybook feel, warming brand moments.

```
This is a character reference sheet for a baby hedgehog named Penny.
Using the exact same character shown — same proportions, same face,
same art style, same coloring — generate a SINGLE NEW IMAGE.
Penny is [scene with hoglets]. [Emotional tone].
[Background: soft cream / themed].
No whiskers. Keep the same art style — soft pencil lines, gentle
shading. The hoglets should be tiny versions of Penny, same coloring
but smaller and rounder. Do NOT include the reference sheet.
Just one scene filling the frame.
```

**Example (sleeping):**
> Penny is curled up in a cozy nest of soft blankets with three tiny hoglets nuzzled against her belly. They are all sleeping peacefully together, the hoglets tucked in close. Warm, tender scene on a soft cream background.

### Critical Details for All Prompts

- **Don't over-specify eyes** — prompting for "visible white sclera" causes wide-eyed/startled looks. Let the model infer from the reference.
- **No whiskers** — Gemini sometimes adds them. Always explicitly exclude.
- **Don't say "watercolor"** — the style carries from the reference. Saying "watercolor" can shift the look.
- **"Filling the frame"** / **"one scene"** — prevents the reference sheet from leaking into output.
- **Anthropomorphized movement** — specify "upright on two legs" for any standing/walking pose.
- **Facing direction** — specify left/right when it matters. "Facing right" implies forward motion.
- **Activity > accessories** — describing what Penny is *doing* produces better results than what she's *wearing*.
- **2-3 hex colors max** for themed scenes — more can overwhelm the prompt.
- **Shorter scene prompts** outperform longer ones — trust the character sheet for identity.

### Batch Generation

Use the `generate.sh` script pattern (see `generated/` dirs for examples):
1. Source API key, set `NANOBANANA_MODEL`
2. Loop variants with 2 generations each (sweet spot for curation)
3. Copy newest `nanobanana-output/*.png` to named target after each generation
4. Keep batches under ~20 sequential runs to avoid Gemini session stalls

Expected keeper rates: ~80-90% for white-bg poses, ~50% for scenes/hoglets.

## Generation Notes

See `GENERATION-NOTES.md` for backend comparison findings, keeper rate data, and prompt iteration history across all rounds.
