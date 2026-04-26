import re

with open('index.html', 'r') as f:
    content = f.read()

# Current nav block:
# <nav>
#     <h1>Sinan.</h1>
#     <a id="themeToggle" style="cursor: pointer; font-size: 16px; font-weight: 500; color: var(--text-primary); text-decoration: none; margin-left: auto; margin-right: 20px; transition: all 0.3s; display: inline-block;">Dark</a>
#     <button class="menu-toggle" onclick="toggleMenu()">☰</button>
#     <div class="nav-links">
#         ...
#         <a href="#contact" onclick="closeMenu()">Contact</a>
#     </div>
# </nav>

nav_pattern = r'(<nav>\s*<h1>Sinan\.</h1>)\s*<a id="themeToggle".*?</a>\s*<button class="menu-toggle" onclick="toggleMenu\(\)">☰</button>\s*(<div class="nav-links">.*?</div>)\s*</nav>'

replacement = r'''\1
            <div style="display: flex; align-items: center; gap: 20px; margin-left: auto;">
                \2
                <a id="themeToggle" style="cursor: pointer; font-size: 13px; font-weight: 600; color: #0a0f1e !important; background: #D4AF37; padding: 6px 16px; border-radius: 20px; text-decoration: none; transition: all 0.3s; display: inline-block;">Dark</a>
                <button class="menu-toggle" onclick="toggleMenu()" style="margin: 0;">☰</button>
            </div>
        </nav>'''

if re.search(nav_pattern, content, flags=re.DOTALL):
    content = re.sub(nav_pattern, replacement, content, flags=re.DOTALL)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Nav fixed!")
else:
    print("Pattern not found!")
