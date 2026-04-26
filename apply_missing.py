import re
import base64

with open('index.html', 'r') as f:
    content = f.read()

# --- 1. Typing Animation in Hero ---
subtitle_pattern = r'<p>Computer Science & Engineering Student \| Full-Stack Web Developer \| AI Enthusiast</p>'
subtitle_replacement = r'''<p>Computer Science & Engineering Student | <span id="typing-text">Full-Stack Web Developer</span><span class="cursor">|</span></p>'''
if '<span id="typing-text">' not in content:
    content = re.sub(subtitle_pattern, subtitle_replacement, content)

typing_script = '''
        // Typing Animation
        const phrases = ["Full-Stack Web Developer", "AI Enthusiast", "Hackathon Winner 🏆", "Open to Internships"];
        let pIndex = 0;
        let cIndex = 0;
        let isDeleting = false;
        const typingEl = document.getElementById('typing-text');
        
        function typeEffect() {
            if (!typingEl) return;
            const current = phrases[pIndex];
            if (isDeleting) {
                typingEl.textContent = current.substring(0, cIndex - 1);
                cIndex--;
            } else {
                typingEl.textContent = current.substring(0, cIndex + 1);
                cIndex++;
            }

            let typeSpeed = isDeleting ? 50 : 100;
            if (!isDeleting && cIndex === current.length) {
                typeSpeed = 2000;
                isDeleting = true;
            } else if (isDeleting && cIndex === 0) {
                isDeleting = false;
                pIndex = (pIndex + 1) % phrases.length;
                typeSpeed = 500;
            }
            setTimeout(typeEffect, typeSpeed);
        }
        if(typingEl) setTimeout(typeEffect, 1000);
'''
if 'const phrases =' not in content:
    content = content.replace('// Three.js Background', typing_script + '\n        // Three.js Background')

css_typing = '''
        .cursor {
            animation: blink 1s step-end infinite;
        }
        @keyframes blink { 50% { opacity: 0; } }
'''
if '.cursor {' not in content:
    content = content.replace('</style>', css_typing + '    </style>')


# --- 2. GitHub Stats Strip ---
skills_end_pattern = r'(<section id="skills".*?</div>\s*)</section>'
stats_strip = '''
                <div style="margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border-gray);">
                    <h4 style="margin-bottom: 20px; text-align: center; color: var(--primary-navy);">GitHub Activity</h4>
                    <div style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
                        <img class="gh-stat-light" src="https://github-readme-stats.vercel.app/api?username=sidoxsinu&show_icons=true&theme=transparent&hide_border=true" alt="GitHub Stats">
                        <img class="gh-stat-light" src="https://github-readme-stats.vercel.app/api/top-langs/?username=sidoxsinu&layout=compact&hide_border=true" alt="Top Languages">
                        
                        <img class="gh-stat-dark" src="https://github-readme-stats.vercel.app/api?username=sidoxsinu&show_icons=true&theme=transparent&hide_border=true&title_color=f3f4f6&text_color=9ca3af&icon_color=6496ff" alt="GitHub Stats" style="display: none;">
                        <img class="gh-stat-dark" src="https://github-readme-stats.vercel.app/api/top-langs/?username=sidoxsinu&layout=compact&theme=transparent&hide_border=true&title_color=f3f4f6&text_color=9ca3af" alt="Top Languages" style="display: none;">
                    </div>
                </div>
'''
if 'GitHub Activity' not in content:
    match = re.search(skills_end_pattern, content, flags=re.DOTALL)
    if match:
        content = content[:match.end(1)] + stats_strip + content[match.end(1):]

css_stats = '''
        html[data-theme="dark"] .gh-stat-light { display: none !important; }
        html[data-theme="dark"] .gh-stat-dark { display: block !important; }
'''
if '.gh-stat-light {' not in content:
    content = content.replace('</style>', css_stats + '    </style>')


# --- 3. Timeline for Experience ---
exp_pattern = r'(<section id="experience" class="bg-light">\s*<div class="section-inner">\s*<h3>Experience & Internship</h3>\s*)<div class="projects">\s*(<div class="card">.*?)</div>\s*</div>\s*</section>'
match = re.search(exp_pattern, content, re.DOTALL)
if match and '<div class="timeline">' not in match.group(0):
    exp_intro = match.group(1)
    exp_card = match.group(2) + '</div>' # close the card
    timeline_html = f'''<div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-marker"></div>
                        <div style="padding-left: 20px;">
                            {exp_card}
                        </div>
                    </div>
                </div>'''
    content = content[:match.start()] + exp_intro + timeline_html + '\n            </div>\n        </section>' + content[match.end():]


# --- 4. Back to Top Button ---
btt_html = '''<button id="btt" style="position: fixed; bottom: 30px; right: 30px; background: var(--primary-navy); color: var(--white); width: 45px; height: 45px; border-radius: 50%; border: none; font-size: 20px; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.15); opacity: 0; pointer-events: none; transition: opacity 0.3s; z-index: 100;">↑</button>'''
if '<button id="btt"' not in content:
    content = content.replace('</body>', btt_html + '\n</body>')

btt_script = '''
        // Back to Top Button
        const btt = document.getElementById('btt');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                btt.style.opacity = '1';
                btt.style.pointerEvents = 'auto';
            } else {
                btt.style.opacity = '0';
                btt.style.pointerEvents = 'none';
            }
        });
        if(btt) btt.addEventListener('click', () => window.scrollTo({top: 0, behavior: 'smooth'}));
'''
if 'const btt = document.getElementById' not in content:
    content = content.replace('// Three.js Background', btt_script + '\n        // Three.js Background')


# --- 5. Scroll Fade-in Animations ---
css_fade = '''
        .fade-in-up {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        .fade-in-up.visible {
            opacity: 1;
            transform: translateY(0);
        }
'''
if '.fade-in-up {' not in content:
    content = content.replace('</style>', css_fade + '    </style>')

# Add classes to h3 and .card if not already present
content = re.sub(r'<h3>', r'<h3 class="fade-in-up">', content)
content = re.sub(r'<div class="card">', r'<div class="card fade-in-up">', content)
content = re.sub(r'<div class="card" style="border-left: 3px solid #D4AF37;">', r'<div class="card fade-in-up" style="border-left: 3px solid #D4AF37;">', content)

fade_script = '''
        // Scroll Fade-in Observer
        const observer_fade = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.fade-in-up').forEach(el => observer_fade.observe(el));
'''
if 'const observer_fade' not in content:
    content = content.replace('// Three.js Background', fade_script + '\n        // Three.js Background')


# --- 6. Favicon & OG Meta Tags ---
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" fill="%23ffffff"/><text x="50" y="65" font-family="sans-serif" font-weight="bold" font-size="45" fill="%230a0f1e" text-anchor="middle">SM</text></svg>'''
favicon_b64 = "data:image/svg+xml;base64," + base64.b64encode(favicon_svg.encode()).decode()

head_meta = f'''
    <link rel="icon" href="{favicon_b64}">
    <meta property="og:title" content="Muhammed Sinan M | Portfolio">
    <meta property="og:description" content="CSE Student | Full-Stack Developer | AI Enthusiast | Hackathon Winner — Best Technical Project at Google for Developers Build with AI">
    <meta property="og:type" content="website">
    <meta property="og:url" content="">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="description" content="CSE Student | Full-Stack Developer | AI Enthusiast | Hackathon Winner — Best Technical Project at Google for Developers Build with AI">
'''
if 'og:title' not in content:
    content = content.replace('<title>Muhammed Sinan M | Portfolio</title>', '<title>Muhammed Sinan M | Portfolio</title>' + head_meta)


# --- 7. Footer Upgrade ---
footer_replacement = '''
        <!-- FOOTER -->
        <footer>
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; padding: 40px 10%; background: var(--primary-navy); color: #f0f0f0;">
                <div style="flex: 1; min-width: 250px;">
                    <h3 style="color: #f0f0f0; margin-bottom: 8px;">Muhammed Sinan M</h3>
                    <p style="color: rgba(240,240,240,0.7); font-size: 14px;">Building the future, one line at a time.</p>
                </div>
                <div style="flex: 1; min-width: 250px; text-align: center;">
                    <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                        <a href="#about" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">About</a>
                        <a href="#projects" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">Projects</a>
                        <a href="#experience" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">Experience</a>
                        <a href="#achievements" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">Achievements</a>
                        <a href="#contact" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">Contact</a>
                    </div>
                </div>
                <div style="flex: 1; min-width: 250px; text-align: right;">
                    <div style="display: flex; gap: 15px; justify-content: flex-end;">
                        <a href="https://github.com/sidoxsinu" target="_blank" rel="noopener noreferrer" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">GitHub</a>
                        <a href="https://www.linkedin.com/in/sidoxsinu/" target="_blank" rel="noopener noreferrer" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">LinkedIn</a>
                        <a href="mailto:muhammedsinan.m67@gmail.com" style="color: rgba(240,240,240,0.8); text-decoration: none; font-size: 14px;">Email</a>
                    </div>
                </div>
            </div>
            <div style="text-align: center; padding: 20px; background: #081022; color: rgba(240,240,240,0.5); font-size: 12px;">
                &copy; 2026 Muhammed Sinan M &middot; All Rights Reserved
            </div>
        </footer>
    </div>'''

if '<footer>' not in content:
    content = content.replace('    </div>\n\n    <script>', footer_replacement + '\n\n    <script>')


# --- 8. Project GitHub Links ---
content = content.replace('href="https://next-gen-ai-assistant-system-mh9wy391u-sidoxsinus-projects.vercel.app"', 'href="https://github.com/sidoxsinu/next-gen-ai-assistant-system"')
content = content.replace('href="https://pylon-topaz.vercel.app"', 'href="https://github.com/sidoxsinu/Pylon"')
content = content.replace('href="https://code-burry.vercel.app"', 'href="https://github.com/sidoxsinu/CodeBurry"')

silentguard_pattern = r'(<h4>SilentGuard</h4>.*?<div class="tags">.*?</div>)\s*(</div>)'
silentguard_replacement = r'\1\n                        <a href="https://github.com/sidoxsinu/SilentGuard" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Project →</a>\n                    \2'
content = re.sub(silentguard_pattern, silentguard_replacement, content, flags=re.DOTALL)

aivoice_pattern = r'(<h4>AI Voice Assistant</h4>.*?<div class="tags">.*?</div>)\s*(</div>)'
aivoice_replacement = r'\1\n                        <a href="https://github.com/sidoxsinu/AI-Voice-Assistant" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Project →</a>\n                    \2'
content = re.sub(aivoice_pattern, aivoice_replacement, content, flags=re.DOTALL)

# Add rel="noopener noreferrer" safely
content = content.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
content = content.replace('rel="noopener noreferrer" rel="noopener noreferrer"', 'rel="noopener noreferrer"')


# --- 9. Add New Project - UniversityHub ---
universityhub_html = '''
                    <div class="card fade-in-up">
                        <div class="card-header">
                            <h4>UniversityHub</h4>
                        </div>
                        <p>A university platform built for students — centralizing resources, information, and tools in one place using vanilla JavaScript.</p>
                        <div class="tags">
                            <span class="tag">HTML/CSS</span>
                            <span class="tag">JavaScript</span>
                        </div>
                        <a href="https://github.com/sidoxsinu/universityhub" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Project →</a>
                    </div>
'''
pylon_end_pattern = r'(<h4>Pylon</h4>.*?<a href="https://github\.com/sidoxsinu/Pylon".*?</a>\s*</div>)'
if '<h4>UniversityHub</h4>' not in content:
    content = re.sub(pylon_end_pattern, r'\1' + universityhub_html, content, flags=re.DOTALL)


with open('index.html', 'w') as f:
    f.write(content)

print("Successfully applied the 9 remaining features!")
