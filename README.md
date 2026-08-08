# 🚀 Muhammed Sinan M — Personal Portfolio

> Source code for my personal portfolio website (https://muhammedsinan.in). A comprehensive reference covering every aspect of the project — architecture, design system, colors, typography, layout, animations, JavaScript features, and SEO optimizations.

---

## 🧑‍💻 Owner / Subject
 
| Field        | Value                                                         |
| ------------ | ------------------------------------------------------------- |
| **Name**     | Muhammed Sinan M                                              |
| **Role**     | Computer Science Student · Full-Stack Developer · AI Enthusiast |
| **Location** | Irinjalakuda, Kerala, India                                   |
| **Email**    | muhammedsinan.m67@gmail.com                                   |
| **Phone**    | +91 85905 68566                                               |
| **Contact**  | https://contact.muhammedsinan.in                              |

### Social Links
| Platform   | URL                                          |
| ---------- | -------------------------------------------- |
| GitHub     | https://github.com/sidoxsinu                 |
| LinkedIn   | https://www.linkedin.com/in/sidoxsinu/       |
| X/Twitter  | https://x.com/sidoxsinu                      |
| Instagram  | https://www.instagram.com/sidoxsinu          |

---

## 🗂️ Project File Structure

```
cv/
├── index.html             # Main HTML (1486 lines, 93 KB) — all sections
├── Style.css              # All styles (1405 lines, 29 KB)
├── animations.js          # All JavaScript animations & interactions (537 lines)
├── Style_backup.css       # CSS backup
├── index_backup.html      # HTML backup
├── images/
│   ├── profile-picture/   # Profile photo (bg-removed-black&white-pfp.png)
│   ├── certificates/      # 23 certificate images/PDFs
│   ├── certs/             # Certificate thumbnails (JPG)
│   └── Resume/            # Muhammed Sinan M.pdf
├── libs/                  # Local library files
├── venv/                  # Python virtual environment (utility scripts)
└── *.py                   # Helper Python scripts (fix_html.py, fix_carousel.py, etc.)
```

---

## 🛠️ Technology Stack

### Frontend Core
| Technology       | Version / Source                          | Purpose                          |
| ---------------- | ----------------------------------------- | -------------------------------- |
| **HTML5**        | Semantic markup                           | Structure of all sections        |
| **CSS3**         | Vanilla CSS (`Style.css`)                 | All styling, layout, animations  |
| **JavaScript**   | Vanilla ES6+ (`animations.js`)            | Animations, interactions, logic  |

### External Libraries (CDN)
| Library               | CDN URL                                                    | Purpose                       |
| --------------------- | ---------------------------------------------------------- | ----------------------------- |
| **GSAP 3**            | `cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js`             | Hero + scroll animations      |
| **GSAP ScrollTrigger**| `cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js`    | Scroll-driven animation engine|

### Fonts (Google Fontshare API)
| Font             | Weights         | Usage          |
| ---------------- | --------------- | -------------- |
| **General Sans** | 500             | Headings (`--font-heading`) |
| **Space Grotesk**| 300, 400        | Body text (`--font-body`)   |

### Hosting / Deployment
- Portfolio: served as a **static HTML file** (`file://` local or web server)
- Projects hosted on **Vercel**
- Contact page: `https://contact.muhammedsinan.in`

---

## 🎨 Design System

### Color Palette

| CSS Variable      | Value                          | Usage                              |
| ----------------- | ------------------------------ | ---------------------------------- |
| `--bg-color`      | `#111111`                      | Main background (soft dark premium)|
| `--text-primary`  | `#ffffff`                      | Primary text                       |
| `--text-secondary`| `#999999`                      | Muted / secondary text             |
| `--accent-red`    | `#E54D2E`                      | Accent highlights, timeline dots, tags |
| `--font-heading`  | `'General Sans', sans-serif`   | All headings                       |
| `--font-body`     | `'Space Grotesk', sans-serif`  | Body, paragraphs, labels           |

#### Additional Inline Colors
| Color              | Value         | Usage                                               |
| ------------------ | ------------- | --------------------------------------------------- |
| Hero background    | `#ffffff`     | Pure white for text-inversion trick                 |
| Accent orange/red  | `#E8562A`     | Quote sources, cert numbers, event results, nav hover |
| Dark card bg       | `#1a1a1a`     | Cards, carousels, dropdowns                         |
| Darker card hover  | `#222222`     | Card hover state                                    |
| Split card right   | `#0d0d0d`     | Project card image-panel background                 |
| Footer background  | `#0a0a0a`     | Site footer                                         |
| Footer bottom bar  | `#081022`     | Copyright bar                                       |
| Gold accent        | `#c9a84c`     | Print CV link, gold-toned elements                  |
| Gold border        | `rgba(212,175,55,0.4)` | Featured project card border          |
| Char dim           | `rgba(255,255,255,0.12)` | Un-lit chars in About text fill     |
| Char accent dim    | `rgba(229,77,46,0.18)`   | Un-lit keyword chars                |

### Typography Scale

| Element          | Size                          | Weight | Family          |
| ---------------- | ----------------------------- | ------ | --------------- |
| Hero title       | `clamp(4rem, 12vw, 12rem)`    | 500    | General Sans    |
| Section h3       | `3.5rem`                      | 500    | General Sans    |
| Section h4 cards | `2rem`                        | 500    | General Sans    |
| Large intro text | `4rem` (↓ 2.5rem @1024px)    | 500    | General Sans    |
| CTA heading      | `clamp(3rem, 6vw, 5rem)`      | 500    | General Sans    |
| Fan title        | `clamp(2.2rem, 5vw, 4rem)`    | 700    | General Sans    |
| Body / card text | `1.1rem`                      | 400    | Space Grotesk   |
| Section label    | `0.75rem`, letter-spacing 0.12em | 400 | Space Grotesk   |
| Tag / badge      | `0.85rem`, uppercase          | 400    | Space Grotesk   |
| Journey year     | `2.8rem`                      | 300    | General Sans    |

---

## 📐 Layout & Positioning

### Global Layout
- **Body**: `overflow-x: clip`, `max-width: 100vw`, dark background `#111111`
- **Sections**: `max-width: 1200px`, `margin-inline: auto`, `padding-block: 5rem`
- **Section inner**: `flex-direction: column`, `gap: 32px`
- Global CSS reset: `* { margin: 0; padding: 0; box-sizing: border-box; }`
- Anti-aliasing: `-webkit-font-smoothing: antialiased`

### Navigation — `.premium-nav`
- `position: fixed`, `top: 0`, full width, `z-index: 1000`
- `padding: 32px 5vw`
- **`mix-blend-mode: difference`** — makes nav white text invert over any background
- `pointer-events: none` on nav, `auto` on children (so it doesn't block scroll)
- Left: copyright `© Muhammed Sinan M` — scrolls to top on click
- Center: `About`, `Projects`, `Experience`, `Resume` (Resume styled orange `#E8562A`)
- Right: `Let's Talk!` button → `https://contact.muhammedsinan.in`
- **Underline hover**: `::after` pseudo-element, `scaleX(0→1)` on hover, `cubic-bezier(0.16, 1, 0.3, 1)`

### Hero Section — `.hero-premium`
- `position: relative`, `width: 100vw`, `height: 100vh`
- **Background**: Pure `#ffffff` white
- **Center content**: flex, `align-items: center`, `justify-content: center`
- **Profile photo** (`.hero-pfp`):
  - `position: absolute`, `height: 110vh` (overflows), `z-index: 1`
  - `filter: grayscale(100%) contrast(1.3) brightness(0.85)`
  - GSAP parallax: moves `yPercent: 15` on scroll
- **Name title** (`.hero-title`):
  - `position: absolute`, `z-index: 2`
  - `mix-blend-mode: difference` — white text inverts to black on white bg and stays white on dark bg
  - `font-size: clamp(4rem, 12vw, 12rem)`, letter-spacing `-0.05em`
- **Social icons** (`.hero-socials`): `position: absolute`, `left: 5vw`, `bottom: 40px`, column flex, `mix-blend-mode: difference`
- **Role subtitles** (`.hero-roles`): `position: absolute`, `right: 5vw`, `bottom: 40px`, text-right, `mix-blend-mode: difference`, `font-size: 1.5vw`
- **Scroll circle** (`.scroll-circle-wrapper`): `position: absolute`, `bottom: 110px`, `right: 5vw`, `z-index: 10`

### Card Layout — `.split-card`
- `display: flex`, `flex-direction: row` (stacks to column at ≤1024px)
- **Left panel** `.split-card-content`: `flex: 1`, `padding: 60px`, column flex
- **Right panel** `.split-card-image`: `flex: 1`, `background: #0d0d0d`, shows year + large acronym letters (`font-size: 10rem`, `rgba(255,255,255,0.03)`)

### Skills Grid — `.skills-grid`
- `display: grid`, `grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`, `gap: 40px`

### Journey Timeline
- `width: 100vw`, `margin-left: calc(-50vw + 50%)` — breaks out of container to full bleed
- Horizontal scroll viewport, `scroll-snap-type: x mandatory`
- Each column: `flex: 0 0 350px` (280px on mobile)

### Certificate Carousel — `.cert-viewport`
- Full-width overflow-x scroll with hidden scrollbar
- `padding-block: 80px` (for 3D perspective room)
- `padding-inline: calc(50vw - 120px)` (centers first/last card)
- `cursor: grab / grabbing`
- Glow fade edges via `.cert-carousel-stage::before/after` pseudo-elements

### Stats Strip — `.stats-strip`
- `display: flex`, `justify-content: space-around`, `flex-wrap: wrap`
- 3 items: `27+ EVENTS`, `6+ PROJECTS`, `3 AWARDS`

### CTA / Contact Section — `.cta-section`
- `display: flex`, `flex-direction: column`, `align-items: center`
- `padding: 100px 5vw`
- `background: linear-gradient(to bottom, transparent, rgba(255,255,255,0.02))`
- Social pills row: flex-wrap, gap 16px

### Footer — `.site-footer`
- `background: #0a0a0a`, `padding: 50px 10%`
- 3-column flex: Contact info | Quick Links | Social & More
- Bottom copyright bar: `#081022`, `font-size: 12px`

---

## 🗺️ Page Sections (in order)

| # | Section ID         | Label              | Background        |
|---|--------------------|--------------------|-------------------|
| 0 | *(hero)*           | Hero               | `#ffffff` white   |
| 1 | `#about`           | About Me           | dark `#111111`    |
| 2 | `#stats-strip`     | Stats              | dark              |
| 3 | *(testimonials)*   | Quotes Marquee     | `rgba(255,255,255,0.02)` |
| 4 | `#journey`         | Journey & Milestones | dark            |
| 5 | `#education`       | Education          | transparent       |
| 6 | `#projects`        | Projects           | dark              |
| 7 | `#achievements`    | Achievements       | dark              |
| 8 | `#experience`      | Experience         | transparent       |
| 9 | `#skills`          | Technical Skills   | dark              |
| 10| `#clubs`           | Clubs & Orgs       | transparent       |
| 11| `#hackathons`      | Hackathons & Events| dark              |
| 12| `#certifications`  | Certifications     | transparent       |
| 13| `#contact-cta`     | CTA / Contact      | gradient dark     |
| 14| *(footer)*         | Footer             | `#0a0a0a`         |

### Scrollspy Sidebar
- 11 dot indicators (`#scrollspy`) — right side, fixed position (currently `display: none` via CSS cleanup rule)
- Sections tracked: About, Journey, Education, Projects, Achievements, Experience, Skills, Clubs, Hackathons, Certifications, Let's Talk!

---

## 📄 Section Content Details

### Hero
- Profile photo: `images/profile-picture/bg-removed-black&white-pfp.png` (B&W, no background)
- Name: **Muhammed** / **Sinan M** (split with `<br>`, mix-blend-mode inverted)
- Role text: "Computer Science Student" · "Full-Stack Developer"
- Scroll circle: rotating SVG text `"SCROLL • EXPLORE •"` + orange asterisk icon
- Social icons: GitHub, LinkedIn, X/Twitter, Instagram (Feather SVG icons)

### About
- Large intro text with **scroll-fill letter animation** (character-by-character on scroll)
- Keywords in orange: `passionate`, `about`, `tech`, `solutions`
- Full text: *"Computer Science student passionate about building real-world tech solutions with clean logic and user-focused design. Strong in frontend development, system thinking, and problem solving, with hands-on experience in developing platforms from scratch. Interested in AI-driven products, SaaS platforms, and scalable systems."*

### Stats Strip
| Stat   | Value  |
| ------ | ------ |
| Events | 27+    |
| Projects | 6+   |
| Awards | 3      |

### Testimonials Marquee (3 quotes, duplicated for seamless loop)
1. *"Was found punctual and inquisitive throughout the programme."* — Suvidha Foundation, Research Internship
2. *"Recognized for technical excellence and innovation among all competing teams."* — MuLearn NSSCE, Build with AI Hackathon
3. *"Active participation, critical thinking ability, and contribution towards nurturing creativity and technical excellence."* — YIP 8.0, K-DISC Government of Kerala

### Journey Timeline (horizontal scroll, 3 columns)
| Year | Milestones |
|------|-----------|
| **2026** | Research Intern @ Suvidha Foundation (AI & Dev workflows) · BeachHack Season 7 Finalist (HackForChrist) |
| **2025** | First Hackathon Win — WEBATHON 2025 Second Prize · Built projects across Python, React (MERN), and Java · B.Tech CS Started @ Christ College of Engineering |
| **2023** | Higher Secondary Science — MES HSS Irimbiliyam |

### Education
| Degree | Institution | Period |
|--------|------------|--------|
| B.Tech in Computer Science & Engineering | Christ College of Engineering, Irinjalakuda | 2025–2029 |
| Higher Secondary – Science | MES HSS Irimbiliyam | 2023–2025 |

### Projects (7 cards, split layout)
| # | Project | Tech | Year | Links |
|---|---------|------|------|-------|
| 1 | **Parackal Travels Hub** 💼 *Freelance* | HTML/CSS, JS, GSAP | 2026 | [Live](https://parackaltravelhub.com) |
| 2 | **Next Generation AI Assistant** 🏆 *Best Tech Project* | AI, Groq API, Llama 3.3 | 2024 | [Live](https://next-gen-ai-assistant-system.vercel.app) · [Repo](https://github.com/sidoxsinu/next-gen-ai-assistant-system) |
| 3 | **Pylon** — Smart Scholarship Finder | HTML/CSS, JavaScript | 2024 | [Live](https://pylon-topaz.vercel.app) · [Repo](https://github.com/sidoxsinu/Pylon) |
| 4 | **UniversityHub** — Student resource platform | HTML/CSS, JavaScript | 2024 | [Repo](https://github.com/sidoxsinu/universityhub) |
| 5 | **CodeBurry** — Gamified learning platform | React, TypeScript, TailwindCSS | 2024 | [Live](https://code-burry.vercel.app) · [Repo](https://github.com/sidoxsinu/CodeBurry) |
| 6 | **SilentGuard** — AI pattern analysis | AI/ML, Python | 2024 | [Repo](https://github.com/sidoxsinu/SilentGuard) |
| 7 | **AI Voice Assistant** — Automation | Voice UI | 2024 | [Repo](https://github.com/sidoxsinu/AI-Voice-Assistant) |

> The featured project card (Next Gen AI Assistant) has a gold border `rgba(212,175,55,0.4)` and gold badge for the 🏆 award. Includes a collapsible "View Recognition →" section with LinkedIn and Instagram links.

### Achievements
1. **🏆 Best Technical Project** — Google for Developers NSSCE Build with AI Hackathon *(MuLearn NSSCE, Mar 2026)*
2. **🏆 WEBATHON 2025 — Second Prize** — CSI CCE (Pylon project)

### Experience & Internship
1. **Research Intern** @ Suvidha Foundation (SMM) — 25 Mar 2026 – 25 Apr 2026
   - In collaboration with Code Karo Yaaro
   - Verify: https://suvidhafoundationedutech.org/verify
2. **NSS Volunteer Leader** @ MES HSS Irimbiliyam — 2023–2025
   - 240+ certified volunteer hours
   - Led community programs, digital content and campaigns

### Technical Skills
| Category | Skills |
|----------|--------|
| Web Development | HTML, CSS, JavaScript, React, TypeScript, TailwindCSS |
| AI & Problem Solving | Basic AI/ML Concepts, Logical Thinking, System Design |
| Design & Tools | UI/UX Design, Canva, Git/GitHub, VS Code |

### Clubs & Organizations

**Leadership & Responsibilities** (2023–2026, ongoing):
- IEEE IAS Webmaster — IEEE Industry Applications Society, CCE Student Branch (2026 – Present)
- IEEE CS Webmaster — IEEE Computer Society, CCE Student Branch (2026 – Present)
- Design Lead — IEEE Kerala Section Joint Chapter (CTS/Nano/EDS) (2026 – Present)
- Learning Coordinator — TinkerHub CCE (2026 – Present)
- Team Member — IEDC Kerala Startup Mission NEST (2026 – Present)
- Co-CFO — IEDC CCE, Innovation & Entrepreneurship Development Centre (Jun 2026 – Present)
- NSS Volunteer Leader (Jun 2023 – Mar 2025) · 240+ certified volunteer hours

**IEEE Memberships** (Aug 2025–Present):
- IEEE Member, IEEE Computer Society, IEEE Electron Devices Society, IEEE Electronics Packaging Society
- IEEE Broadcast Technology Society, IEEE Industry Applications Society, IEEE Vehicular Technology Society
- IEEE Engineering in Medicine & Biology Society
- IEEE Sensors Council (2026 – Present)
- IEEE Systems Council (2026 – Present)
- IEEE Transportation Electrification Council (2026 – Present)

**Communities & Organizations** (2025–Present):
- TinkerHub CCE, Community of Developers, FOSS CCE, IEDC Kerala Startup Mission NEST

### Hackathons & Events (27+ total, organized by institution)

| Institution | Events |
|------------|--------|
| **Christ College of Engineering (CCE)** | BeachHack Season 7 (Finalist), WEBATHON 2025 (2nd Prize), Code a Pookalam, TECHLETICS 4.0 Quake Clash (Participant), DEVMODE: UNITY UNLEASHED, EVOLV 2.0, FOSS RELAY CODING, JUMPSTART 8.0 |
| **VIT Vellore** | HackBattle (Participant) |
| **Rajagiri School of Engineering & Technology** | HackQuest '25 (Participant) |
| **NIT Calicut** | IEEE YESS'25 (Participant) |
| **IIT Hyderabad & Tech Maghi** | AI Cyber Security Workshop, Agentic AI Boot Camp |
| **NSS Palakkad / μLearn** | Build With AI 2026 Hackathon (Best Technical Project) |
| **K-DISC / Government of Kerala** | YIP 8.0 Idea Submission (Participant), YIP 8.0 VOS Training |

### Certifications (formal)
- IEEE Certified Member (CM)
- Google Developer Program (2025)
- National Service Scheme (NSS) Certificate (2023–2025)

### Languages
- English · Malayalam · Hindi · Arabic

### Certificate Carousel (23 cards, #01–#23)
| # | Certificate |
|---|-------------|
| #01 | IEEE YESS'25 |
| #02 | FOSS Relay Coding |
| #03 | EVOLV 2.0 Bootcamp |
| #04 | BeachHack 7 – Survive the Island |
| #05 | BeachHack 7 – Error 404 |
| #06 | YIP 8.0 VOS Training |
| #07 | Spectrum Softtech IV |
| #08 | HackBattle VIT |
| #09 | Code a Pookalam |
| #10 | AI Cyber Security Workshop |
| #11 | JUMPSTART 8.0 Bootcamp |
| #12 | NSS Volunteer |
| #13 | Unity Unleashed Workshop |
| #14 | Agentic AI Boot Camp |
| #15 | CSI Webathon 2nd Prize |
| #16 | BeachHack 7 – Debug |
| #17 | YIP 8.0 Idea Submission |
| #18 | HackQuest '25 |
| #19 | TECHLETICS 4.0 Quake Clash |
| #20 | IEDC District Hackathon |
| #21 | CSI Webathon Participant |
| #22 | MATLAB Onramp |
| #23 | Suvidha Research Intern |

---

## ✨ Animations & Interactive Features

### 1. GSAP Hero Entrance (inline script, `DOMContentLoaded`)
| Element | Animation | Duration | Ease |
|---------|-----------|----------|------|
| `.premium-nav` | `y: -20 → 0, opacity: 0 → 1` | 0.3s | power2.out |
| `.hero-title` | `y: 20 → 0, opacity: 0 → 1` | 0.4s | power3.out |
| `.hero-pfp` | `scale: 1.02 → 1, opacity: 0 → 1` | 0.4s | power2.out |
| `.hero-socials a` | `x: -10 → 0, opacity: 0 → 1` | 0.3s, stagger 0.05s | power2.out |
| `.hero-roles p` | `x: 10 → 0, opacity: 0 → 1` | 0.3s, stagger 0.05s | power2.out |
| `.scroll-circle-wrapper` | `opacity: 0, scale: 0.8 → 1` | 0.6s, delay 0.6s | power2.out |

### 2. GSAP Scroll-Driven Parallax (ScrollTrigger, scrub)
- **Profile image** (`hero-pfp`): `yPercent: 15` on scroll (slow float down)
- **Scroll circle SVG**: rotates `720°` over full page scroll
- **Hero name** (`hero-name`): `yPercent: -25` (separate instance in `animations.js`)
- **Hero portrait** (`hero-portrait`): `yPercent: 15`
- **Hero subtitle** (`hero-subtitle`): `opacity → 0`, `yPercent: -30`, fades out by `40% top`

### 3. Scroll Reveal — `animations.js` Feature 2
| Class | Animation | Duration | Trigger |
|-------|-----------|----------|---------|
| `.reveal-text` | `y: 50 → 0, opacity: 0 → 1` | 0.5s, power3.out | `top 88%` viewport |
| `.reveal-block` | `y: 35 → 0, opacity: 0 → 1` | 0.4s, power2.out | `top 85%` viewport |
| `.reveal-stagger` li | `x: -25 → 0, opacity: 0 → 1` | 0.6s, stagger 0.08s | `top 85%` viewport |

### 4. Letter-by-Letter Scroll Fill — Feature 9 (About section)
- Every character in `.large-intro-text` is wrapped in a `<span class="char">`
- Regular chars: default `rgba(255,255,255,0.12)` → lit `#ffffff`
- Keyword chars (`.highlight-text` words): default `rgba(229,77,46,0.18)` → lit `#E54D2E`
- Scroll progress: fill begins when text is 60% down viewport, ends when 60% above
- Uses `IntersectionObserver` + `requestAnimationFrame` for performance

### 5. Card Pile Build-Up (Desktop) + Mobile Scroll Reveal — Feature 10

**Desktop (> 768px) — GSAP Scroll-Pinned Pile:**
- Applied to `.projects`, `.achievements .projects`, `.experience .projects` containers
- **Initial State**: Section heading is visible alone; inner container is pinned. Cards are positioned off-screen above (`y: -160, opacity: 0, scale: 0.9`).
- **Drop-in Animation**: Cards drop in one by one (every ~70vh) with a `back.out(1.2)` bounce ease.
- **Dealt Deck Effect**: Each card lands slightly lower (`y: i * 15px`) with alternating rotations (e.g. `0°, -4°, +3.5°`).
- **Scroll-back**: Cards smoothly fly back up when scrolling in reverse.

**Mobile (≤ 768px) — IntersectionObserver Reveal:**
- GSAP pile is **completely skipped** (function returns early after `isMobile` check).
- Container class `card-pile-container` is replaced with `mobile-project-feed` (normal `flex-direction: column` flow).
- Each card gets `mobile-project-card--hidden` class (CSS: `opacity: 0; transform: translateY(28px)`).
- `IntersectionObserver` (threshold `0.08`, rootMargin `-40px`) watches each card.
- When card enters viewport → `--hidden` class removed, `mobile-project-card--visible` added (CSS transition handles fade + slide).
- Cards are revealed once only (`obs.unobserve(entry.target)`).
- `prefers-reduced-motion`: all transitions skipped, cards shown immediately at full opacity.
- Stagger: 0.05s delay increments per nth-child (1–4) via CSS.

### 6. 3D Certificate Carousel — Feature: Infinite Coverflow (inline script)
- 23 original cards are **cloned** (prepend + append sets) for seamless infinite scroll
- **3D coverflow effect**: `perspective(1400px) rotateY()` — cards fan left/right based on scroll center distance
  - Center card: `scale(1)`, `brightness(1)`, `rotateY(0)`
  - Side cards: `rotateY(±50deg)`, `scale(1.35)`, `brightness(0.65)`, `translateZ(80px)`
- **Auto-scroll**: constant `0.6px/frame` accumulator, pauses on mouse drag
- **Drag-to-scroll**: mouse `mousedown/mousemove`, speed factor `1.5×`
- **Click guard**: if total drag `> 5px`, click is suppressed (no accidental opens)
- **Teleport guard**: when `scrollLeft >= setWidth * 2` or `<= 0`, jumps back to real set
- Clicking a card opens the certificate file in a new tab

### 7. Fan/3D Carousel — Feature 1 (animations.js, for `.fan-card` elements)
- Center card angle: `0°`, z: `+80px`, scale: `1`
- Offset formula: `rotateY = offset * 22deg` (clamped ±55°), `scale = 1 - |offset| * 0.1`
- Navigation: arrow keys, dot clicks, side-card clicks, drag/swipe (mouse + touch)
- Auto-advances every **4 seconds**, pauses on `mouseenter`
- Drag threshold: `60px` for swipe, `8px` for isDragging flag

### 8. Magnetic Button Effect — Feature 3
- Applied to: `nav a`, `.contact-link`, `.btn-primary`, `.btn-secondary`, `.hero-cta`
- On `mousemove`: `translate(dx * 0.15, dy * 0.15)` from button center
- On `mouseleave`: resets to `translate(0, 0)`

### 9. 3D Card Tilt on Hover — Feature 4
- Applied to `.card`, `.split-card`, `.event-list-item`
- `perspective(800px) rotateX(±10deg) rotateY(±10deg) scale(1.02)` on mousemove
- Shine layer (`.tilt-shine`): radial gradient at cursor position `(--mx, --my)`, opacity 0 → 1

### 10. Custom Cursor — Feature 5
- `#cursorDot`: `position: fixed`, `mix-blend-mode: difference`, `16px` white circle
- Follows mouse with `mousemove` listener
- On hover (links, buttons, cards): expands to `40px`, turns `rgba(232,86,42,0.9)` (orange)
- Hidden on touch devices (`ontouchstart` check)
- `document.body.style.cursor = 'none'` for all elements

### 11. Number Counter — Feature 8
- Uses `IntersectionObserver` (threshold `0.5`)
- Animates from 0 → target over `1800ms` with ease-out-cubic
- Stats: `27+`, `6+`, `3`
- Suffix support via `data-suffix` attribute

### 12. Accordion Dropdowns — `toggleDropdown()`
- Used in Clubs and Hackathons sections
- `parentItem.classList.toggle('active')` → shows `.club-content` / `.event-content`
- Arrow rotates `180°` when open (CSS: `.active > .dropdown-arrow { transform: rotate(180deg) }`)

### 13. Scroll Circle Expand — (previous feature, icon interaction)
- Click/touch on the center orange asterisk of the scroll circle triggers expansion
- Only fires when interaction hits the central orange portion of the icon

### 14. Journey Timeline Navigation
- Prev/Next buttons scroll `viewport.scrollBy({ left: ±350, behavior: 'smooth' })`
- `scroll-snap-type: x mandatory`, each column is a snap point

### 15. Testimonials Marquee
- CSS animation: `marqueeScroll` — `translateX(0 → -50%)` over `25s linear infinite`
- `animation-play-state: paused` on hover

### 16. Reading Progress Bar
- `#reading-progress` element exists in HTML but is currently hidden (`display: none !important`)

### 17. Share Button + Popup
- `#share-btn`, `#share-popup`, `#share-toast` exist in HTML but are currently hidden
- Popup contains: LinkedIn, WhatsApp, Twitter/X, Instagram, Copy Link options

### 18. Carousel Navigation Buttons (`.carousel-nav-btn`)
- Ripple fill: `::before` pseudo, starts at `(--x, --y)` cursor position, expands to `150×150px` on hover
- Prev/next: `scrollBy({ left: ±300, behavior: 'smooth' })`

### 19. Back to Top Button — `#back-to-top`
- Fixed position, SVG chevron up icon
- `data-magnetic=""` attribute for magnetic effect

### 20. Mobile Nav Menu — `#mobile-nav-menu`
- Currently hidden (`display: none !important`)
- Contains all section links + Download Resume + Toggle Dark/Light

---

## 🧩 Key CSS Techniques

| Technique | Where Used | How |
|-----------|-----------|-----|
| `mix-blend-mode: difference` | Nav, hero title, socials | White elements invert to black on white backgrounds |
| CSS Custom Properties | Everywhere | `--bg-color`, `--accent-red`, `--font-heading`, `--mx`, `--my`, `--x`, `--y`, `--card-index` |
| `clamp()` fluid typography | Hero title, CTA, fan title | Scales smoothly between breakpoints |
| `scroll-snap-type: x mandatory` | Journey timeline, cert carousel | Snap-to-column horizontal scroll |
| `perspective` + `rotateY` | Cert carousel, fan carousel, card tilt | 3D transforms |
| `mix-blend-mode: difference` on cursor | `.cursor-dot` | White dot inverts on all backgrounds |
| Absolute card pile drop-in | Projects, skills, clubs, events | Cards stack overlapping the sticky heading on scroll |
| `IntersectionObserver` | Counters, about-text-fill | Efficient scroll detection |
| `requestAnimationFrame` | Carousel render, counters | Smooth 60fps rendering |
| `will-change: transform` | Parallax elements, carousel cards | GPU compositing hint |
| SVG `<textPath>` | Scroll circle | Text flows along circular path |
| CSS `::before`/`::after` | Nav underline, carousel fade edges, timeline dots | Pseudo-element design |
| `linear-gradient` fade edges | Cert carousel stage | Masks side cards with fade |
| `scrollbar-width: none` | All carousels, timeline | Hidden scrollbars |

---

## 📱 Mobile vs Desktop Experience & Optimizations

The portfolio implements a highly sophisticated responsive design. Desktop provides a rich, heavily animated, mouse-driven experience, while mobile provides a native-feeling, touch-optimized, performance-conscious layout.

### 1. Desktop Experience (Width > 768px)
- **Navigation**: Full horizontal navbar (`.premium-nav .nav-links`) with hover-underline animations.
- **Hero**: GSAP ScrollTrigger parallax (`yPercent: 15` on profile photo).
- **Cursor & Hover**: Custom magnetic cursor (`#cursorDot`) with `mix-blend-mode` inversion that expands over interactive elements.
- **Card Stacking**: Features a complex GSAP-driven "drop from top into a pile" animation for project cards, forming a 3D dealt deck as you scroll.
- **3D Tilt**: Project cards use `mousemove` events to calculate perspective and rotation (`rotationX`, `rotationY`), creating a shiny 3D tilt effect on hover (`.tilt-shine`).
- **Letter Fill**: The About section features a character-by-character text fill animation driven by scroll (`requestAnimationFrame`).

### 2. Mobile Experience (Width ≤ 768px)
- **Navigation**: Desktop links are hidden. A hamburger button (`.nav-hamburger`) toggles a full-screen slide-in overlay menu (`#mobile-nav-menu`) with massive typography for touch targets.
- **Hero Layout**: Hero container uses `100svh` to avoid iOS toolbar jumpiness. Profile photo is centered with CSS (`left: 50%; transform: translateX(-50%)`). GSAP hero parallax is disabled to prevent layout conflicts. Social icons and roles are repositioned to the bottom center.
- **Cursor & Tilt Disabled**: Custom `#cursorDot` is `display: none`, native pointers are restored. The 3D tilt and magnetic button effects are blocked using JS touch guards (`ontouchstart in window`).
- **CSS Sticky Stack (Custom Mobile Feature)**: The GSAP drop-from-top card pile is disabled. Instead, `.projects` uses `position: sticky` with staggered `top` offsets (`90px`, `102px`, etc.). As the user scrolls down, cards organically slide up and stack seamlessly at the top of the screen like a deck of cards.
- **Touch-Optimized Carousels**: The Certificate and Fan carousels utilize native `touchstart`, `touchmove`, and `touchend` events to handle swiping. Rotation limits in the 3D Fan Carousel are reduced from `±55°` to `±30°` to fit mobile screens.
- **Timeline Swipe**: Journey timeline supports horizontal touch swiping, and the `scrollBy` buttons shift `280px` instead of `350px`.
- **Performance Guards**: `will-change` properties are removed from idle elements to save GPU memory on mobile devices. Minimum touch bounds (`44x44px`) are enforced globally.

---

## 📐 Responsive Breakpoints

| Breakpoint | Changes |
|-----------|---------|
| `≤ 1024px` | Split cards stack to column, large intro text reduces to `2.5rem` |
| `≤ 768px` | Hero title `22vw`, roles `4vw`, section h3 `2rem`, nav padding reduced, social icons horizontal row at bottom, cards `padding: 32px 24px` |
| `≤ 768px` | Journey header stacks vertically, columns narrow to `280px` |
| `≤ 768px` | Scroll circle scales to `0.65` from bottom-right origin |
| `≤ 768px` | Footer converts to single column, skills grid converts to single column |

---

## 🔌 Global JavaScript Functions

| Function | Location | Purpose |
|----------|---------|---------|
| `toggleDropdown(button)` | `animations.js` (global) | Toggle club/event accordion open/close |
| `toggleMenu()` | `animations.js` (global) | Toggle `.nav-links.active` (legacy) |
| `toggleRecognition()` | inline HTML | Toggle `#recognition-links` visibility on featured project card |
| `closeMenu()` | inline HTML `onclick` | Close mobile nav menu |
| `window.open(url, '_blank')` | Cert carousel click | Open certificate in new tab |
| `window.print()` | Footer | Print CV |
| `window.scrollTo({top:0, behavior:'smooth'})` | Nav logo | Smooth scroll to top |

---

## 🏗️ Architecture Notes

- **Single HTML file** — all sections live in `index.html`, no routing
- **No build step** — pure HTML/CSS/JS, works directly in browser
- All JavaScript is split into **IIFEs** (Immediately Invoked Function Expressions), each labeled as "FEATURE N"
- GSAP is loaded from CDN and checked with `typeof gsap !== 'undefined'` before use
- `animations.js` is loaded with `defer` attribute at end of body
- Inline `<script>` in HTML handles: GSAP hero entrance, cert carousel, carousel 3D, journey navigation buttons
- Python scripts (`.py` files) are **utility scripts** used during development for HTML manipulation, not part of the runtime

---

## 🔗 External Links & APIs

| Resource | URL |
|---------|-----|
| Contact page | https://contact.muhammedsinan.in |
| Resume (PDF) | `images/Resume/Muhammed Sinan M.pdf` |
| Next Gen AI Assistant live | https://next-gen-ai-assistant-system.vercel.app |
| Pylon live | https://pylon-topaz.vercel.app |
| CodeBurry live | https://code-burry.vercel.app |
| Suvidha cert verify | https://suvidhafoundationedutech.org/verify |
| GSAP CDN | https://cdn.jsdelivr.net/npm/gsap@3/ |
| Font API | https://api.fontshare.com/v2/css |

---

## 🌐 SEO & Meta

```html
<title>Muhammed Sinan M | Full-Stack Developer & AI Enthusiast | Kerala</title>
<meta name="description" content="Portfolio of Muhammed Sinan M (sidoxsinu)...">
<meta property="og:title" content="Muhammed Sinan M | Full-Stack Developer & AI Enthusiast">
<meta property="og:description" content="Portfolio of Muhammed Sinan M (sidoxsinu)...">
<meta property="og:type" content="profile">
<meta name="twitter:card" content="summary_large_image">
```

- **JSON-LD Schema Markup**: Included rich `Person` schema providing details on education, occupation, portfolio URL, alternate names (`Mohammed Sinan`, `Sinan M`, `MohammedSinanM`), and technical skills (`GSAP`, `Freelance Web Development`).
- Favicon: inline SVG base64 — white square with dark `SM` initials
- Semantic HTML5 structure with `<h1>` (hero title), `<nav>`, `<section>`, and `<footer>` elements.
- ARIA Attributes (`aria-label`, `aria-hidden="true"`) implemented across the site for screen readers.
- Modern WebP Images (`loading="lazy"`) for all assets, ensuring maximum Core Web Vitals performance.

---

*Last updated: June 2026 · Generated from `index.html`, `Style.css`, and `animations.js`*
