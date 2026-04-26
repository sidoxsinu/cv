import re

with open('index.html', 'r') as f:
    content = f.read()

# We need to replace the entire <section id="experience"> block
exp_pattern = r'<section id="experience" class="bg-light">.*?</section>'

new_exp = '''<section id="experience" class="bg-light">
            <div class="section-inner">
                <h3 class="fade-in-up">Experience & Internship</h3>
                <div class="projects">
                    
                    <div class="card fade-in-up" style="display: flex; flex-direction: column;">
                        <div class="card-header">
                            <h4>Research Intern</h4>
                            <span class="badge">Internship</span>
                        </div>
                        <p style="color: var(--primary-navy); font-size: 16px; font-weight: 600; margin-bottom: 4px;">Suvidha Foundation (Suvidha Mahila Mandal)</p>
                        <p style="color: var(--accent-blue); font-size: 14px; font-weight: 500; margin-bottom: 12px;">25 Mar 2026 – 25 Apr 2026</p>
                        <p>Completed an internship programme at Suvidha Foundation in collaboration with Code Karo Yaaro. Was recognized for being punctual and inquisitive throughout the programme.</p>
                        <p style="font-size: 14px; color: var(--text-secondary); margin-bottom: 20px;"><strong>Certificate ID:</strong> SMM222324827</p>
                        
                        <div style="margin-top: auto; display: flex; flex-direction: column; align-items: center; gap: 16px; padding-top: 20px;">
                            <img src="images/certificates/thumb_IE-HK-26-2027.jpg" alt="Internship Certificate" style="width: 100%; max-width: 280px; height: 200px; object-fit: contain; background: #fff; border-radius: 8px; border: 1px solid var(--border-gray);">
                            <a href="https://suvidhafoundationedutech.org/verify" target="_blank" rel="noopener noreferrer" class="btn" style="width: 100%; text-align: center;">Verify Certificate</a>
                        </div>
                    </div>

                    <div class="card fade-in-up" style="display: flex; flex-direction: column;">
                        <div class="card-header">
                            <h4>NSS Volunteer Leader</h4>
                            <span class="badge">Volunteer</span>
                        </div>
                        <p style="color: var(--primary-navy); font-size: 16px; font-weight: 600; margin-bottom: 4px;">MES HSS Irimbiliyam</p>
                        <p style="color: var(--accent-blue); font-size: 14px; font-weight: 500; margin-bottom: 12px;">2023 – 2025</p>
                        <p style="margin-bottom: 20px;">Led community programs, coordinated events, managed digital content and campaigns. Completed 240+ certified volunteer hours and developed strong leadership skills.</p>
                        
                        <div style="margin-top: auto; display: flex; flex-direction: column; align-items: center; gap: 16px; padding-top: 20px;">
                            <img src="images/certificates/1753219537959.jpeg" alt="NSS Volunteer Certificate" style="width: 100%; max-width: 280px; height: 200px; object-fit: contain; background: #fff; border-radius: 8px; border: 1px solid var(--border-gray);">
                            <a href="images/certificates/1753219537959.jpeg" target="_blank" rel="noopener noreferrer" class="btn" style="width: 100%; text-align: center;">View Certificate</a>
                        </div>
                    </div>

                </div>
            </div>
        </section>'''

if re.search(exp_pattern, content, flags=re.DOTALL):
    content = re.sub(exp_pattern, new_exp, content, flags=re.DOTALL)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Reverted to grid and fixed layout!")
else:
    print("Pattern not found!")
