import re

with open('index.html', 'r') as f:
    content = f.read()

# ==========================================
# 1. CSS INJECTIONS
# ==========================================
css_injection = '''
        /* --- GLOBAL ANIMATION PREFERENCES --- */
        html { scroll-behavior: smooth; }
        
        body, section, .card, nav, h1, h2, h3, h4, p, a, span, .timeline-marker, footer {
            transition: background-color 0.5s ease, color 0.4s ease, border-color 0.5s ease, box-shadow 0.4s ease;
        }
        
        body {
            animation: pageLoad 0.8s ease-out forwards;
            opacity: 0;
        }
        @keyframes pageLoad { to { opacity: 1; } }

        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
        }

        /* --- HERO ANIMATIONS --- */
        .hero-img-animate {
            animation: breathe 3s ease-in-out infinite alternate;
            will-change: transform, box-shadow;
        }
        @keyframes breathe {
            0% {
                transform: rotate3d(0, 1, 0, -5deg) scale(1);
                box-shadow: 0 0 15px rgba(212, 175, 55, 0.2), 0 0 30px rgba(10, 15, 30, 0.1);
            }
            100% {
                transform: rotate3d(0, 1, 0, 5deg) scale(1.02);
                box-shadow: 0 0 25px rgba(212, 175, 55, 0.5), 0 0 50px rgba(10, 15, 30, 0.3);
            }
        }
        
        html[data-theme="dark"] .hero-img-animate {
            animation: breatheDark 3s ease-in-out infinite alternate;
        }
        @keyframes breatheDark {
            0% { box-shadow: 0 0 15px rgba(212, 175, 55, 0.2), 0 0 30px rgba(100, 150, 255, 0.1); transform: rotate3d(0, 1, 0, -5deg) scale(1); }
            100% { box-shadow: 0 0 25px rgba(212, 175, 55, 0.5), 0 0 50px rgba(100, 150, 255, 0.3); transform: rotate3d(0, 1, 0, 5deg) scale(1.02); }
        }

        .clip-text {
            display: inline-block;
            overflow: hidden;
            vertical-align: bottom;
        }
        .clip-text-inner {
            display: inline-block;
            transform: translateY(100%);
            animation: slideUpReveal 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            animation-delay: 0.2s;
        }
        @keyframes slideUpReveal { to { transform: translateY(0); } }

        .cursor {
            display: inline-block;
            animation: blinkScale 1s steps(1) infinite;
            will-change: transform;
        }
        @keyframes blinkScale { 50% { transform: scaleY(0); } }

        .hero-actions .btn, .hero-actions a {
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
            will-change: transform, box-shadow;
        }
        .hero-actions .btn:hover, .hero-actions a:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        }

        /* --- NAVBAR ANIMATIONS --- */
        nav {
            transition: all 0.4s ease !important;
        }
        nav.scrolled {
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
            background: rgba(255,255,255,0.85);
        }
        html[data-theme="dark"] nav.scrolled {
            background: rgba(10, 15, 30, 0.85);
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        
        .nav-links a {
            position: relative;
            animation: navDrop 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            opacity: 0;
            transform: translateY(-10px);
        }
        @keyframes navDrop { to { opacity: 1; transform: translateY(0); } }
        
        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -4px;
            left: 0;
            width: 100%;
            height: 2px;
            background: var(--accent-blue);
            transform: scaleX(0);
            transform-origin: center;
            transition: transform 0.3s ease;
        }
        .nav-links a:hover::after, .nav-links a.active::after {
            transform: scaleX(1);
        }
        .nav-links a:active {
            transform: scale(0.97);
        }

        #themeToggle.flipping {
            animation: flipToggle 0.4s ease;
        }
        @keyframes flipToggle {
            0% { transform: rotateX(0deg); }
            50% { transform: rotateX(90deg); }
            100% { transform: rotateX(0deg); }
        }

        /* --- SCROLL-TRIGGERED ANIMATIONS --- */
        h3.fade-in-up {
            opacity: 0;
            transform: skewX(-2deg) translateX(-20px);
            transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform, opacity;
        }
        h3.fade-in-up.visible {
            opacity: 1;
            transform: skewX(0) translateX(0);
        }
        
        .card.fade-in-up {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform, opacity;
        }
        .card.fade-in-up.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .timeline-marker {
            transform: scale(0);
            transition: transform 0.6s cubic-bezier(0.68, -0.55, 0.27, 1.55);
        }
        .timeline-marker.visible {
            transform: scale(1);
        }

        .skill-category {
            opacity: 0;
            transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: transform, opacity;
        }
        .skill-category.fly-left { transform: translateX(-40px); }
        .skill-category.fly-right { transform: translateX(40px); }
        .skill-category.visible {
            opacity: 1;
            transform: translateX(0);
        }

        /* --- CARD HOVER & SHIMMER --- */
        .card {
            transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease, border-color 0.3s ease !important;
            will-change: transform, box-shadow;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.1);
        }
        html[data-theme="dark"] .card:hover {
            box-shadow: 0 12px 24px rgba(0,0,0,0.4);
        }
        
        .featured-card {
            position: relative;
            overflow: hidden;
        }
        .featured-card::before {
            content: '';
            position: absolute;
            top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(to right, transparent, rgba(255,255,255,0.1), transparent);
            transform: skewX(-20deg);
            animation: shimmerSweep 3s infinite linear;
            pointer-events: none;
        }
        @keyframes shimmerSweep {
            100% { left: 200%; }
        }

        #experience .card {
            border-left: 3px solid transparent;
        }
        #experience .card:hover {
            border-left-color: #D4AF37;
            animation: borderPulse 1.5s infinite alternate;
        }
        @keyframes borderPulse {
            0% { border-left-color: rgba(212, 175, 55, 0.5); }
            100% { border-left-color: rgba(212, 175, 55, 1); }
        }

        /* Certificate Images */
        .cert-img-container {
            perspective: 800px;
            overflow: hidden;
            border-radius: 8px;
        }
        .cert-img-container img {
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            transform: rotateY(15deg) scale(0.9);
            will-change: transform, filter;
        }
        .card:hover .cert-img-container img {
            transform: rotateY(0deg) scale(1.04);
            filter: brightness(1.1);
        }

        /* --- STATS ANIMATIONS --- */
        .stat-col {
            opacity: 0;
            transform: translateY(-5px);
            transition: all 0.5s ease;
        }
        .stat-col.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* --- MISC ANIMATIONS --- */
        #btt { transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); }
        #btt:hover { transform: rotate(360deg) scale(1.1); }

        footer a { transition: letter-spacing 0.3s ease, color 0.3s ease !important; }
        footer a:hover { letter-spacing: 1px; color: #fff !important; }

        .copyright-pulse {
            animation: copyPulse 4s infinite alternate ease-in-out;
        }
        @keyframes copyPulse {
            0% { opacity: 0.5; }
            100% { opacity: 0.8; }
        }
'''

if '/* --- GLOBAL ANIMATION PREFERENCES --- */' not in content:
    content = content.replace('</style>', css_injection + '\n    </style>')

# ==========================================
# 2. HTML STRUCTURE MODIFICATIONS
# ==========================================

# 2a. Profile Photo class
content = content.replace('class="hero-img"', 'class="hero-img hero-img-animate"')

# 2b. Hero Heading clipPath reveal
if '<span class="clip-text">' not in content:
    content = content.replace('<h2>Muhammed Sinan M</h2>', '<h2><span class="clip-text"><span class="clip-text-inner">Muhammed Sinan M</span></span></h2>')

# 2c. Cursor animation update (already handled in CSS, remove old CSS if needed)
content = re.sub(r'\.cursor\s*\{\s*animation:\s*blink[^}]*\}\s*@keyframes blink\s*\{\s*50%\s*\{\s*opacity:\s*0;\s*\}\s*\}', '', content)

# 2d. Featured Award Card class
if 'class="card fade-in-up" style="border-left: 3px solid #D4AF37;' in content:
    content = content.replace('class="card fade-in-up" style="border-left: 3px solid #D4AF37;', 'class="card fade-in-up featured-card" style="border-left: 3px solid #D4AF37;')

# 2e. Stats Stagger Elements
stat_html_old = '''<div style="flex: 1; text-align: center;">
                                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Event</div>
                                    <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary);">Build with AI</div>
                                </div>
                                <div style="flex: 1; text-align: center;">
                                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Organized By</div>
                                    <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary);">Google Developers</div>
                                </div>
                                <div style="flex: 1; text-align: center;">
                                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Recognition</div>
                                    <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary);">Best Technical Project</div>
                                </div>'''
stat_html_new = '''<div class="stat-col" style="flex: 1; text-align: center;">
                                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Event</div>
                                    <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary);">Build with AI</div>
                                </div>
                                <div class="stat-col" style="flex: 1; text-align: center;">
                                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Organized By</div>
                                    <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary);">Google Developers</div>
                                </div>
                                <div class="stat-col" style="flex: 1; text-align: center;">
                                    <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Recognition</div>
                                    <div style="font-size: 0.9rem; font-weight: 600; color: var(--text-primary);">Best Technical Project</div>
                                </div>'''
content = content.replace(stat_html_old, stat_html_new)

# 2f. Skills fly-in classes
content = re.sub(r'<div class="skill-category">', r'<div class="skill-category fly-left">', content, count=2)
content = content.replace('<div class="skill-category">', '<div class="skill-category fly-right">')

# 2g. Certificate Wrappers in Experience
cert_pattern = r'<div style="flex: 0 0 200px; max-width: 100%; display: flex; align-items: center; justify-content: center;">\s*<img src="(.*?)" alt="(.*?)" style="(.*?)">\s*</div>'
cert_repl = r'<div class="cert-img-container" style="flex: 0 0 200px; max-width: 100%; display: flex; align-items: center; justify-content: center;"><img src="\1" alt="\2" style="\3"></div>'
content = re.sub(cert_pattern, cert_repl, content)

# 2h. Copyright pulse
content = content.replace('&copy; 2026 Muhammed Sinan M', '<span class="copyright-pulse">&copy; 2026 Muhammed Sinan M</span>')

# 2i. Stagger delay for nav links
nav_links_html = '''<div class="nav-links">
                <a href="#about" onclick="closeMenu()">About</a>
                <a href="#education" onclick="closeMenu()">Education</a>
                <a href="#projects" onclick="closeMenu()">Projects</a>
                <a href="#experience" onclick="closeMenu()">Experience</a>
                <a href="#skills" onclick="closeMenu()">Skills</a>
                <a href="#clubs" onclick="closeMenu()">Clubs</a>
                <a href="#hackathons" onclick="closeMenu()">Hackathons</a>
                <a href="#certifications" onclick="closeMenu()">Certifications</a>
                <a href="#achievements" onclick="closeMenu()">Achievements</a>
                <a href="#contact" onclick="closeMenu()">Contact</a>
            </div>'''
nav_links_html_new = '''<div class="nav-links">
                <a href="#about" style="animation-delay: 0.05s;" onclick="closeMenu()">About</a>
                <a href="#education" style="animation-delay: 0.10s;" onclick="closeMenu()">Education</a>
                <a href="#projects" style="animation-delay: 0.15s;" onclick="closeMenu()">Projects</a>
                <a href="#experience" style="animation-delay: 0.20s;" onclick="closeMenu()">Experience</a>
                <a href="#skills" style="animation-delay: 0.25s;" onclick="closeMenu()">Skills</a>
                <a href="#clubs" style="animation-delay: 0.30s;" onclick="closeMenu()">Clubs</a>
                <a href="#hackathons" style="animation-delay: 0.35s;" onclick="closeMenu()">Hackathons</a>
                <a href="#certifications" style="animation-delay: 0.40s;" onclick="closeMenu()">Certifications</a>
                <a href="#achievements" style="animation-delay: 0.45s;" onclick="closeMenu()">Achievements</a>
                <a href="#contact" style="animation-delay: 0.50s;" onclick="closeMenu()">Contact</a>
            </div>'''
content = content.replace(nav_links_html, nav_links_html_new)


# ==========================================
# 3. JAVASCRIPT INJECTIONS
# ==========================================
js_injection = '''
        // --- ANIMATIONS JS ---
        // 1. Navbar scroll effect
        const nav = document.querySelector('nav');
        window.addEventListener('scroll', () => {
            if(window.scrollY > 80) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');
        });

        // 2. Active Section Highlighting
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-links a');
        const observer_active = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    navLinks.forEach(link => {
                        link.classList.remove('active');
                        if(link.getAttribute('href') === '#' + entry.target.id) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, { threshold: 0.3 });
        sections.forEach(sec => observer_active.observe(sec));

        // 3. Stagger Cards Logic
        document.querySelectorAll('.projects, .achievements-grid, #experience .projects, #hackathons .projects').forEach(grid => {
            const cards = grid.querySelectorAll('.card');
            cards.forEach((card, index) => {
                card.style.transitionDelay = `${index * 0.1}s`;
            });
        });

        // 4. Stagger Stats Logic
        const statCols = document.querySelectorAll('.stat-col');
        statCols.forEach((col, index) => {
            col.style.transitionDelay = `${index * 0.15}s`;
        });
        const observer_stats = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        });
        statCols.forEach(el => observer_stats.observe(el));

        // 5. Timeline markers observer
        const observer_markers = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) entry.target.classList.add('visible');
            });
        }, { threshold: 1 });
        document.querySelectorAll('.timeline-marker').forEach(el => observer_markers.observe(el));

        // 6. Skills Observer
        const observer_skills = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) entry.target.classList.add('visible');
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.skill-category').forEach(el => observer_skills.observe(el));

        // 7. Dark Toggle Flip Animation Listener
        const themeTgl = document.getElementById('themeToggle');
        if(themeTgl) {
            themeTgl.addEventListener('click', () => {
                themeTgl.classList.remove('flipping');
                void themeTgl.offsetWidth; // trigger reflow
                themeTgl.classList.add('flipping');
                setTimeout(() => themeTgl.classList.remove('flipping'), 400);
            });
        }
'''

if '// --- ANIMATIONS JS ---' not in content:
    content = content.replace('// Three.js Background', js_injection + '\n        // Three.js Background')


with open('index.html', 'w') as f:
    f.write(content)

print("Comprehensive animations successfully injected!")
