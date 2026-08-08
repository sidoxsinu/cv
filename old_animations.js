
// PERFORMANCE: Apply will-change to hero-pfp AFTER load, not before.
// Pre-compositing before first paint can prevent Chrome's LCP reporter
// from recording the paint event, causing NO_LCP scores.
(function applyWillChangeAfterLCP() {
  const pfp = document.querySelector('.hero-pfp');
  if (!pfp) return;
  if (pfp.complete) {
    pfp.style.setProperty('will-change', 'transform', 'important');
  } else {
    pfp.addEventListener('load', function() {
      pfp.style.setProperty('will-change', 'transform', 'important');
    }, { once: true });
  }
})();

// FEATURE 2 — SCROLL-TRIGGERED TEXT REVEAL ANIMATIONS
(function initScrollReveal() {
  if (typeof gsap === 'undefined') return;
  gsap.registerPlugin(ScrollTrigger);

  const trigger88 = window.innerWidth <= 768 ? 'top 92%' : 'top 88%';
  const trigger85 = window.innerWidth <= 768 ? 'top 92%' : 'top 85%';

  gsap.utils.toArray('.reveal-text').forEach(el => {
    gsap.fromTo(el,
      { y: 50, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.5,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: el,
          start: trigger88,
          toggleActions: 'play none none none',
        }
      }
    );
  });

  gsap.utils.toArray('.reveal-block').forEach((el, i) => {
    gsap.fromTo(el,
      { y: 35, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.4,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: el,
          start: trigger85,
        }
      }
    );
  });

  gsap.utils.toArray('.reveal-stagger').forEach(list => {
    const items = list.querySelectorAll('li');
    gsap.fromTo(items,
      { x: -25, opacity: 0 },
      {
        x: 0,
        opacity: 1,
        duration: 0.6,
        stagger: 0.08,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: list,
          start: trigger85,
        }
      }
    );
  });
})();

// FEATURE 3 — MAGNETIC BUTTON EFFECT
(function initMagneticButtons() {
  if ('ontouchstart' in window || navigator.maxTouchPoints > 0) return;
  const magneticEls = document.querySelectorAll(
    'nav a, .contact-link, .btn-primary, .btn-secondary, .hero-cta, .magnetic-btn, .cta-btn, .btn, .social-pill'
  );

  magneticEls.forEach(el => {
    el.classList.add('magnetic-btn');

    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const cx = rect.left + rect.width / 2;
      const cy = rect.top + rect.height / 2;
      const dx = (e.clientX - cx) * 0.15;
      const dy = (e.clientY - cy) * 0.15;
      el.style.transform = `translate(${dx}px, ${dy}px)`;
    });

    el.addEventListener('mouseleave', () => {
      el.style.transform = 'translate(0, 0)';
    });
  });
})();

// FEATURE 4 — 3D CARD TILT ON HOVER
(function initCardTilt() {
  if ('ontouchstart' in window || navigator.maxTouchPoints > 0) return;
  const cards = document.querySelectorAll('.card:not(.card-swap-container .card), .split-card, .event-list-item');

  cards.forEach(card => {
    card.classList.add('tilt-card');

    if (!card.querySelector('.tilt-shine')) {
      const shine = document.createElement('div');
      shine.className = 'tilt-shine';
      if (getComputedStyle(card).position === 'static') {
        card.style.position = 'relative';
      }
      card.appendChild(shine);
    }

    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rotX = ((y - cy) / cy) * -10;  // max ±10deg
      const rotY = ((x - cx) / cx) * 10;

      // Use GSAP to animate rotationX/Y independently without breaking the 'y' and 'rotation' (Z) 
      // applied by the stacking animation!
      gsap.to(card, {
        rotationX: rotX,
        rotationY: rotY,
        scale: 1.02,
        transformPerspective: 800,
        duration: 0.1,
        ease: "none",
        overwrite: "auto"
      });

      const mx = (x / rect.width * 100).toFixed(1);
      const my = (y / rect.height * 100).toFixed(1);
      card.style.setProperty('--mx', `${mx}%`);
      card.style.setProperty('--my', `${my}%`);
    });

    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        rotationX: 0,
        rotationY: 0,
        scale: 1,
        duration: 0.4,
        ease: "power2.out",
        overwrite: "auto"
      });
    });
  });
})();

// FEATURE 5 — SMOOTH CUSTOM CURSOR
(function initCustomCursor() {
  if ('ontouchstart' in window || navigator.maxTouchPoints > 0) return;
  const dot = document.getElementById('cursorDot');
  if (!dot) return;

  if ('ontouchstart' in window) {
    dot.style.display = 'none';
    return;
  }

  let mouseX = 0, mouseY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = mouseX + 'px';
    dot.style.top = mouseY + 'px';
  });

  const hoverTargets = document.querySelectorAll('a, button, .fan-card, .project-card, .accordion-header, [role="button"], .split-card');
  hoverTargets.forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
  });

  document.body.style.cursor = 'none';
  hoverTargets.forEach(el => { el.style.cursor = 'none'; });
})();

// FEATURE 7 — HERO TEXT PARALLAX DEPTH
(function initHeroParallax() {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

  gsap.to('.hero-name', {
    yPercent: -25,
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero-premium',
      start: 'top top',
      end: 'bottom top',
      scrub: true,
    }
  });

  // Portrait parallax: desktop only — on mobile, pfp uses height:100% layout
  if (!('ontouchstart' in window || navigator.maxTouchPoints > 0)) {
    gsap.to('.hero-portrait', {
      yPercent: 15,
      ease: 'none',
      scrollTrigger: {
        trigger: '.hero-premium',
        start: 'top top',
        end: 'bottom top',
        scrub: true,
      }
    });
  }

  gsap.to('.hero-subtitle', {
    opacity: 0,
    yPercent: -30,
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero-premium',
      start: 'top top',
      end: '40% top',
      scrub: true,
    }
  });
})();

// FEATURE 8 — SECTION COUNTER / NUMBER ANIMATION
(function initCounters() {
  const counters = document.querySelectorAll('.count-up');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      observer.unobserve(entry.target);

      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const duration = 1800; // ms
      const startTime = performance.now();

      function tick(now) {
        const progress = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
        el.textContent = Math.round(eased * target);
        if (progress < 1) requestAnimationFrame(tick);
      }

      requestAnimationFrame(tick);
    });
  }, { threshold: 0.5 });

  counters.forEach(el => observer.observe(el));
})();

// Make toggleDropdown global
window.toggleDropdown = function (button) {
  const parentItem = button.closest('.club-item') || button.closest('.event-item');
  if (parentItem) {
    parentItem.classList.toggle('active');
    button.classList.toggle('active');
  }
};



// FEATURE 9 — LETTER-BY-LETTER SCROLL FILL (about text)
(function initAboutTextFill() {
  const para    = document.querySelector('#about .large-intro-text');
  const section = document.querySelector('#about');
  if (!para || !section) return;

  // ── Force the paragraph visible; char colours handle the reveal ──────────
  para.style.opacity = '1';
  para.style.transform = 'none';

  // ── 1. Split every character into its own <span> ─────────────────────────
  const chars = [];
  const nodes = Array.from(para.childNodes);
  para.innerHTML = '';

  nodes.forEach((node, nodeIdx) => {
    let text = node.textContent.replace(/\s+/g, ' ');
    if (nodeIdx === 0) text = text.trimStart();
    if (nodeIdx === nodes.length - 1) text = text.trimEnd();
    if (!text) return;

    if (node.nodeType === Node.TEXT_NODE) {
      Array.from(text).forEach(ch => {
        const s = document.createElement('span');
        s.className = 'char';
        s.textContent = ch;
        para.appendChild(s);
        chars.push(s);
      });
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      // keyword span (.highlight-text) → accent colour when lit
      Array.from(text).forEach(ch => {
        const s = document.createElement('span');
        s.className = 'char char--key';
        s.textContent = ch;
        para.appendChild(s);
        chars.push(s);
      });
    }
  });


  const total   = chars.length;
  let lastLit   = -1;
  let rafId     = null;


  // ── 2. Compute progress from the paragraph's own position ─────────────────
  function updateFill() {
    const rect = para.getBoundingClientRect();
    const vh   = window.innerHeight;
    const isMobile = window.innerWidth <= 768;

    // Fill begins when text is ~60% down the viewport on desktop, 85% on mobile
    const start = isMobile ? vh * 0.85 : vh * 0.60;  
    const end   = isMobile ? vh * 0.0 : vh * -0.40;  // finishes exactly when it hits the top edge on mobile

    let progress = (start - rect.top) / (start - end);
    progress = Math.max(0, Math.min(1, progress));

    const targetLit = Math.round(progress * total);

    if (targetLit === lastLit) { rafId = null; return; }

    if (targetLit > lastLit) {
      for (let i = Math.max(0, lastLit); i < targetLit; i++) {
        chars[i].classList.add('char--lit');
      }
    } else {
      for (let i = lastLit - 1; i >= targetLit; i--) {
        chars[i].classList.remove('char--lit');
      }
    }

    lastLit = targetLit;
    rafId = null;
  }

  function onScroll() {
    if (!rafId) rafId = requestAnimationFrame(updateFill);
  }

  // ── 3. Attach listener only while section is near viewport ───────────────
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        window.addEventListener('scroll', onScroll, { passive: true });
        updateFill(); // paint immediately on enter
      } else {
        window.removeEventListener('scroll', onScroll);
      }
    });
  }, { rootMargin: '400px 0px 400px 0px' });

  observer.observe(section);

  // Also run once on load in case about section starts in view
  updateFill();
})();



// FEATURE 10 — CARD PILE BUILD-UP (Desktop + Mobile)
// Phase 1: Section heading is visible alone.
// Phase 2: Each scroll segment drops the next card from above,
//          landing on the pile and fanning out with slight rotations for a "dealt deck" look.
// On mobile (≤768px): screen pins and cards drop one-by-one with no rotation,
//          creating a clean stacking effect synced to scroll.
(function initCardPile() {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

  const isMobile = window.innerWidth <= 768;

  // ONLY target .projects containers to avoid breaking skills grids or dropdowns
  const containers = document.querySelectorAll('#projects .projects, #achievements .projects, #experience .projects');
  
  // Alternating rotation offsets → natural "dealt deck" appearance (desktop only)
  const ROTS = [0, -4, 3.5, -6, 5, -2.5, 4.5, -3, 6, -1, 3, -5];

  containers.forEach(container => {
    const cards = Array.from(container.children).filter(el => el.matches('.card'));
    if (cards.length < 2) return; // Don't pile if only 1 card

    const section = container.closest('section');
    const sectionInner = section?.querySelector('.section-inner');
    if (!section || !sectionInner) return;

    // Apply grid overlap: cards will perfectly stack in CSS without explicit heights
    container.classList.add('card-pile-container');

    const vh = window.innerHeight;
    // Mobile: faster pacing (less scroll per card) since cards are taller in column layout
    const scrollPerCard = isMobile ? 0.55 : 0.70;
    const pinDistance = cards.length * vh * scrollPerCard;
    
    // GSAP will pin the inner section automatically and add the required spacing
    ScrollTrigger.create({
      trigger: section,
      start: 'top 0px',
      end: `+=${pinDistance}`,
      pin: sectionInner,
      pinSpacing: true,
    });

    // 3. Set up cards
    cards.forEach((card, i) => {
      // Kill tweens from Feature 2 reveal to prevent conflicts
      gsap.killTweensOf(card);
      card.classList.remove('fade-in-up', 'reveal-block', 'reveal-text', 'fly-left', 'fly-right');

      // Adaptive layout variables — mobile gets no rotation, smaller offsets
      const startScale = isMobile ? 0.95 : 0.9;
      const targetScale = 1;
      const rotMult = isMobile ? 0 : 1;      // No rotation on mobile
      const yStep = isMobile ? 8 : 15;        // Tighter stacking on mobile

      // Set initial state: hidden off-screen (below on mobile, above on desktop)
      const startY = isMobile ? 300 : -160;
      gsap.set(card, { clearProps: 'transform,opacity,filter' });
      gsap.set(card, { y: startY, opacity: 0, scale: startScale, rotation: 0, zIndex: i + 1 });
      card.style.removeProperty('--card-index');

      // 4. ScrollTrigger: drop each card when its threshold is reached
      const dropOffset = (i + 0.3) * (vh * scrollPerCard);
      
      ScrollTrigger.create({
        trigger: section,
        start: () => `top ${0 - dropOffset}px`,
        onEnter() {
          gsap.killTweensOf(card);
          gsap.to(card, {
            y: (i * yStep),
            opacity: 1,
            scale: targetScale,
            rotation: ROTS[i % ROTS.length] * rotMult,
            duration: isMobile ? 0.6 : 0.8,
            ease: isMobile ? 'power3.out' : 'back.out(1.2)',
          });
        },
        onLeaveBack() {
          gsap.killTweensOf(card);
          gsap.to(card, {
            y: startY,
            opacity: 0,
            scale: startScale,
            rotation: 0,
            duration: 0.4,
            ease: 'power3.in',
          });
        },
      });
    });
  });
})();


// FEATURE 11 — GLASSMORPHISM FLOATING NAV ON SCROLL
// Nav transforms from full-width transparent to a floating frosted-glass pill
// when scrolled past the hero, and reverts when scrolling back up.
(function initGlassNav() {
  const nav = document.querySelector('.premium-nav');
  const hero = document.querySelector('.hero-premium');
  if (!nav || !hero) return;

  // Use IntersectionObserver: when hero is mostly off-screen, activate glass nav
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Hero is visible → restore original nav
          nav.classList.remove('nav-glass');
        } else {
          // Hero scrolled away → morph to glass pill
          nav.classList.add('nav-glass');
        }
      });
    },
    {
      // Fire when only 5% of the hero is still visible
      threshold: 0.05,
    }
  );

  observer.observe(hero);
})();


