import re

with open('index.html', 'r') as f:
    content = f.read()

old_exp_block_pattern = r'<section id="experience" class="bg-light">\s*<div class="section-inner">\s*<h3 class="fade-in-up">Experience & Internship</h3>\s*<div class="timeline">\s*<div class="timeline-item">\s*<div class="timeline-marker"></div>\s*<div style="padding-left: 20px;">\s*<div class="card fade-in-up">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>'

new_exp_block = '''<section id="experience" class="bg-light">
            <div class="section-inner">
                <h3 class="fade-in-up">Experience & Internship</h3>
                <div class="timeline">
                    <!-- Internship Timeline Item -->
                    <div class="timeline-item">
                        <div class="timeline-marker"></div>
                        <div style="padding-left: 20px;">
                            <div class="card fade-in-up" style="display: flex; gap: 24px; align-items: stretch; flex-wrap: wrap;">
                                <div style="flex: 1; min-width: 250px; display: flex; flex-direction: column;">
                                    <div class="card-header">
                                        <h4>Research Intern</h4>
                                        <span class="badge">Internship</span>
                                    </div>
                                    <p style="color: var(--primary-navy); font-size: 16px; font-weight: 600; margin-bottom: 4px;">Suvidha Foundation (Suvidha Mahila Mandal)</p>
                                    <p style="color: var(--accent-blue); font-size: 14px; font-weight: 500; margin-bottom: 12px;">25 Mar 2026 – 25 Apr 2026</p>
                                    <p>Completed an internship programme at Suvidha Foundation in collaboration with Code Karo Yaaro. Was recognized for being punctual and inquisitive throughout the programme.</p>
                                    <p style="font-size: 14px; color: var(--text-secondary); margin-bottom: 20px;"><strong>Certificate ID:</strong> SMM222324827</p>
                                    <a href="https://suvidhafoundationedutech.org/verify" target="_blank" rel="noopener noreferrer" class="btn" style="text-align: center; margin-top: auto;">Verify Certificate</a>
                                </div>
                                <div style="flex: 0 0 280px; max-width: 100%; display: flex; align-items: center; justify-content: center;">
                                    <img src="images/certificates/thumb_IE-HK-26-2027.jpg" alt="Internship Certificate" style="width: 100%; height: 210px; object-fit: contain; background: #fff; border-radius: 8px; border: 1px solid var(--border-gray);">
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- NSS Timeline Item -->
                    <div class="timeline-item">
                        <div class="timeline-marker"></div>
                        <div style="padding-left: 20px;">
                            <div class="card fade-in-up" style="display: flex; gap: 24px; align-items: stretch; flex-wrap: wrap;">
                                <div style="flex: 1; min-width: 250px; display: flex; flex-direction: column;">
                                    <div class="card-header">
                                        <h4>NSS Volunteer Leader</h4>
                                        <span class="badge">Volunteer</span>
                                    </div>
                                    <p style="color: var(--primary-navy); font-size: 16px; font-weight: 600; margin-bottom: 4px;">MES HSS Irimbiliyam</p>
                                    <p style="color: var(--accent-blue); font-size: 14px; font-weight: 500; margin-bottom: 12px;">2023 – 2025</p>
                                    <p style="margin-bottom: 20px;">Led community programs, coordinated events, managed digital content and campaigns. Completed 240+ certified volunteer hours and developed strong leadership skills.</p>
                                    <a href="images/certificates/1753219537959.jpeg" target="_blank" rel="noopener noreferrer" class="btn" style="text-align: center; margin-top: auto;">View Certificate</a>
                                </div>
                                <div style="flex: 0 0 280px; max-width: 100%; display: flex; align-items: center; justify-content: center;">
                                    <img src="images/certificates/1753219537959.jpeg" alt="NSS Volunteer Certificate" style="width: 100%; height: 210px; object-fit: contain; background: #fff; border-radius: 8px; border: 1px solid var(--border-gray);">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

if re.search(old_exp_block_pattern, content, flags=re.DOTALL):
    content = re.sub(old_exp_block_pattern, new_exp_block, content, flags=re.DOTALL)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Experience section updated.")
else:
    print("Pattern not found!")
