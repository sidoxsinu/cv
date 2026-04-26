import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Next Gen AI Assistant
pattern_ai = r'<a href="https://github\.com/sidoxsinu/next-gen-ai-assistant-system"\s*target="_blank" rel="noopener noreferrer" class="card-link" style="margin-bottom: 24px;">View Project →</a>'
replacement_ai = r'''<div style="display: flex; gap: 12px; margin-bottom: 24px;">
                            <a href="https://next-gen-ai-assistant-system-mh9wy391u-sidoxsinus-projects.vercel.app" target="_blank" rel="noopener noreferrer" class="card-link" style="margin: 0;">Live Demo ↗</a>
                            <a href="https://github.com/sidoxsinu/next-gen-ai-assistant-system" target="_blank" rel="noopener noreferrer" class="card-link" style="margin: 0;">View Repository ↗</a>
                        </div>'''
content = re.sub(pattern_ai, replacement_ai, content)

# 2. Pylon
pattern_pylon = r'<a href="https://github\.com/sidoxsinu/Pylon" target="_blank" rel="noopener noreferrer" class="card-link">View Project →</a>'
replacement_pylon = r'''<div style="display: flex; gap: 12px; margin-top: auto;">
                            <a href="https://pylon-topaz.vercel.app" target="_blank" rel="noopener noreferrer" class="card-link" style="margin: 0;">Live Demo ↗</a>
                            <a href="https://github.com/sidoxsinu/Pylon" target="_blank" rel="noopener noreferrer" class="card-link" style="margin: 0;">View Repository ↗</a>
                        </div>'''
content = content.replace('<a href="https://github.com/sidoxsinu/Pylon" target="_blank" rel="noopener noreferrer" class="card-link">View Project →</a>', replacement_pylon)

# 3. CodeBurry
pattern_cb = r'<a href="https://github\.com/sidoxsinu/CodeBurry" target="_blank" rel="noopener noreferrer" class="card-link">View Project →</a>'
replacement_cb = r'''<div style="display: flex; gap: 12px; margin-top: auto;">
                            <a href="https://code-burry.vercel.app" target="_blank" rel="noopener noreferrer" class="card-link" style="margin: 0;">Live Demo ↗</a>
                            <a href="https://github.com/sidoxsinu/CodeBurry" target="_blank" rel="noopener noreferrer" class="card-link" style="margin: 0;">View Repository ↗</a>
                        </div>'''
content = content.replace('<a href="https://github.com/sidoxsinu/CodeBurry" target="_blank" rel="noopener noreferrer" class="card-link">View Project →</a>', replacement_cb)


# 4. UniversityHub, SilentGuard, AI Voice (only GitHub repo)
content = content.replace('<a href="https://github.com/sidoxsinu/universityhub" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Project →</a>', '<a href="https://github.com/sidoxsinu/universityhub" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Repository ↗</a>')
content = content.replace('<a href="https://github.com/sidoxsinu/SilentGuard" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Project →</a>', '<a href="https://github.com/sidoxsinu/SilentGuard" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Repository ↗</a>')
content = content.replace('<a href="https://github.com/sidoxsinu/AI-Voice-Assistant" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Project →</a>', '<a href="https://github.com/sidoxsinu/AI-Voice-Assistant" target="_blank" rel="noopener noreferrer" class="card-link" style="margin-top: 16px;">View Repository ↗</a>')

# Update the achievement Pylon link if needed? The user said "replace view project with live vercel link add additional view repostery with same style for project github repo". 
# The achievement Pylon link is `🔗 View Project`. I'll leave it as is, or change to `🔗 View Repository`? Actually, it's just `View Project`, I'll change it to `🔗 Live Demo` or `🔗 View Repository`. The prompt specifies "for project github repo". I'll leave the achievements alone since they aren't "View Project ->" card links.

with open('index.html', 'w') as f:
    f.write(content)

print("Project links updated.")
