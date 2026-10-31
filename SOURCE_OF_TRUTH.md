# Duck Pond Idle 2 — Source of Truth

> **Project status:** Concept and visual/gameplay foundation  
> **Target:** Mobile-first browser idle/collection game, playable in iPhone Safari  
> **Repository:** https://github.com/brxceOg/Duck-Pond-Idle-2

This document is the canonical reference for the game's identity, player experience, core systems, and implementation priorities. When future requests conflict with this document, follow the user's newest explicit direction and update this document to match.

## 1. Game identity

**Duck Pond Idle 2** is a cute, character-driven rubber-duck collecting idle game. The player builds a lively little pond habitat populated by sentient rubber ducks with distinct silhouettes, personalities, sizes, and animations. Ducks are collected through a whimsical gumball-machine-style capsule roller, then placed into a framed habitat where they waddle, idle, interact, and make the pond feel alive.

The game should feel like a charming toy collection brought to life—not a spreadsheet, generic idle-game template, or flat menu simulator.

### Core fantasy
- Discover a mysterious new rubber duck from a colorful capsule machine.
- Add it to a growing flock of expressive, living toy characters.
- Watch the ducks inhabit a little world with their own idle behaviors.
- Earn and spend progression resources to improve the pond, collection, and future discoveries.
- Gradually turn a simple pond into a bustling, personality-filled duck sanctuary.

## 2. Core screen composition

The habitat is a persistent, visually framed play area and the emotional centerpiece of the game.

### Habitat / pond display
- Present the pond inside a clearly defined frame, like a little living diorama or toy display.
- The habitat should remain visible while the player uses collection, upgrade, and inventory menus whenever the viewport allows.
- The habitat is not a battle lane and ducks do not fight by default. The Battle Cats reference is about the readable framed play-area composition and the feeling of watching characters live in a dedicated space—not combat mechanics.
- Ducks should be visible at a glance, with enough room to recognize their shapes and animations.
- The pond should have depth, shoreline details, water movement, plants, lily pads, small props, and subtle environmental motion.
- Add small ambient events and duck-to-duck moments so the scene feels inhabited rather than like a static roster display.

### Responsive layout
- On wider screens, use a side-by-side composition: the framed pond remains on one side while the primary game interface occupies the other.
- On narrow iPhone portrait screens, preserve the same hierarchy without shrinking everything into unreadable columns. Use a compact, persistent habitat panel near the top or a carefully designed split/stacked layout, with menus below it.
- Keep the habitat present during normal play; a menu may temporarily expand, but it should not make the ducks feel like a separate screen or disconnected feature.
- Respect iPhone safe areas, browser viewport changes, touch targets, and vertical scrolling.

## 3. Main gameplay loop

1. **View the habitat.** The player sees their current ducks living in the pond.
2. **Collect capsules.** The player visits a gumball-machine-inspired duck capsule roller.
3. **Reveal a duck.** A capsule rolls, opens, and reveals a duck with a satisfying anticipation-and-reveal sequence.
4. **Add to the flock.** The new duck joins the habitat and begins its idle routine.
5. **Progress.** The player earns the game's resources and invests in upgrades, collection growth, and habitat improvements.
6. **Return and discover.** The player checks on the pond, gathers progress, and rolls for more ducks.

The exact currency names, roll prices, rarity rates, duplicate rules, offline progression, and upgrade economy are **not yet locked**. Do not silently invent final balance values; propose them as a design pass before implementation.

## 4. Duck collection and capsule machine

The capsule machine is the primary collection interface and should be a major visual attraction.

- Build a recognizable gumball/capsule machine that visibly contains colorful duck capsules.
- The machine should feel tactile and toy-like: rounded glass dome, colorful capsules, a sturdy base, a crank or button, and a clear collection/reveal area.
- Rolling should have anticipation: capsule movement, mechanical bounce/rattle, a selected capsule dropping, opening, and a duck reveal.
- The reveal should give the duck a moment in the spotlight before it joins the habitat.
- Each duck is a distinct collectible character, not simply a recolor. Different ducks can vary by body scale, head/body proportions, beak, accessories, markings, colors, expression, and personality.
- The collection interface should clearly communicate what the player is spending and what kind of roll they are making. Exact roll tiers and odds remain a future balancing decision.
- Duplicate handling, rarity tiers, guarantees/pity, and collection completion rewards are future design decisions; document them before coding them.

## 5. Sentient rubber ducks

All ducks share a recognizable base archetype, but each should feel like a character.

### Base archetype
Use the supplied reference image as the starting visual guide:
- Bright, glossy yellow rubber-duck body.
- Oversized rounded head and compact, plump body.
- Large expressive dark eyes with bright catchlights.
- Bold orange-to-red beak with a friendly, readable shape.
- Small rounded wings and a simple duck tail.
- Warm blush/cheek accents where appropriate.
- Thick, dark burgundy-brown cartoon outlines.
- Smooth, soft highlights and warm shaded gradients.
- Cute, cheerful, toy-like proportions.

The reference is a direction guide, not an asset to reproduce. Create original artwork for the game; do not include its watermark or copy a stock image.

### Character differentiation
- Vary overall scale and proportions, not only color.
- Give each duck a clear silhouette that remains readable at small mobile sizes.
- Use accessories, markings, beak shapes, facial expressions, and body shape to establish identity.
- Ducks should feel sentient through eye direction, blinking, head tilts, tiny reactions, waddles, and interactions.
- A duck's rarity or value should not be communicated only through a colored border; its design should feel special.

### Animation baseline
Every duck should have a small set of layered, reusable animations:
- Idle bob / gentle breathing.
- Blink and occasional eye movement.
- Waddle walk with body sway.
- Turn / change direction.
- Short hop or excited reaction.
- Contextual interactions such as looking at another duck, investigating a prop, or resting.
- Entry animation when first joining the pond.

Animations must remain smooth, readable, and lightweight on mobile browsers. Avoid excessive motion that makes the habitat visually noisy.

## 6. Pond life and habitat behavior

The pond should feel like a small living diorama:
- Gentle looping water movement and occasional ripples.
- Ducks choose destinations and waddle around the available habitat.
- Ducks should avoid overlapping one another and major props.
- Ducks should stay within the visible habitat bounds.
- Lily pads, reeds, flowers, stones, and small decorations add scale and personality.
- Occasional ambient moments—such as a duck pausing, looking around, stretching, or reacting to a nearby duck—make the flock feel alive.

Behavior should be deterministic enough to avoid jitter, teleporting, clipping, or constant direction changes. Movement should have clear start, travel, and settle phases. The pond is a home space first; do not add combat or hostile encounters unless the user explicitly asks for them.

## 7. Progression and menus

The menus should feel like physical, lovingly crafted parts of the toy world.

Planned interface areas:
- **Capsule Machine:** roll for new ducks.
- **Duck Collection / Flock:** inspect owned ducks and their details.
- **Upgrades:** improve idle earnings, collection access, habitat capacity, or other agreed systems.
- **Habitat / Decorations:** personalize the pond as this system is designed.
- **Settings:** audio, motion, save/reset, and accessibility controls.

The exact economy and menu inventory are not locked yet. Prioritize a small, understandable first playable loop over a large collection of empty tabs.

### Menu behavior
- Menus should not obscure the habitat more than necessary.
- Use clear hierarchy, tactile buttons, readable labels, and satisfying pressed/selected states.
- Keep controls comfortable for thumbs on iPhone.
- Avoid dense dashboards, tiny text, generic gradients, and default web-form styling.

## 8. Art and presentation rules

See [ART_SOURCE.md](ART_SOURCE.md) for the canonical visual direction.

High-level rules:
- 2D cartoon illustration with cute, friendly, character-first design.
- Soft, rounded shapes and expressive faces.
- Strong, consistent outlines and polished shading.
- Warm, playful color palette with enough contrast for mobile readability.
- Handcrafted, illustrated UI—not sterile computerized panels.
- The pond and ducks should share one coherent visual language.
- Avoid pixel art, flat placeholder shapes, generic AI-generated cozy-game clichés, and mismatched asset styles.

## 9. Technical and quality requirements

- Mobile-first browser game; iPhone Safari is a primary target.
- Responsive behavior must work in portrait and landscape orientations.
- Keep animations efficient and avoid unnecessary per-frame work.
- Use a consistent coordinate system for the habitat and keep all duck movement within its bounds.
- Separate game state, rendering, animation, and UI logic where practical.
- Save collection and progression reliably using browser storage; define a versioned save format before substantial progression is added.
- Do not ship placeholder buttons, fake menu actions, or nonfunctional interactions.
- Avoid regressions to existing working features when adding new systems.
- Test actual touch interactions and viewport behavior, not only desktop mouse input.

## 10. Development priorities

Build in this order unless the user changes priorities:

1. **Foundation and layout:** responsive screen composition, persistent framed pond, menu structure.
2. **Visual foundation:** original base duck artwork/style, pond frame, water, shoreline, and core UI components.
3. **Duck simulation:** spawn, idle, blink, waddle, turn, path selection, boundaries, and collision avoidance.
4. **Capsule machine:** machine presentation, roll interaction, capsule animation, reveal, and flock insertion.
5. **Collection and persistence:** owned ducks, duck details, save/load, and duplicate handling once designed.
6. **Progression:** economy and upgrades after the core loop feels good.
7. **Polish:** sound, ambient moments, accessibility, performance, and device testing.

## 11. Acceptance checklist

A milestone is not complete just because it renders once. Verify:
- The pond reads as a framed living play area.
- The ducks are cute, expressive, distinct, and consistent with the reference archetype.
- Ducks visibly idle and move naturally without jitter, overlap, or leaving the pond.
- The capsule machine communicates the collection fantasy and has a satisfying reveal.
- The player can understand the current action, cost, and result.
- Menus feel tactile and illustrated rather than like generic computer UI.
- The layout is usable on an iPhone without tiny controls or clipped content.
- All visible controls work, and saved progress survives a reload.

## 12. Open decisions

Do not assume these are finalized until discussed:
- Currency name(s), earning rate, roll cost, and upgrade prices.
- Rarity tiers, probabilities, roll variants, guarantees, and duplicate compensation.
- Starting duck roster and the first batch of collectible duck designs.
- Maximum visible ducks, habitat expansion, and duck placement controls.
- Offline progress and idle reward rules.
- Whether ducks have individual stats, moods, needs, or purely cosmetic personalities.
- Sound direction and accessibility options.
