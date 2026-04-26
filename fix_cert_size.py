import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('flex: 0 0 280px;', 'flex: 0 0 200px;')
content = content.replace('height: 210px;', 'height: 150px;')

with open('index.html', 'w') as f:
    f.write(content)

print("Certificate container sizes reduced!")
