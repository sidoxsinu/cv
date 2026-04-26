import re
import base64

with open('index.html', 'r') as f:
    content = f.read()

# 1. Navbar: Insert Dark Mode Toggle
nav_pattern = r'<button class="menu-toggle"'
nav_replacement = r'<a id="themeToggle" style="cursor: pointer; font-size: 16px; font-weight: 500; color: var(--text-primary); text-decoration: none; margin-left: auto; margin-right: 20px; transition: all 0.3s; display: inline-block;">Dark</a>\n            <button class="menu-toggle"'

if '<a id="themeToggle"' not in content:
    content = re.sub(nav_pattern, nav_replacement, content, count=1)

# 2. Hero Section: Replace Download CV Button with minimal text link
with open('images/cv/Muhammed Sinan M.pdf', 'rb') as f:
    pdf_b64 = base64.b64encode(f.read()).decode('utf-8')
pdf_data_uri = f"data:application/pdf;base64,{pdf_b64}"

hero_pattern = r'<a class="hero-link" href="#projects">View My Work →</a>'
hero_replacement = f'''<div style="display: flex; gap: 24px; justify-content: center; align-items: center; margin-top: 20px; flex-wrap: wrap;">
                    <a class="hero-link" href="#projects" style="margin: 0;">View My Work →</a>
                    <a class="hero-link" href="{pdf_data_uri}" download="Muhammed_Sinan_M_Resume.pdf" style="margin: 0; border: none; background: transparent; padding: 0;">Download CV →</a>
                </div>'''

if 'Download CV →' not in content:
    content = content.replace(hero_pattern, hero_replacement)

# 3, 5. Inject Dark Mode CSS and Three.js Script
injection = '''
    <style>
        .dark-mode {
            --primary-navy: #f3f4f6;
            --charcoal-gray: #f3f4f6;
            --white: #0a0f1e;
            --light-gray: #111827;
            --border-gray: #374151;
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
        }
        
        #themeToggle:hover {
            text-decoration: underline;
            color: var(--accent-blue);
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // Dark Mode Logic
        const themeToggle = document.getElementById('themeToggle');
        const root = document.documentElement;
        if(localStorage.getItem('theme') === 'dark') {
            root.classList.add('dark-mode');
            if(themeToggle) themeToggle.textContent = 'Light';
        }
        if(themeToggle) {
            themeToggle.addEventListener('click', () => {
                root.classList.toggle('dark-mode');
                if(root.classList.contains('dark-mode')) {
                    localStorage.setItem('theme', 'dark');
                    themeToggle.textContent = 'Light';
                } else {
                    localStorage.setItem('theme', 'light');
                    themeToggle.textContent = 'Dark';
                }
            });
        }

        // Three.js Background
        const heroSection = document.querySelector('.hero');
        if (heroSection) {
            heroSection.style.position = 'relative';
            heroSection.style.zIndex = '1';
            heroSection.style.overflow = 'hidden';
            
            const canvas = document.createElement('canvas');
            canvas.style.position = 'absolute';
            canvas.style.top = '0';
            canvas.style.left = '0';
            canvas.style.width = '100%';
            canvas.style.height = '100%';
            canvas.style.zIndex = '-1';
            canvas.style.pointerEvents = 'none';
            heroSection.insertBefore(canvas, heroSection.firstChild);

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, heroSection.clientWidth / heroSection.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
            renderer.setSize(heroSection.clientWidth, heroSection.clientHeight);
            renderer.setPixelRatio(window.devicePixelRatio);

            const geometry = new THREE.IcosahedronGeometry(1, 0);
            const material = new THREE.MeshBasicMaterial({ 
                color: root.classList.contains('dark-mode') ? 0x6496ff : 0x0f1e50, 
                wireframe: true, 
                transparent: true, 
                opacity: root.classList.contains('dark-mode') ? 0.12 : 0.15 
            });
            
            const observer = new MutationObserver(() => {
                if (root.classList.contains('dark-mode')) {
                    material.color.setHex(0x6496ff);
                    material.opacity = 0.12;
                } else {
                    material.color.setHex(0x0f1e50);
                    material.opacity = 0.15;
                }
            });
            observer.observe(root, { attributes: true, attributeFilter: ['class'] });

            const meshes = [];
            for (let i = 0; i < 15; i++) {
                const mesh = new THREE.Mesh(geometry, material);
                mesh.position.set((Math.random() - 0.5) * 20, (Math.random() - 0.5) * 20, (Math.random() - 0.5) * 10 - 5);
                mesh.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, 0);
                mesh.userData = {
                    rx: (Math.random() - 0.5) * 0.01,
                    ry: (Math.random() - 0.5) * 0.01,
                    dx: (Math.random() - 0.5) * 0.02,
                    dy: (Math.random() - 0.5) * 0.02
                };
                scene.add(mesh);
                meshes.push(mesh);
            }
            camera.position.z = 10;

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
                    meshes.forEach(mesh => {
                        mesh.rotation.x += mesh.userData.rx;
                        mesh.rotation.y += mesh.userData.ry;
                        mesh.position.x += mesh.userData.dx + (mouseX * 0.01);
                        mesh.position.y += mesh.userData.dy + (mouseY * 0.01);
                        
                        if (mesh.position.x > 15 || mesh.position.x < -15) mesh.userData.dx *= -1;
                        if (mesh.position.y > 15 || mesh.position.y < -15) mesh.userData.dy *= -1;
                    });
                    renderer.render(scene, camera);
                }
                requestAnimationFrame(animate);
            }
            animate();
        }
    </script>
</body>'''

if 'themeToggle.addEventListener' not in content:
    content = content.replace('</body>', injection)

with open('index.html', 'w') as f:
    f.write(content)

print("Applied fixes successfully.")
