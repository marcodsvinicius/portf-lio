---
version: alpha
name: "Cyberpunk Glass & Neon Lime"
description: "Design System for Marco Vinicius' Portfolio. A premium dark interface combining modern glassmorphism, structured Montserrat typography, cyber-styled asymmetrical grids, and vibrant neon lime interactive highlights."
colors:
  background: "#050505"
  surface: "#111111"
  accent-lime: "#CCFF00"
  accent-brand: "#B7E500"
  accent-hover: "#B3E600"
  text-primary: "#FFFFFF"
  text-secondary: "#A0A0A0"
  text-dark: "#111111"
  border-subtle: "rgba(255, 255, 255, 0.1)"
  glow-shadow: "rgba(204, 255, 0, 0.3)"
  overlay-dark: "rgba(5, 5, 5, 0.8)"
typography:
  main-sans:
    fontFamily: "Plus Jakarta Sans"
    fontWeight: 500
    lineHeight: 1.6
  case-montserrat:
    fontFamily: "Montserrat"
    fontWeight: 400
    lineHeight: 1.6
  h1-hero:
    fontFamily: "Montserrat"
    fontSize: "4.5rem"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: "-0.05em"
  h2-section:
    fontFamily: "Montserrat"
    fontSize: "3rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  body-text:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  nav-text:
    fontFamily: "Montserrat"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.1em"
rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
  xl: "16px"
  full: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "96px"
components:
  quick-nav-dock:
    backgroundColor: "rgba(0, 0, 0, 0.8)"
    backdropFilter: "blur(24px)"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.xl}"
    padding: "6px"
  quick-nav-item-active:
    backgroundColor: "rgba(255, 255, 255, 0.1)"
    textColor: "{colors.accent-lime}"
  button-primary:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.text-dark}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.text-primary}"
    borderColor: "{colors.border-subtle}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
  project-card:
    backgroundColor: "{colors.accent-brand}"
    textColor: "{colors.text-dark}"
    rounded: "{rounded.xl}"
    padding: "32px"
---

# Cyberpunk Glass & Neon Lime Design System

This document describes the foundational patterns, tokens, and layouts that govern the visual identity and user experience of Marco Vinicius' Portfolio. It acts as the single source of truth for designers and developers (including AI coding agents) to build or extend this portfolio without drifting from the aesthetic guidelines.

---

## Overview

### High-End Cyberpunk Minimalist
The user interface is built on a high-contrast dark theme, combining raw cyberpunk energy (asymmetrical grids, industrial neon greens) with the elegance of premium editorial layouts (spacious grids, rich glassmorphism, bold uppercase typography). 

#### Core Brand Pillars:
1. **Deep Dark Tech Environment:** Absolute solid blacks (`#050505`) form the core workspace, creating a backdrop where neon accents pop without visual strain.
2. **Glassmorphism & Depth:** Soft borders (`rgba(255,255,255,0.1)`) and high-blur backdrops (`backdrop-blur-xl`) mimic smoked glass, layering navigation elements cleanly above content.
3. **Electric Accents:** High-frequency neon lime (`#CCFF00` / `#B7E500`) serves as the primary visual driver for interaction, focus states, and highlighting.
4. **Editorial Typography Structure:** Massive titles with tight letter-spacing, offset alignment columns, and a clean grid layout.

---

## Colors

The system uses a strict hierarchical color system to guide the user's attention from background content to primary interactive triggers.

* **Primary Solid Background (`#050505`):** The absolute foundation of the dark mode. Solid black to maximize contrast and eliminate screen glowing.
* **Secondary Surface (`#111111`):** A subtle dark slate used for cards, list backdrops, and containers.
* **Accent Lime (`#CCFF00`):** Electric neon green used strictly for active states, highlights, floating glows, and critical focus triggers.
* **Accent Brand Green (`#B7E500`):** A slightly richer lime tint used on the landing page's main grid card project backgrounds, providing a punchy yet premium tone.
* **Accent Hover Green (`#B3E600`):** A slightly deeper lime green for hover feedback transitions.
* **Text Primary (`#FFFFFF`):** High-readability white for headings, active labels, and critical text.
* **Text Secondary (`#A0A0A0`):** Soft grey for descriptions, subheadings, metadata, and default states.
* **Border Subtle (`rgba(255, 255, 255, 0.1)`):** Standard line dividers and container borders to maintain structure without cluttering.

---

## Typography

The project uses two primary Google Fonts to balance futuristic technological sharpness with fluid reading comfort.

* **Montserrat:** Applied on main section headers, all uppercase components, numeric metrics, navigation anchors, tags, and badge labels. This provides structural density and a modern editorial weight.
* **Plus Jakarta Sans:** Applied on descriptive body text, summaries, and narrative elements. This offers excellent readability in paragraph blocks on dark interfaces.

### Standard Typography Classes (Tailwind)

#### Page Header (Case Study Titles)
```html
<h1 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase py-2 leading-[1.0] tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-white via-white to-gray-500">
  TITLE HERE
</h1>
```
*Note: Always use `py-2` and `leading-[1.0]` on capitalized case titles to prevent uppercase diacritics (like `Ã`) from being clipped by overflow margins.*

#### Section Subtitle
```html
<span class="text-[#ccff00] font-mono text-sm font-bold mb-2 block">
  01 / SECTION NAME
</span>
```

#### Section Heading
```html
<h2 class="text-3xl font-bold uppercase tracking-tight text-white">
  Heading Title
</h2>
```

---

## Layout

The grid systems are highly structured but incorporate offset column densities.

### 1. Main Grid Card Component (Landing Page)
The primary work showcase is built around large cards arranged in a responsive grid (`grid-cols-1 lg:grid-cols-2`):
* Solid background color `#B7E500` that changes text elements to absolute dark `#111111`.
* Custom transition speeds and transforms: `hover:-translate-y-2 hover:shadow-[0_20px_40px_-10px_rgba(183,229,0,0.3)] duration-500`.
* Overlaid with a subtle noise filter texture to give a physical paper/screen feeling:
  ```html
  <div class="absolute inset-0 opacity-[0.05] pointer-events-none mix-blend-overlay" style='background-image: url("data:image/svg+xml,...");'></div>
  ```

### 2. Case Study Layout
* **Hero Block:** Spacious, minimal, full-width `header` with details divided into standard grid metadata properties (Company, Role, Resumo, Tags).
* **Section Grid:** Standard columns structured around a `grid md:grid-cols-12` split:
  * Column size `md:col-span-4` for numbers and section headings.
  * Column size `md:col-span-8` for case narrative, alerts, lists, and images.

---

## Elevation & Depth

To sustain the technological dark tone, traditional blurred drop-shadows are minimized. Instead, the interface relies on ambient radial color glows and sharp glassmorphic layering.

### Ambient Neon Glows
Radial lime ambient backdrops are used behind hero blocks to create depth:
```html
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-[600px] bg-[#ccff00]/5 blur-[120px] rounded-full pointer-events-none"></div>
```

### Smoked Glass Overlay
A layered translucent style used on navigation, tooltips, and floating widgets:
* Backdrop blur: `backdrop-blur-xl` / `backdrop-filter: blur(24px)`.
* Color fill: `bg-black/80`.
* Core border: `border border-white/10`.
* Custom glow shadow: `shadow-[0_15px_40px_rgba(0,0,0,0.6),0_0_30px_rgba(204,255,0,0.03)]`.

---

## Shapes

Shapes are geometric, clean, and futuristic.
* **Buttons:** Perfectly pill-shaped (`rounded-full` / `100px`) for high-contrast ergonomics.
* **Cards & Containers:** `rounded-2xl` (`16px`) for larger visual components and grids.
* **Tabs & Dock Sub-Items:** `rounded-xl` (`12px`) to match inner rounded margins beautifully.
* **Pills & Badges:** Compact pills (`rounded-full`) or custom sharp rectangular corners.

---

## Components

The system features several highly refined interactive components that must be replicated identically across all pages.

### 1. Floating Header + Glass Drawer Menu
Every page (home and case studies) shares the same navigation: a fixed top bar with the `MV.` logo on the left and a hamburger button on the right. Clicking the button opens a compact glassmorphic drawer anchored to the top-right corner (`#mobile-menu-drawer`), with the language toggle, section links (scrollspy-highlighted in lime) and social links.

> The bottom "Quick-Nav Dock" described in earlier versions of this document was removed from all pages. Do not reintroduce it: the drawer is the single navigation pattern.

* Trigger: `#mobile-menu-btn` (carries `aria-expanded` / `aria-controls`).
* Panel: `bg-[#050505]/95 backdrop-blur-2xl border border-white/10 rounded-2xl`, opens with `scale-95 → scale-100` + opacity.
* Backdrop: `#mobile-menu-backdrop` closes the drawer on click; `Esc` also closes it.
* Scrollspy: `IntersectionObserver` with `rootMargin: '-30% 0px -60% 0px'` over `section[id]`, toggling `text-lime bg-white/10` on the matching `[data-mobile-section]` link.
* Logic lives in `assets/js/site.js`; no page carries its own copy.

### 2. Solutions Carousel with Dynamic Image Synchronization
An interactive carousel that maps textual features to visual screen outputs on a synchronized canvas.

#### Structure:
* Left/Right buttons control the slide index.
* The translation is animated horizontally: `transform = translateX(-${currentIndex * 100}%)` on `#solucao-carousel-track`.
* The visual image `#solucao-image` has its source updated dynamically based on a mapped image array matching the active text block.
* Active navigation dots change state dynamically (`bg-black` vs `bg-black/20`).

### 3. Lightbox Image Modal
A smooth overlay window allowing users to examine case mockups in detailed full-screen views.
* Background: `bg-black/90 backdrop-blur-sm z-[100]`.
* Animated expansion: transition `scale-95 opacity-0` into `scale-100 opacity-100`.
* Scroll Locking: Set `document.body.style.overflow = 'hidden'` on open, and restore it on close to maintain scroll positions perfectly.

---

## Do's and Don'ts

### Do's:
* **DO** use absolute pixel dimensions or standard viewport-scale rules for images inside carousels to maintain layout ratios across resolutions.
* **DO** use Montserrat with uppercase tracking (`tracking-wider` or `tracking-widest`) for any technical indicators, numbers, tag categories, or labels.
* **DO** keep the bottom nav items in a vertical column for mobile (`flex-col`) with `text-[8px]` text, and horizontal `flex-row` with `text-[10px]` on desktop.
* **DO** ensure the separate floating back button is included in mobile docks right beside the nav items, so navigation flows perfectly on mobile viewports.
* **DO** use subtle hover micro-animations (`hover:scale-110`, `hover:-translate-y-2`, `transition-all duration-300`) to increase visual premium feeling.

### Don'ts:
* **DON'T** use standard saturated colors (e.g. basic blue or generic green). Stick strictly to the system's curated palettes: Electric Neon Lime (`#CCFF00`), Brand Green (`#B7E500`), and solid dark bases.
* **DON'T** add scroll progress lines or horizontal trackers at the top of case study pages; these have been intentionally removed to prevent visual clutter and maintain design simplicity.
* **DON'T** clip capital letter accents. Always ensure page headers use a combination of `py-2` and `leading-[1.0]` or appropriate line-height metrics.
* **DON'T** hardcode values that drift from the central design tokens. Always map colors to the glassmorphic spec (`bg-black/80 backdrop-blur-xl border border-white/10`).

---

## Implementation Notes (code)

### Files
* `tailwind.config.js` (repo root) — the tokens above as Tailwind theme extensions, compiled to `assets/css/tailwind.css` by `npm run build:css` or the GitHub Action. Use `bg-brand`, `text-lime`, `border-brand/40`, `bg-ink`, `bg-surface`, `font-montserrat`, `font-jakarta`, `animate-fadeIn` instead of arbitrary values like `bg-[#B7E500]`.
* `assets/css/site.css` — shared base styles plus the motion components below.
* `assets/js/site.js` — menu, header glass-on-scroll, scrollspy, scroll reveal, back-to-top, page transitions.
* `assets/js/home.js` — home-only interactions.
* `assets/js/case.js` — case-study carousels (slides from `#solucao-data` JSON), lightbox and password gate.

### Motion components (home)
* **Scroll reveal:** add `class="reveal"` (+ `style="--d:n"` for stagger, `--stagger` to change the step). Elements fade/slide in once when 8% visible.
* **Page transitions:** cross-document View Transitions (`@view-transition { navigation: auto }`) with a fade/slide; browsers without support get a 200 ms fade-out on internal link clicks.
* **Hero:** `#hero-canvas` draws a lime dot grid that brightens and pushes away from the pointer; `.hero-spot` is a radial light following the cursor. `.hero-highlight` wraps the key phrase of the `h1` (lime, glow, underline that draws itself). `.scroll-cue` is the animated scroll hint (hidden after 80 px, not shown on phones).
* **Project cards:** `.tilt-card` gets a 3D tilt (±6°) and a `.tilt-glow` sheen following the pointer; `.card-preview` slides a screenshot in on hover; below 1024 px it becomes a static block between the card header and the title.
* **Skills:** `.skill-card` items get a lime border glow and soft fill that follow the pointer across `#skills-grid` (desktop only).
* **Timelines:** `.timeline` containers draw a lime `.timeline-line` as the page scrolls; `.tl-dot` markers light up (`is-lit`) when the line passes them.
* **Expandable text:** `[data-expandable]` blocks clamp long descriptions and add a "Ler mais / Read more" toggle only when the text overflows.
* **Contact:** `.status-dot` availability pulse + `#local-time` (America/Sao_Paulo); `.copy-email` copies the address with a 2 s "Copiado!" state; `#contact-canvas` draws a signal radar (sweep, blips that light up when the beam passes, a blip that follows the pointer) and `#contact-orb-shape` tilts toward the pointer.

### Accessibility & motion safety
* Everything above respects `prefers-reduced-motion: reduce` (static grid and radar, no tilt, instant reveal).
* Focus is trapped inside the Hub de Obras password modal; `Esc` closes it and focus returns to the card.
