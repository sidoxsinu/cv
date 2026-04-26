import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Dark Mode / Light Mode Toggle: 
old_script_start = '    <style>\n        .dark-mode {'
old_script_end = '    </script>\n</body>'

if old_script_start in content and old_script_end in content:
    content = content[:content.find(old_script_start)] + "</body>"
else:
    print("Warning: old script chunk not found!")

new_injection = '''
    <style>
        html[data-theme="dark"] {
            --white: #0a0f1e;
            --light-gray: #111827;
            --primary-navy: #f0f0f0;
            --charcoal-gray: #f0f0f0;
            --text-primary: #f0f0f0;
            --border-gray: #2a3b5c;
        }
        html[data-theme="dark"] body {
            background-color: var(--white);
            color: var(--text-primary);
        }
        html[data-theme="dark"] .bg-light {
            background-color: #0a0f1e !important;
        }
        
        #themeToggle:hover {
            text-decoration: underline;
        }

        /* Achievements specific styles */
        #achievements .card {
            border-left: 3px solid #D4AF37;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Dark Mode Logic
        const themeToggle = document.getElementById('themeToggle');
        const root = document.documentElement;
        
        function setTheme(theme) {
            if (theme === 'dark') {
                root.setAttribute('data-theme', 'dark');
                if(themeToggle) themeToggle.textContent = 'Light';
                localStorage.setItem('theme', 'dark');
            } else {
                root.removeAttribute('data-theme');
                if(themeToggle) themeToggle.textContent = 'Dark';
                localStorage.setItem('theme', 'light');
            }
        }
        
        if(localStorage.getItem('theme') === 'dark') {
            setTheme('dark');
        } else {
            setTheme('light');
        }

        if(themeToggle) {
            themeToggle.addEventListener('click', () => {
                if(root.getAttribute('data-theme') === 'dark') {
                    setTheme('light');
                } else {
                    setTheme('dark');
                }
            });
        }

        // Three.js Background
        const heroSection = document.querySelector('.hero');
        if (heroSection) {
            heroSection.style.position = 'relative';
            heroSection.style.zIndex = '1';
            
            const heroInner = heroSection.querySelector('.section-inner');
            if(heroInner) {
                heroInner.style.position = 'relative';
                heroInner.style.zIndex = '2';
            }
            
            const canvas = document.createElement('canvas');
            canvas.style.position = 'absolute';
            canvas.style.top = '0';
            canvas.style.left = '0';
            canvas.style.width = '100%';
            canvas.style.height = '100%';
            canvas.style.zIndex = '0';
            canvas.style.pointerEvents = 'none';
            heroSection.insertBefore(canvas, heroSection.firstChild);

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, heroSection.clientWidth / heroSection.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
            renderer.setSize(heroSection.clientWidth, heroSection.clientHeight);
            renderer.setPixelRatio(window.devicePixelRatio);

            const geometry = new THREE.IcosahedronGeometry(1.5, 0);
            
            const material = new THREE.MeshBasicMaterial({ 
                color: 0x0f1e50, 
                wireframe: true, 
                transparent: true, 
                opacity: 0.18
            });

            const meshes = [];
            for (let i = 0; i < 20; i++) {
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.set((Math.random() - 0.5) * 25, (Math.random() - 0.5) * 25, (Math.random() - 0.5) * 15 - 5);
                mesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);
                mesh.userData = {
                    rx: (Math.random() - 0.5) * 0.005,
                    ry: (Math.random() - 0.5) * 0.005,
                    dx: (Math.random() - 0.5) * 0.01,
                    dy: (Math.random() - 0.5) * 0.01
                };
                scene.add(mesh);
                meshes.push(mesh);
            }
            camera.position.z = 12;

            let mouseX = 0;
            let mouseY = 0;
            document.addEventListener('mousemove', (e) => {
                mouseX = (e.clientX / window.innerWidth) * 2 - 1;
                mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
            });

            window.addEventListener('resize', () => {
                if (!heroSection) return;
                camera.aspect = heroSection.clientWidth / heroSection.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(heroSection.clientWidth, heroSection.clientHeight);
            });

            function animate() {
                if (document.visibilityState === 'visible') {
                    const isDark = root.getAttribute('data-theme') === 'dark';
                    material.color.setHex(isDark ? 0x6496ff : 0x0f1e50);
                    material.opacity = isDark ? 0.12 : 0.18;

                    meshes.forEach(mesh => {
                        mesh.position.x += mesh.userData.dx;
                        mesh.position.y += mesh.userData.dy;
                        
                        mesh.rotation.x += mesh.userData.rx + (mouseY * 0.002);
                        mesh.rotation.y += mesh.userData.ry + (mouseX * 0.002);
                        
                        if (mesh.position.x > 15 || mesh.position.x < -15) mesh.userData.dx *= -1;
                        if (mesh.position.y > 15 || mesh.position.y < -15) mesh.userData.dy *= -1;
                    });
                    renderer.render(scene, camera);
                }
                requestAnimationFrame(animate);
            }
            animate();
        }
        
        // Recognition Toggle Logic
        function toggleRecognition() {
            const content = document.getElementById('recognition-links');
            const btn = document.getElementById('recognition-toggle-btn');
            if(content.style.display === 'none') {
                content.style.display = 'flex';
                btn.textContent = '📎 Hide Recognition ↑';
            } else {
                content.style.display = 'none';
                btn.textContent = '📎 View Recognition →';
            }
        }
    </script>
</body>'''

content = content.replace('</body>', new_injection)

# 2. Fix Next Gen AI Assistant Project Card (Lines 164-172 replacement)
old_card_end_pattern = r'<div style="border-top: 1px solid var\(--border-gray\); padding-top: 16px; font-size: 13px; color: var\(--text-secondary\); line-height: 1\.5;">.*?</div>\s*</div>'

new_card_end = '''<div style="border-top: 1px solid var(--border-gray); padding-top: 16px; margin-bottom: 16px;">
                            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; text-align: left;">
                                <div style="border-right: 1px solid var(--border-gray); padding-right: 10px;">
                                    <div style="font-size: 0.65rem; letter-spacing: 0.08em; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 4px;">Event</div>
                                    <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-primary);">Build with AI</div>
                                </div>
                                <div style="border-right: 1px solid var(--border-gray); padding-right: 10px;">
                                    <div style="font-size: 0.65rem; letter-spacing: 0.08em; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 4px;">Organized By</div>
                                    <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-primary);">Google Developers</div>
                                </div>
                                <div>
                                    <div style="font-size: 0.65rem; letter-spacing: 0.08em; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 4px;">Recognition</div>
                                    <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-primary);">Best Technical Project</div>
                                </div>
                            </div>
                        </div>

                        <div style="font-size: 13px; color: var(--text-secondary); line-height: 1.5;">
                            <span style="font-size: 0.75rem; letter-spacing: 0.05em; text-transform: uppercase; margin-right: 8px;">As Featured In</span>
                            
                            <a href="javascript:void(0)" id="recognition-toggle-btn" onclick="toggleRecognition()" style="color: var(--text-secondary); text-decoration: none; border-bottom: 1px solid transparent; transition: all 0.2s;">📎 View Recognition →</a>
                            
                            <div id="recognition-links" style="display: none; flex-direction: column; gap: 8px; margin-top: 12px; padding-left: 12px; border-left: 2px solid var(--border-gray);">
                                <a href="https://www.linkedin.com/posts/mulearn-nssce_engineering-excellence-at-its-best-congratulations-activity-7453323334664200192-6xAI" target="_blank" class="minimal-link" style="color: var(--text-secondary); text-decoration: none;">🔗 MuLearn NSSCE (LinkedIn)</a>
                                <a href="https://www.linkedin.com/posts/mulearn-nssce_buildwithai-buildwithaixasulearn-buildwithaipalakkad-activity-7453136864355557376-I1J3" target="_blank" class="minimal-link" style="color: var(--text-secondary); text-decoration: none;">📣 Event Post (LinkedIn)</a>
                                <a href="https://www.instagram.com/p/DXjRXeCk9Ry/" target="_blank" class="minimal-link" style="color: var(--text-secondary); text-decoration: none;">📸 Christ College of Engineering (Instagram)</a>
                                <a href="https://www.instagram.com/p/DXgG9EDj1Du/" target="_blank" class="minimal-link" style="color: var(--text-secondary); text-decoration: none;">📸 MuLearn & MU Campus (Instagram)</a>
                            </div>
                        </div>
                    </div>'''

if not re.search(old_card_end_pattern, content, flags=re.DOTALL):
    print("Warning: old card end pattern not found!")
else:
    content = re.sub(old_card_end_pattern, new_card_end, content, flags=re.DOTALL)

# 3. Add Achievements & Recognition Section between Projects and Experience
achievements_section = '''
        <!-- ACHIEVEMENTS -->
        <section id="achievements">
            <div class="section-inner">
                <h3>Achievements & Recognition</h3>
                <div class="projects">
                    <div class="card">
                        <div class="card-header" style="margin-bottom: 8px;">
                            <h4 style="margin: 0; color: var(--primary-navy); font-size: 1.1rem;">🏆 Best Technical Project — Google for Developers NSSCE Build with AI Hackathon</h4>
                        </div>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px; font-weight: 500;">Organized by MuLearn NSSCE · Mar 2026</p>
                        <p style="margin-bottom: 16px;">Next Gen AI Assistant recognized for technical excellence and innovation among all competing teams.</p>
                        
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <a href="https://www.linkedin.com/posts/mulearn-nssce_engineering-excellence-at-its-best-congratulations-activity-7453323334664200192-6xAI" target="_blank" class="minimal-link" style="font-size: 0.85rem; color: var(--text-secondary); text-decoration: none;">🔗 MuLearn NSSCE (LinkedIn)</a>
                            <a href="https://www.linkedin.com/posts/mulearn-nssce_buildwithai-buildwithaixasulearn-buildwithaipalakkad-activity-7453136864355557376-I1J3" target="_blank" class="minimal-link" style="font-size: 0.85rem; color: var(--text-secondary); text-decoration: none;">📣 Event Post (LinkedIn)</a>
                            <a href="https://www.instagram.com/p/DXjRXeCk9Ry/" target="_blank" class="minimal-link" style="font-size: 0.85rem; color: var(--text-secondary); text-decoration: none;">📸 Christ College of Engineering (Instagram)</a>
                            <a href="https://www.instagram.com/p/DXgG9EDj1Du/" target="_blank" class="minimal-link" style="font-size: 0.85rem; color: var(--text-secondary); text-decoration: none;">📸 MuLearn & MU Campus (Instagram)</a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-header" style="margin-bottom: 8px;">
                            <h4 style="margin: 0; color: var(--primary-navy); font-size: 1.1rem;">🏆 Webathon Runner Up</h4>
                        </div>
                        <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px; font-weight: 500;">Organized by Webathon · 2024</p>
                        <p style="margin-bottom: 16px;">Pylon: an all-in-one scholarship search platform recognized as Runner Up at the Webathon.</p>
                        <a href="https://pylon-topaz.vercel.app" target="_blank" class="minimal-link" style="font-size: 0.85rem; color: var(--text-secondary); text-decoration: none;">🔗 View Project</a>
                    </div>
                </div>
            </div>
        </section>

'''

if '<section id="achievements"' not in content:
    content = content.replace('<section id="experience"', achievements_section + '<section id="experience"')

if 'href="#achievements"' not in content:
    content = content.replace('<a href="#experience"', '<a href="#achievements" onclick="closeMenu()">Achievements</a>\n                <a href="#experience"')

with open('index.html', 'w') as f:
    f.write(content)
print("Fixes applied.")
