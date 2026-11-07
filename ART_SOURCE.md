# Duck Pond Idle 2 — Art Source & Visual Direction

> **Purpose:** Canonical visual reference for all original game art, UI, animation, and presentation.  
> **Primary target:** Cute, polished 2D cartoon art for a mobile browser game.

## 1. Overall art identity

The game should look like a lovingly illustrated rubber-duck toy collection. The desired feeling is cute, warm, bright, expressive, and immediately readable—taking broad inspiration from the friendly character appeal and soft visual language of Hello Kitty-style character worlds without copying any specific character, brand assets, or proprietary designs.

The art should feel authored and cohesive. It must not look like a collection of unrelated AI images, generic idle-game assets, or flat vector placeholders.

**Keywords:** glossy toy, rounded, expressive, cheerful, soft shading, bold outline, charming, collectible, storybook polish, tactile interface.

## 2. Duck reference archetype

The user-approved isolated rubber-duck sprite is the canonical base archetype for every collectible. All ducks must use the same toy silhouette, proportions, face placement, beak shape, wing shape, and outline.

### Defining visual traits
- Plump, rounded, bright-yellow rubber duck.
- Large rounded head that flows naturally into a compact body.
- Large, glossy dark eyes with white highlights.
- Wide, orange-red beak with a friendly, expressive shape.
- Small wing shapes integrated into the body.
- Warm orange shading around the lower body and edges.
- Soft white specular highlights that make the duck look like shiny molded rubber.
- Thick, dark burgundy-brown outer contour and confident internal linework.
- Optional soft cheek blush for extra personality.

### Proportion and expression
- The head should be large enough to carry the character's expression.
- The body should feel chunky and buoyant, not thin or anatomically realistic.
- Eyes should remain legible at the smallest gameplay size.
- The beak is a signature feature and should have a clear silhouette.
- Keep expressions simple and emotionally readable: happy, curious, sleepy, surprised, smug, bashful, excited.

### Important asset rule
Use only the user-approved isolated transparent sprite archetype and the original game-made variations derived from it. Do not ship the yellow reference background, stock watermark, or ground shadow. Keep the sprite background fully transparent. The reference is a visual direction; do not reintroduce stock-image branding.

## 3. Duck family design system

Every collectible duck must belong to the same visual family while remaining individually recognizable.

Differentiate ducks using the approved shared rubber-duck sprite archetype only. Keep the silhouette, head/body proportions, face, beak, wing, and outline identical across the entire roster. Individual ducks may vary by body color, glossy finish, and a small molded-toy detail or accessory that does not alter the underlying anatomy. Higher-rarity ducks must each receive their own distinct treatment while remaining unmistakably the same kind of rubber duck. Never turn a collectible into another bird species or change its anatomy.

### Size readability
Large and small ducks must feel meaningfully different in the pond. Preserve clear outlines and readable facial features at every scale. Do not scale down so far that eyes and beaks disappear.

## 4. Linework, shading, and materials

### Outlines
- Use a consistent dark burgundy, plum-brown, or warm near-black outline.
- Outer contours should be continuous and fully enclose each character.
- Internal linework should be slightly lighter or thinner than the outside contour.
- Avoid hairline strokes that disappear on phone screens.
- Avoid inconsistent outline widths between ducks, props, and UI illustrations.

### Shading
- Use soft, rounded gradients and painted-looking shadow transitions.
- Place bright specular highlights on curved rubber surfaces.
- Add warm reflected light and subtle contact shadows where they help establish volume.
- Keep the rendering polished but simple enough to read at small sizes.
- Avoid harsh metallic reflections, plastic 3D rendering, or noisy texture.

### Material language
Rubber ducks should look like glossy molded bath toys. Water should look soft, clean, and inviting. Wood, ceramic, paper, fabric, and plants should each have their own subtle material cues in the interface and habitat.

## 5. Palette direction

Use a warm, playful palette anchored by:
- Sunny rubber-duck yellow.
- Tangerine and coral-orange accents.
- Deep burgundy / plum-brown outlines.
- Creamy whites for highlights and interface surfaces.
- Fresh pond greens, aqua, and blue-green water.
- Soft pinks and pastel accent colors for selected characters and decorations.

Colors should be vivid enough to feel joyful, but not fluorescent or visually exhausting. Keep text and controls high-contrast and accessible. A duck's color should remain distinct against the pond background.

## 6. Pond environment

The habitat should feel like a miniature illustrated pond display.

### Environment elements
- A clearly framed pond with a deliberate, finished border.
- Layered water with soft tonal variation, ripples, and occasional glints.
- Rounded lily pads, reeds, small flowers, stones, and shoreline plants.
- A few carefully chosen props that create scale and little points of interest.
- Gentle shadows beneath ducks and objects to anchor them to the water.
- Subtle background details that do not compete with the ducks.

### Composition
- The pond is a dedicated viewing space, not a full-screen background behind every menu.
- Keep a clean visual center where ducks can move and be seen.
- Place decorative elements around the edges so they do not obstruct the flock.
- Maintain a clear foreground/midground/background order.
- Use depth and overlap intentionally; never allow important outlines to disappear behind water or props.

### Ambient animation
- Slow, looping water shimmer and ripple effects.
- Lily pads and floating details may drift subtly.
- Small flowers or reeds can sway gently.
- Occasional bubbles, glints, or tiny water disturbances add life.
- Effects should be restrained; the ducks remain the focus.

## 7. Duck animation language

Animations should feel soft, buoyant, and characterful—not robotic.

### Core loops and actions
- **Idle:** subtle body bob, gentle breathing, occasional blink.
- **Look:** eyes shift, head tilts, brief pause.
- **Waddle:** short alternating steps, side-to-side body sway, small body bounce.
- **Turn:** smooth orientation change with a brief settle.
- **Hop / excitement:** compact squash-and-stretch, lift, and landing.
- **Rest:** slower breathing and relaxed expression.
- **Join pond:** a cheerful entrance, small bounce or splash, then transition into idle.

### Animation principles
- Use anticipation before larger actions and a soft settle afterward.
- Apply squash-and-stretch sparingly to emphasize weight and buoyancy.
- Keep foot movement and body sway synchronized.
- Avoid sudden teleporting, snapping, jitter, or excessive random motion.
- Use animation states with controlled transitions so multiple ducks can move simultaneously without visual chaos.
- Preserve the character silhouette throughout every animation.

## 8. UI and menu art direction

Menus must look like crafted objects from the same whimsical world—not like default web components or sterile computerized dashboards.

### Visual language
- Rounded, friendly panel shapes with intentional borders and layered depth.
- Cream, warm pastel, pond-green, and soft blue surfaces.
- Illustrated headers, small duck motifs, stamps, labels, and decorative details used with restraint.
- Buttons should look tactile: clear resting, pressed, disabled, and selected states.
- Use subtle shadows, inset details, edge highlights, and material texture to create depth.
- Typography should be friendly and highly legible; use expressive display lettering sparingly and a clean rounded face for small labels and body text.

### Avoid
- Generic rectangular cards with default shadows.
- Flat, lifeless panels with no material identity.
- Excessive gradients, neon glows, glassmorphism, and sci-fi HUD styling.
- Tiny text, overly dense information, or decorative clutter behind important controls.
- Placeholder emoji as a substitute for finished icons or illustrations.
- Inconsistent corner radii, outlines, or button styles.

### Layout relationship
The habitat should remain visible as the player opens menus. On desktop/wide layouts, the pond and menu can sit side by side. On iPhone portrait, adapt the same visual hierarchy to a compact habitat region and a thumb-friendly menu beneath it. Never force a narrow phone viewport into tiny side-by-side columns.

## 9. Capsule machine art direction

The collectible machine is a pastel-pink capsule dispenser, guided by the repository reference image but rendered as original in-game artwork. Do not ship or trace the stock reference image.

### Silhouette and construction
- A rounded, transparent aqua-tinted glass globe holds a visible pile of colorful capsules.
- The globe sits above a softly tapered pink pedestal with a bold burgundy-plum outline.
- A small rounded pink cap/button crowns the globe.
- A short pink collar separates the globe from the pedestal.
- The pedestal has a simple front crank/turning knob and a dark recessed capsule retrieval hatch near its base.
- Keep the silhouette compact, friendly, and immediately recognizable at phone size.

### Palette and material
- Use bubblegum pink, blush, and soft rose for the cap, collar, and body, with gentle lighter highlights and darker rose shading.
- The globe is pale aqua/blue-green glass with transparent-looking tonal layers, a clean curved glint, and subtle inner reflections.
- Capsules are small rounded two-tone eggs with warm plum outlines, a horizontal seam, and tiny glossy highlights. Vary their lower-half colors across butter yellow, mint/aqua, lavender, coral, and pink.
- Match the duck artwork's warm dark outlines, rounded shapes, polished toy finish, and soft dimensional shading.



### Capsule pile composition
- Capsules must form one compact, gravity-settled pile at the bottom of the globe, not evenly centered rows or isolated floating pieces.
- Use staggered, slightly overlapping rows with varied small rotations so each capsule looks nestled against its neighbors.
- Leave visible clear glass above the pile; keep every capsule fully inside the globe and away from the collar.
- Keep the dispenser compact in the roll panel so the machine does not dominate the menu or crowd the roll controls.

### Interaction and animation
- The roll action should make the whole machine wobble gently, tumble/rattle the capsules, and rotate the crank.
- Keep the machine grounded; motion should settle smoothly and must not cause layout shifts or clipping.
- Preserve the existing roll cost, collectible odds, currency deduction, and duck-reveal behavior unless those mechanics are explicitly changed.
- Respect reduced-motion preferences while keeping the roll action fully functional.
- The machine should remain legible and well-proportioned in both the narrow iPhone layout and the wider desktop layout.

## 10. Iconography and typography

- Create a consistent icon family with rounded strokes and clear silhouettes.
- Icons should be illustrated or carefully styled to match the duck world.
- Currency, collection, upgrades, and settings icons must be immediately distinguishable.
- Use a friendly rounded typeface for functional text and a more expressive display style for occasional titles.
- Prioritize legibility at common iPhone sizes; do not use decorative fonts for long descriptions or tiny labels.
- Keep the approved font hierarchy: **Just Ducky** is the main typeface across the interface, including headings, buttons, important labels, numerical indicators, and primary UI text. **Rubber Duck** is reserved for supporting descriptions and secondary text. The uploaded Duck and Ducky fonts may be used only as custom-font fallbacks; never use system fonts or generic system-font fallbacks anywhere in the game.

## 11. Asset production standards

- Create original assets with transparent backgrounds where appropriate.
- Keep character outlines closed, clean, and free of gaps.
- Use consistent light direction and outline weight across the asset set.
- Design important characters at a resolution that supports crisp downscaling on high-density mobile screens.
- Keep sprites and UI elements modular so animation and state changes do not require redrawing entire scenes.
- Provide separate layers or frames for body, eyes, beak, wings, and effects when useful for animation.
- Avoid blurry scaling, jagged edges, stray pixels, clipped contours, and background-color bleed.
- Test every asset against both light and dark portions of the pond scene.

## 12. Visual quality checklist

Before an asset or screen is considered finished, check:
- Does it clearly belong to the same visual world as the base yellow duck?
- Is the silhouette readable at iPhone gameplay size?
- Are the outlines continuous, confident, and consistent?
- Do shading and highlights make the material feel rounded and toy-like?
- Does the design feel cute and expressive rather than generic?
- Is the UI tactile and illustrated rather than flat or computer-generated?
- Does the pond remain visually calm enough for the ducks to stand out?
- Are animations smooth, buoyant, and free of jitter or abrupt snapping?


## 13. Mandatory art-source workflow

This document is not optional inspiration. It is the required production reference for every visual change.

- Before producing or modifying any character, sprite, prop, environment illustration, icon, UI surface, particle effect, or animation, read the relevant sections of this document.
- Treat the full document as the style contract: silhouette, proportions, line weight, palette, lighting, materials, rendering, composition, and motion must remain coherent.
- Do not rely on memory, generic art prompts, default libraries, emoji, or placeholder geometry when creating production visuals.
- For a new visual idea not covered here, establish its style, palette, shape language, and animation behavior in this document before or alongside implementation.
- Review new assets in the context of the existing game—not only in isolation—and revise mismatches before considering them finished.
- The user may explicitly change the art direction. When that happens, update this source so later work follows the newest approved direction.

## 14. Pond environment — lush illustrated storybook landscape

The pond must be a visually stunning little outdoor world rendered in the same cute, polished 2D cartoon language as the ducks. The target is a complete illustrated landscape, not a flat pond graphic with a few decorations.

### Overall feeling
Think of a lovingly painted miniature nature diorama: lush, welcoming, colorful, layered, and full of small discoveries. The world should feel like a place the ducks inhabit. Keep the charm and simplicity of cute character art while giving the environment enough craftsmanship and detail to feel special.

### Trees and leafy background
- Place clusters of trees behind and around the pond, set back from the shoreline so they frame rather than crowd the water.
- Use varied rounded canopy silhouettes, overlapping foliage clumps, subtle leaf highlights, and warm shadow pockets.
- Show trunks and branches where composition allows. Avoid featureless green blobs.
- Vary tree heights, widths, species-like silhouettes, and spacing. Avoid copy-pasted repeated tree shapes.
- Add occasional smaller shrubs and bushes to transition between trees and shoreline.
- Canopies and selected branches should have a soft, gentle breeze animation with subtle independent motion.

### Grass and shoreline planting
- Build flowing, layered grass along the banks, with curved tufts and individual blade clusters rather than a flat green strip.
- Use varied greens and warm highlights to separate grass planes and establish depth.
- Include cattails with recognizable brown seed heads, slender stems, and long leaves. Place them in small intentional clusters along selected edges of the water.
- Add reeds, rushes, clover, rounded shrubs, tiny wildflowers, daisies, buttercups, and occasional larger blooms for color accents.
- Include stones, pebbles, roots, and soft earth transitions to make the shoreline feel naturally formed.
- Keep plant silhouettes clear and avoid letting tall plants obscure ducks or important gameplay space.

### Pond water and edge
- Give the pond an organic, carefully designed outline. Avoid a plain ellipse or generic blue rectangle.
- Use multiple water tones and soft curved shapes to suggest depth, shallow edges, and reflected sky.
- Add layered ripples, subtle current lines, glints, and soft reflections. Keep the water clean and inviting.
- Integrate lily pads, small floating flowers, and occasional drifting leaves naturally into the composition.
- Use gentle shoreline shadows and overlapping bank elements to connect the water to the surrounding landscape.
- Preserve a clear central swimming area with enough room for multiple ducks of different sizes to move and remain readable.

### Composition and depth
- Compose the environment in at least four intentional visual planes: distant background, tree/shrub midground, pond and shoreline gameplay plane, and selective foreground framing.
- Use overlap, scale variation, atmospheric color shifts, and contact shadows to communicate depth in 2D.
- Let foliage frame the scene from the sides and corners, while leaving a clear visual window onto the ducks.
- Keep trees set back from the water's edge; use grasses, cattails, reeds, and stones as the transition to the pond.
- Distribute detail unevenly and naturally. Avoid symmetrical decoration, evenly spaced props, repeated stamps, or clutter.
- The scene must look finished and beautiful when viewed as a whole at iPhone screen size.

### Environmental motion
- Grass and reed clusters sway gently with varied phase, amplitude, and timing; do not animate every blade in unison.
- Cattail heads and flower stems should bend subtly with the breeze.
- Tree foliage should have slight canopy/branch movement while trunks remain stable.
- Water shimmer and ripples should loop at different speeds and positions to avoid obvious repetition.
- Floating leaves, tiny insects, and occasional bubbles may add life, but remain secondary to the ducks.
- Environmental motion must be smooth, restrained, lightweight, and performant on mobile.
- Avoid jitter, abrupt snapping, synchronized mechanical loops, or excessive motion. Support reduced-motion preferences where available.

### Environmental palette and rendering
- Use layered fresh greens: deeper forest/leaf greens in the background, mid greens for shrubs and banks, and brighter yellow-greens for sunlit grass.
- Use warm earth browns, soft stone neutrals, flower accents, and aqua/teal/blue-green water.
- Keep outlines consistent with the duck world: deep warm burgundy/plum-brown or warm near-black, adjusted carefully for small details.
- Use soft painted gradients, clean color separations, gentle highlights, and readable shadow shapes.
- Avoid flat single-color fills, harsh neon colors, muddy low-contrast greens, heavy photorealism, and plastic 3D rendering.

## 16. Rubber-duck toy identity and visual variety

Every collectible is the same kind of object: a molded rubber duck toy. The collection must never read as different bird species. All ducks share the exact same base silhouette, proportions, head, body, wing, tail nub, beak, eye placement, and molded construction.

Visual variety comes from:
- Distinct rubber colors and complementary belly shading.
- Different toy finishes where appropriate (glossy, pearlescent, metallic, matte).
- Accessories and costume pieces that sit on the shared duck model: bows, hats, crowns, glasses, collars, badges, tiny capes, and playful themed add-ons.
- Small painted toy graphics only when they look like intentional decals or manufactured details—not feathers, plumage, anatomy, or natural bird markings.

Non-negotiable visual rules:
- Do not change the base duck silhouette, add feather tails, add hair/feather tufts, reshape the wings, or alter body/head proportions between collectible designs.
- Do not add freckles, feather patterns, feather strokes, bird-like markings, fangs, or anatomy that makes a duck look like another species.
- A themed design such as Zomduck or Count Quackula is a themed rubber duck toy. Its theme must be communicated through color, paint, and removable-looking toy accessories—not creature anatomy.
- All shared base contours use the warm plum outline `#713c35`. Any accessory outline should harmonize with that same border language and remain visually attached to the toy.
- Keep accessories readable at normal iPhone gameplay scale, avoid obscuring the face, and preserve the same duck silhouette beneath them.
- All collectible ducks use the same base display scale. Rarity and coin production must not change the duck's physical proportions.
- Equipped cosmetics continue to render above the built-in toy design where they overlap.

Current collectible toy identities:
- **Sunny:** classic sunny-yellow rubber duck; clean, simple original toy.
- **Minty:** pastel mint-green rubber duck with small cool-toned sunglasses.
- **Berry:** lavender rubber duck with a little flower clip.
- **Peaches:** peach-colored rubber duck with a pink bow.
- **Lulu:** periwinkle rubber duck with a small star badge.
- **Goldie:** golden rubber duck with a tiny toy crown.
- **Zomduck:** moss-green rubber duck with a playful sewn-on patch accessory; no zombie anatomy.
- **Count Quackula:** midnight-purple rubber duck with a small costume bow and cape detail; no fangs, bat ears, or bird anatomy.

### Capsule progression and collectible economy

- Rarity order is **Common → Uncommon → Rare → Epic → Legendary → Mythic**.
- The **Classic Capsule** remains 25 Pond Coins and keeps the original six-toy odds unchanged.
- The **Premium Capsule** costs 250 Pond Coins and uses its own improved rarity distribution. Its current weighted mix is Sunny 24%, Minty 22%, Berry 17%, Peaches 14%, Lulu 9%, Goldie 8%, Zomduck 4%, and Count Quackula 2%.
- Mythic rubber-duck designs are exclusive to Premium Capsules for now. Premium rolls therefore have a 6% combined Mythic chance.
- Premium is a long-term coin sink, not a replacement for Classic. Both options remain available, and duplicates continue converting into the matching design's Duck Points.
- Keep capsule prices, odds, rarity labels, collection icons, pond sprites, and per-design coin rates in sync whenever the roster changes.

## 17. Completion and visual quality gates

An asset or animation is not finished if it is only a rough stand-in or a partial visual pass.

- No placeholder sprites, blank panels, temporary emoji, unfinished silhouettes, missing animation states, or TODO art in a completed feature.
- Every visible state must have its intended art: idle, active, pressed, disabled, selected, reveal, transition, and error/empty states where applicable.
- Animation work must include complete start, loop, transition, and settle behavior as appropriate—not a single disconnected moving part.
- Inspect assets at native size and at actual iPhone display scale. Check outline closure, edge quality, clipping, layering, contrast, and visual consistency.
- Test environmental motion alongside multiple ducks to ensure the combined scene remains calm, readable, and performant.
- The full pond composition must feel rich and deliberate even when the ducks are stationary. The environment is a primary feature, not disposable background filler.


## 16. Fifth non-negotiable rule — environmental objects respond to ducks

The environment is not a painted backdrop. Ducks are physical inhabitants of a shared little world, and the artwork and animation must communicate that contact convincingly.

### Visual interaction language
- Lily pads should visibly give way when nudged by a duck: shift across the water, tilt or bob subtly where appropriate, create small ripples, then drift and settle.
- Floating leaves and other loose surface details should respond to nearby movement with gentle displacement and wake effects.
- Flexible reeds, grass, cattails, and flower stems may bend or sway when brushed, then ease back into their resting pose.
- Fixed objects such as stones, roots, and sturdy shoreline structures should read as solid. Ducks should turn, slow, or route around them rather than visibly pass through.
- Duck contact should have readable anticipation and response: a small approach, soft nudge, object reaction, and a natural return to swimming or waddling.
- Larger ducks may produce a more noticeable response than tiny ducks, but all reactions should remain soft, cute, and physically believable.

### Layering and animation requirements
- Keep object motion visually connected to the point and direction of contact. Do not animate a lily pad independently in a way that ignores the duck that nudged it.
- Add subtle ripples or a small wake when a floating object moves through water.
- Use gentle easing, momentum, and damping so displaced objects do not snap instantly to a new location or continue sliding forever.
- Preserve correct foreground/background ordering as ducks move around, behind, or in front of environmental objects.
- Contact animations must not cause outlines to clip, sprites to overlap incorrectly, or visual layers to flicker.
- When several ducks interact with one object, reactions should remain composed and readable rather than producing frantic movement.

### Art-direction acceptance checks
- A duck visibly nudging a lily pad produces a smooth, connected displacement and water ripple.
- A duck never appears to swim through a lily pad or solid object.
- Plants that are meant to be flexible bend on contact; fixed props remain fixed.
- Object reactions match their material, weight, and placement in the scene.
- The interaction reads clearly at iPhone gameplay scale without excessive effects or clutter.
- Ducks and props remain visually coherent with the shared rounded shapes, warm palette, polished shading, and consistent outline style.

These requirements apply to every new duck, acquired duck, environmental prop, and habitat animation. Do not ship a pond scene where ducks are merely layered on top of scenery.


## 17. Updated UI direction — pastel sticker-book interface

The user-approved visual reference dated 2026-11-04 establishes a new direction for the entire game interface. This direction supersedes the older cream-and-sage dashboard treatment in section 8. It applies to menus, cards, buttons, counters, tabs, modal/dialog surfaces, badges, and decorative UI elements. It does not require redesigning the pond environment or collectible duck sprites.

### Core visual identity
- Build a sweet, playful pastel interface inspired by illustrated sticker books, cute casual puzzle games, and hand-decorated stationery.
- The dominant colors are bubblegum pink, blush, lavender, and soft periwinkle blue.
- Use deep plum / purple-brown outlines consistently around panels, buttons, icons, and ornamental frames.
- Favor rounded, inflated, softly scalloped, ribbon-like, or flower-edged silhouettes over plain generic rectangles.
- Surfaces should feel like layered paper, enamel badges, or glossy stickers: soft highlights, subtle inner shading, and a small grounded shadow.
- The visual should feel cohesive and deliberately illustrated, never like a generic web dashboard.

### Palette
- Background: soft lavender / orchid with gentle tonal variation.
- Main panels: blush pink and pale rose.
- Secondary panels and primary action buttons: powder blue / periwinkle.
- Alternate buttons and selected states: bubblegum pink.
- Accent details: lilac, pale yellow, peach, mint, and small floral colors.
- Outlines and primary text: deep plum, with pale cream or white highlights where needed.
- Keep functional text high-contrast and readable. Pastel fills must not make labels low-contrast.

### Panel and button construction
- Main content panels should have a clear plum outline, generous rounded corners, and a soft offset shadow or layered edge.
- Use scalloped edges selectively for featured headers, special cards, level/reward-like elements, and decorative sections. Avoid applying scallops to every tiny component.
- Primary action buttons should read as soft blue sticker buttons; secondary or alternate actions may use pink.
- Buttons need distinct resting, pressed, disabled, and selected states. Pressed states should move or compress subtly without shifting surrounding layout.
- Use pill, capsule, ribbon, flower, and rounded plaque silhouettes where they improve hierarchy.
- Use small ornamental flowers, leaves, sparkles, stars, and bows as corner accents or separators. Keep them away from text and touch targets.
- Counters, progress bars, currency indicators, and status chips should look like miniature decorated UI assets rather than plain text on a flat strip.

### Iconography and typography
- Replace generic emoji and inconsistent icon treatments with a unified set of chunky, outlined illustrated icons.
- Icons should use the same plum outline, pastel fills, and simple readable silhouettes as the reference.
- Keep important labels, headings, buttons, and counters in **Just Ducky**; use **Rubber Duck** for supporting descriptions and secondary copy. Do not introduce system fonts.
- Do not allow decorative fonts to compromise small counters, long descriptions, or accessibility.
- Maintain one-line currency/count labels where the layout calls for a compact counter, and prevent text from overflowing its card.

### Layout and decoration
- Keep the interface mobile-first, with comfortable thumb-sized controls and clear vertical hierarchy on iPhone.
- Desktop may expand spacing and panel width, but should retain the same visual language rather than reverting to a different theme.
- Use floral corners, sparkle marks, ribbons, and small decorative flourishes to add charm, not clutter.
- Ensure decorative art never obscures text, duck sprites, interactive controls, or important information.
- Preserve the pond scene as the habitat's own visual world; the new interface frames and complements it rather than recoloring or replacing it.

### Implementation and acceptance checks
- Apply the new treatment consistently across Roll, Pond, My Ducks, individual duck detail screens, upgrades, appearances, wallet/currency displays, dialogs, and future screens.
- Keep existing game mechanics, save data, duck art, pond composition, capsule machine behavior, and navigation intact during UI-only redesigns.
- Check the interface at narrow iPhone widths and desktop widths. No horizontal overflow, clipped labels, overlapping decorations, or tiny controls.
- Check text contrast and preserve readable single-line counts in the My Ducks cards.
- Avoid shipping a partial theme where only buttons change while the panels, cards, counters, and navigation remain in the old visual style.
- The overall result should feel like a polished pastel sticker-game UI, using the supplied image as direction rather than copying it literally.


## 18. UI refinement — plush, cuddly character-world finish

The follow-up direction approved on 2026-11-04 clarifies that the interface must feel less like stationery, a printed planner, or a business dashboard and more like a soft, lovable character game. This section refines and takes priority over any conflicting surface-treatment language in section 17.

### Emotional target
- The interface should feel warm, huggable, playful, and slightly magical—as if the ducks live inside a cute little toy world.
- Aim for a plush-toy / enamel charm / soft candy aesthetic: rounded, pillowy, soft-edged, friendly, and inviting.
- The reference's pastel colors and outlined illustrations remain useful, but avoid the rigid printed-card or office-stationery impression.
- The broad Hello-Kitty-like appeal is about sweetness, simplicity, expressive charm, and friendly character-world design. Do not copy protected character art, logos, or proprietary assets.

### Surface and shape language
- Prefer inflated rounded shapes, soft capsules, cloud-like panels, puffy buttons, scalloped edges, and gently irregular organic silhouettes.
- Panels should feel softly cushioned, with gentle inner highlights and rounded depth rather than hard flat frames.
- Use outlines as a warm illustration contour, not as rigid boxes around every single element.
- Avoid repeated nested rectangular borders, sharp dividers, dense grids, stiff card layouts, and excessive uniform corner radii.
- Use asymmetry and gentle variation in decorative elements so the screen feels hand-crafted and alive.
- Let some elements float visually with soft shadows instead of placing everything inside a bordered container.

### Color and lighting
- Keep the pastel pink, blush, lavender, and powder-blue family, but use soft tonal transitions and warm light.
- Add subtle creamy highlights, gentle rosy shadows, and restrained gradients that suggest rounded volume.
- Avoid high-contrast black outlines, harsh drop shadows, metallic shine, flat printed fills, and overly crisp corporate UI polish.
- Plum outlines should remain friendly and soft, with enough weight for phone readability.

### Buttons and interaction
- Buttons should look like soft candy pieces or puffy toy controls, not rectangular web buttons.
- Use rounded capsule and cloud silhouettes, slight inner highlights, and a small soft grounding shadow.
- Press feedback should feel like a cushion compressing or a soft button gently sinking; do not cause neighboring elements to jump.
- Selected states should feel like a favorite sticker or special charm, not a spreadsheet selection.
- Disabled states should remain clear but gently faded, not greyed-out in a businesslike way.

### Decoration and icon treatment
- Use small flowers, bows, hearts, stars, leaves, and sparkles as charming accents, with varied placement and scale.
- Prefer bespoke illustrated icons with soft fills and friendly contours over emoji or generic line-icon sets.
- Decoration should feel integrated into the interface, not like a repeated border pattern or printed ornament.
- Keep the duck artwork as the emotional center. UI flourishes must never compete with duck expressions or habitat movement.

### Layout and content density
- Favor breathing room, friendly groupings, and clear touch targets over dense dashboards.
- Avoid making every statistic a separate rigid tile. Combine related information in softer groupings where appropriate.
- Use small organic section headers, friendly microcopy, and clear visual hierarchy.
- The iPhone layout should feel like a cute little game screen, not a shrunken desktop application.
- Retain desktop responsiveness without introducing a more formal desktop-only visual language.

### Acceptance checklist
- At first glance, the UI should feel cute, cuddly, warm, and characterful—not businesslike, computerized, or print/stationery themed.
- Main panels and buttons should feel pillowy and tactile.
- The interface should not rely on repeated rectangular cards and nested borders to organize every item.
- The pastel palette should be cohesive and soft while keeping all functional text readable.
- Existing duck sprites, pond art, capsule machine, saved data, and game mechanics remain unchanged during a styling-only pass.
- Check narrow iPhone and desktop layouts for overflow, clipping, touch-target size, and readable counts.

## 19. Full-width terrarium viewing experience

The approved direction dated 2026-11-04 expands the pond into a full-width habitat viewing window. The pond should feel like a miniature living terrarium that the player is observing, not a small game viewport contained inside a narrow card.

- The pond scene spans the full available horizontal viewport, including the screen edges.
- Keep the existing illustrated landscape, water, shoreline, plants, and duck animation composition intact; expand the viewing canvas responsively rather than stretching or replacing individual artwork.
- Keep the habitat as the dominant visual feature on the Pond screen. The Pond Improvements content remains directly beneath it and may scroll below the viewing area.
- Header and navigation remain readable and comfortably inset; they do not constrain the habitat width.
- On wide screens, let the habitat use the full browser width while keeping supporting upgrade content at a comfortable reading width.
- Preserve the pond's natural aspect ratio and crisp rendering. Do not crop important scenery, distort ducks, or introduce horizontal scrolling.
- The habitat edge should feel like looking into a little environment, not a rigid inset video-game screen. Avoid adding a heavy frame or artificial monitor-like border.
- Keep mobile performance, touch interaction coordinates, duck movement bounds, and all saved game state unchanged.

## 20. Pond Improvements — floating button and bottom sheet

The approved interaction direction dated 2026-11-04 removes the permanent upgrade panel from the main Pond screen so players can enjoy and interact with the full-width habitat without scrolling past a large upgrade section.

- Place one friendly, clearly labeled **Pond Improvements** button directly beneath the terrarium.
- Style it as a soft, pillowy garden-themed control that belongs to the existing plush pastel interface.
- Activating it opens a rounded bottom sheet over the pond screen; the habitat remains in place behind the overlay rather than being pushed down or replaced.
- The sheet contains the existing Pond Improvements content and purchase controls. Preserve all upgrade costs, levels, coin deductions, income calculations, save behavior, and existing copy unless separately requested.
- The sheet has its own vertical scrolling area. Scrolling upgrade content must not scroll the underlying Pond screen.
- Include a clear close control and allow tapping the dimmed backdrop or pressing Escape to dismiss the sheet.
- On phones, anchor the sheet to the bottom with safe-area spacing and comfortable thumb-sized controls. On wider screens, present it as a centered, comfortably sized floating panel.
- Keep the open/close motion soft and restrained, and respect reduced-motion preferences.
- Do not add a permanent page-length upgrade section beneath the pond, introduce horizontal scrolling, or obscure the habitat when the sheet is closed.


## 21. Just Ducky primary UI typography

**Just Ducky** by **Duck Reid** is the approved primary interface typeface.

- Use Just Ducky for all primary UI text: headings, titles, buttons, tabs, important labels, counters, numerical indicators, and other high-priority interface text.
- Use **Rubber Duck** for supporting descriptions and secondary copy such as subtitles, rarity descriptors, upgrade explanations, duck detail metadata, and small informational text.
- Do not use system fonts, generic `sans-serif`/`serif` fallbacks, or browser-default typography anywhere in the game. Keep the uploaded Duck and Ducky faces only as optional custom-font fallbacks behind the two approved typefaces.
- The font is downloaded from the author's DaFont listing during the Pages build and placed at `assets/fonts/JustDucky.ttf`; do not replace it with a visually similar substitute.
- Credit: **Just Ducky by Duck Reid**, [DaFont listing](https://www.dafont.com/justducky.font). The listing states it is free for personal use and requests credit and notification when used/shared. This game use is personal/non-commercial; obtain the appropriate permission or license before any commercial use.


## 22. Individual duck coin-income indicators

- Every duck in the pond gets its own floating payout indicator, anchored above its head and following its movement.
- The indicator displays the duck species' current per-second coin value, including the active Pond Improvement multiplier. Different species therefore show their own actual income rather than a shared flock total.
- Each duck triggers its own short payout animation on a staggered one-second rhythm: the cream sticker pops in, floats upward slightly, and fades away quickly so it can appear again on the next payout.
- Use the primary **Just Ducky** typeface for the numerical amount and all other important counters. Pair the amount with a tiny warm-gold coin mark, a plum outline, and a soft cream sticker surface for contrast against the water.
- Keep the cue compact and close to the duck's head. It must not change duck movement, coin calculations, save data, or the pond layout.
- Preserve continuous passive coin accumulation. The individual indicators are visual cues for each duck's per-second contribution, not a replacement payout system.



## 23. Duck Games — collectible accessory sprite family

Duck Games introduces collectible, equippable duck accessories as preparation for future boss fights and raids. All new pieces must look like tiny glossy toy-world treasures that belong to the established rubber-duck family.

### Shared accessory art rules
- Use the established warm plum-brown outline, rounded silhouettes, soft pastel fills, gentle dimensional shading, creamy highlights, and subtle contact shadows.
- Accessories must remain readable at small iPhone gameplay scale and must not obscure duck eyes, beaks, or expressions.
- Keep accessory sprites as transparent-background SVG or high-resolution raster art in `assets/accessories/`; do not use emoji or generic icon placeholders for collected rewards.
- The inventory must display the actual accessory sprite, not a text symbol. The pond duck renderer should draw the corresponding equipped piece on the correct body location.
- Hats sit directly against and conform to the crown; wing-held props are layered between the duck body and its near-wing panel: the wand remains visible against the body, while the wing panel is redrawn over the shaft; only a small grip detail sits above the wing; chest ornaments sit on the front body, never on the tail.
- Equipment is cosmetic for now. The data model should preserve item identity and equipment slots so later boss/raid systems can use accessories as armor/stat inputs without replacing this collection.

### Initial reward set
- **Berry Bonnet** (`berry_bonnet`, hat): a soft berry-pink bonnet with a curved crown, broad rounded brim, tiny cream bow, and warm golden center detail.
- **Starry Wand** (`star_wand`, hand): a golden wand with a dimensional butter-yellow star, plum outline, and tiny pastel sparkles. It is held beside the duck's near wing.
- **Peachy Beak Bow** (`peachy_beak_bow`, chest): a small peach-pink bow charm centered on the duck's chest, clear of the beak and tail.

### Lily Pad Hop presentation and motion
- The minigame is a miniature pond vignette: three rounded green lily pads, aqua/mint water tones, warm highlights, and soft plum outlines.
- The active target pad receives a gentle golden glow/lift; the player taps it during a five-hop run.
- Keep the game readable and thumb-friendly on iPhone. Motion should be brief and soft, and honor reduced-motion preferences.
- Reward reveal uses the exact inventory sprite. Do not substitute text-only rewards.

## Duck Games — autonomous activity presentation
- Lily Pad Hop is an activity the duck completes independently; the player does not tap pads, time reactions, or control the duck.
- When a duck is sent, show a dedicated illustrated activity screen with that exact duck visibly hopping between three lily pads. Use the duck's normal sprite and equipped accessories.
- The lily-pad course should feel like a small animated diorama: rounded layered pads, soft water/grass tones, gentle highlights, and a clear jumping arc. The duck should visibly travel from pad to pad and bounce on landing.
- Keep motion playful and readable, with a short pause between hops. Respect reduced-motion settings; the activity must still communicate progress without animation.
- The player can leave the activity screen to collect coins, roll capsules, inspect ducks, or improve the pond. The duck's activity continues in the background and resolves its reward automatically. Do not block normal navigation or passive income.
- Keep the activity display focused on the duck, course, progress, and result. Never add player-facing reaction buttons or instructions to tap a pad.

## 24. Independent collectible duck PNG sprites

- Keep `assets/ducks/source.svg` as the untouched Sunny/master duck source.
- Each collectible has its own finished PNG in `assets/ducks/`: `sunny.png`, `mint.png`, `berry.png`, `peach.png`, `lilac.png`, `gold.png`, `zombie.png`, and `vampire.png`.
- The game loads these standalone PNGs directly. No runtime hue shifts, SVG filters, canvas recoloring, or layered recoloring systems are allowed.
- Every variant must preserve the exact master silhouette, face, beak, wing, outline, gloss, and shading placement. Only the rubber body palette changes.
- The beak is a signature orange feature. Keep every beak pixel identical to Sunny's original orange beak, including its upper/lower surfaces and mouth details. Do not use broad hue transforms that tint the beak.
- Recolor the body and its warm shadow regions together, but preserve the original per-pixel brightness/saturation structure so shadows remain smooth and highlights remain glossy. Avoid clipped RGB matrix transforms, noisy transitions, speckling, or newly introduced artifacts in shaded areas.
- Keep sprite dimensions, alpha silhouette, and registration aligned with the 160×148 master so accessories, wing layering, pond movement, and collectible icons remain consistent.
- The offline generator is `tools/generate_duck_pngs.py`. It must verify the master dimensions, unchanged alpha silhouette, and pixel-identical protected beak region before a generated sprite is accepted.
