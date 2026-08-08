/**
 * AccordionGallery.js
 * Vanilla JavaScript port of the React Bits AccordionGallery component.
 * Requires GSAP.
 */
class AccordionGallery {
    constructor(element, options = {}) {
        this.root = element;
        this.items = options.items || [];
        this.defaultIndex = options.defaultIndex !== undefined ? options.defaultIndex : 2;
        this.accentColor = options.accentColor || '#e8562a';
        this.overlayColor = options.overlayColor || '#060010';
        this.textColor = options.textColor || '#ffffff';
        this.height = options.height || 460;
        this.gap = options.gap || 10;
        this.radius = options.radius || 16;
        this.expandRatio = options.expandRatio || 0.52;
        this.orientation = options.orientation || 'horizontal';
        this.duration = options.duration || 0.6;
        this.ease = options.ease || 'power3.out';
        this.parallax = options.parallax || 0.5;
        this.tilt = options.tilt || 8;
        this.stagger = options.stagger || 0.06;
        this.trigger = options.trigger || 'hover';
        this.showLabels = options.showLabels !== undefined ? options.showLabels : true;
        this.grayscale = options.grayscale !== undefined ? options.grayscale : true;

        this.vertical = this.orientation === 'vertical';
        this.count = this.items.length;
        this.active = Math.min(Math.max(this.defaultIndex, 0), this.count - 1);
        this.prefersReduced = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)').matches : false;
        
        this.panels = [];
        this.mediaElements = [];
        this.barElements = [];
        this.textElements = [];
        this.tl = null;
        this.mediaSize = 320;
        
        this.init();
    }

    init() {
        this.render();
        
        this.panels = Array.from(this.root.querySelectorAll('.ag-panel'));
        this.mediaElements = Array.from(this.root.querySelectorAll('.ag-panel__media'));
        this.barElements = Array.from(this.root.querySelectorAll('.ag-panel__bar'));
        this.textElements = Array.from(this.root.querySelectorAll('.ag-panel__text'));

        this.bindEvents();
        
        this.resizeObserver = new ResizeObserver(() => this.measure());
        this.resizeObserver.observe(this.root);
        
        this.measure();
        this.applyLayout(false);
    }

    render() {
        this.root.classList.add('accordion-gallery');
        if (this.vertical) this.root.classList.add('accordion-gallery--vertical');
        
        this.root.style.setProperty('--ag-accent', this.accentColor);
        this.root.style.setProperty('--ag-overlay', this.overlayColor);
        this.root.style.setProperty('--ag-text', this.textColor);
        this.root.style.setProperty('--ag-gap', `${this.gap}px`);
        this.root.style.setProperty('--ag-radius', `${this.radius}px`);
        this.root.style.height = this.vertical ? `${Math.round(this.height * 1.6)}px` : `${this.height}px`;
        
        this.root.setAttribute('role', 'list');
        this.root.setAttribute('aria-label', 'Quotes gallery');

        this.root.innerHTML = this.items.map((item, i) => {
            const isActive = i === this.active;
            const tag = item.link ? 'a' : 'div';
            return `
                <${tag} class="ag-panel ${isActive ? 'ag-panel--active' : ''}" 
                    style="border-radius: ${this.radius}px;" 
                    ${item.link ? `href="${item.link}"` : ''} 
                    data-index="${i}"
                    role="listitem" 
                    tabindex="0" 
                    ${isActive ? 'aria-current="true"' : ''} 
                    aria-label="${item.label}">
                    
                    <span class="ag-panel__frame">
                        <span class="ag-panel__media">
                            <img src="${item.image}" alt="" draggable="false" />
                        </span>
                        <span class="ag-panel__overlay" aria-hidden="true"></span>
                    </span>
                    
                    ${this.showLabels ? `
                        <span class="ag-panel__label" aria-hidden="true">
                            <span class="ag-panel__bar"></span>
                            <span class="ag-panel__text">
                                ${item.quote}
                                <span class="ag-panel__source">${item.source}</span>
                            </span>
                        </span>
                    ` : ''}
                </${tag}>
            `;
        }).join('');
    }

    bindEvents() {
        this.panels.forEach((panel, i) => {
            panel.addEventListener('mouseenter', () => {
                if (this.trigger === 'hover') this.setActive(i);
            });
            
            panel.addEventListener('focus', () => this.setActive(i));
            
            panel.addEventListener('click', (e) => {
                if (i !== this.active) {
                    e.preventDefault();
                    this.setActive(i);
                }
            });

            panel.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                    e.preventDefault();
                    this.setActive((i + 1) % this.count);
                    this.panels[(i + 1) % this.count].focus();
                } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                    e.preventDefault();
                    this.setActive((i - 1 + this.count) % this.count);
                    this.panels[(i - 1 + this.count) % this.count].focus();
                }
            });
        });
    }

    setActive(i) {
        if (this.active === i) return;
        
        this.panels[this.active].classList.remove('ag-panel--active');
        this.panels[this.active].removeAttribute('aria-current');
        
        this.active = i;
        
        this.panels[this.active].classList.add('ag-panel--active');
        this.panels[this.active].setAttribute('aria-current', 'true');
        
        this.applyLayout(true);
    }

    measure() {
        if (!this.root) return;
        const rect = this.root.getBoundingClientRect();
        const total = this.vertical ? rect.height : rect.width;
        const usable = Math.max(total - this.gap * (this.count - 1), 120);
        const size = Math.max(140, usable * Math.min(Math.max(this.expandRatio, 0.2), 0.9) * 1.22);
        this.mediaSize = size;
        this.root.style.setProperty('--ag-media-size', `${size}px`);
    }

    applyLayout(animate = true) {
        if (!this.panels.length || typeof gsap === 'undefined') return;

        const r = Math.min(Math.max(this.expandRatio, 0.2), 0.9);
        const grow = this.count > 1 ? (r * (this.count - 1)) / (1 - r) : 1;
        
        if (this.tl) this.tl.kill();
        const dur = animate && !this.prefersReduced ? this.duration : 0;
        this.tl = gsap.timeline();

        this.panels.forEach((panel, i) => {
            const isActive = i === this.active;
            const media = this.mediaElements[i];
            const bar = this.barElements[i];
            const text = this.textElements[i];

            const rot = isActive ? 0 : i < this.active ? this.tilt : -this.tilt;
            const rotProp = this.vertical ? { rotateX: -rot } : { rotateY: rot };

            this.tl.to(panel, { flexGrow: isActive ? grow : 1, ...rotProp, duration: dur, ease: this.ease }, 0);

            if (media) {
                const drift = Math.max(-1.5, Math.min(1.5, this.active - i));
                const shift = drift * this.parallax * this.mediaSize * 0.06;
                const gray = this.grayscale ? (isActive ? 0 : 1) : 0;
                this.tl.to(
                    media,
                    {
                        xPercent: -50,
                        yPercent: -50,
                        x: this.vertical ? 0 : isActive ? 0 : shift,
                        y: this.vertical ? (isActive ? 0 : shift) : 0,
                        '--ag-gray': gray,
                        '--ag-dim': isActive ? 0 : 0.35,
                        duration: dur,
                        ease: this.ease
                    },
                    0
                );
            }

            if (this.showLabels && bar && text) {
                if (isActive) {
                    this.tl.to([bar, text], { opacity: 1, x: 0, duration: dur, ease: this.ease, stagger: this.prefersReduced ? 0 : this.stagger }, 0);
                } else {
                    this.tl.to([bar, text], { opacity: 0, x: -14, duration: dur * 0.6, ease: this.ease }, 0);
                }
            }
        });
    }

    destroy() {
        if (this.resizeObserver) this.resizeObserver.disconnect();
        if (this.tl) this.tl.kill();
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const rootEl = document.getElementById('testimonials-accordion');
    if (rootEl && typeof gsap !== 'undefined') {
        const items = [
            { 
                image: 'images/project-images/AvenWing.webp', 
                quote: 'Premium e-commerce platform featuring an interactive product gallery, GSAP animations, and direct WhatsApp checkout.',
                source: 'AvenWing',
                label: 'AvenWing',
                link: '#project-avenwing'
            },
            { 
                image: 'images/project-images/Parackal-Travel-Hub.webp', 
                quote: 'Full-stack bilingual travel booking platform with custom inquiry flows and responsive design.',
                source: 'Parackal Travels Hub',
                label: 'Parackal Travels Hub',
                link: '#project-parackal'
            },
            { 
                image: 'images/project-images/Next-Gen-Ai-Assistant.webp', 
                quote: 'Award-winning multi-modal AI assistant powered by Groq Llama 3.3 for real-time voice interaction.',
                source: 'Next Gen AI Assistant',
                label: 'Next Gen AI Assistant',
                link: '#project-ai-assistant'
            },
            { 
                image: 'images/project-images/Pylon.webp', 
                quote: 'Zero-dependency scholarship discovery platform with real-time filtering and custom search algorithms.',
                source: 'Pylon',
                label: 'Pylon',
                link: '#project-pylon'
            },
            { 
                image: 'images/project-images/CodeBurry.webp', 
                quote: 'Gamified frontend development learning platform with interactive coding challenges and an XP-based reward system.',
                source: 'CodeBurry',
                label: 'CodeBurry',
                link: '#project-codeburry'
            }
        ];

        new AccordionGallery(rootEl, {
            items: items,
            defaultIndex: 2, // Center panel (3rd out of 5)
            accentColor: '#e8562a' // Match site's red accent
        });
    }
});
