import os
import re

os.makedirs('assets', exist_ok=True)

# 1. Generate SVG Banner
svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#833ab4;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#fd1d1d;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fcb045;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)"/>
  <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="40" font-weight="bold" fill="white" dominant-baseline="middle" text-anchor="middle">
    Awesome Embedding Models
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
  </text>
</svg>"""
with open('assets/banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Decorate with Emojis & Banner
readme_emojis = readme.replace('# Awesome-Embedding-Models', '# 🚀 Awesome-Embedding-Models\n\n<p align="center"><img src="assets/banner.svg" alt="Banner"></p>')
readme_emojis = readme_emojis.replace('## Embedding Models in AI', '## 🧠 Embedding Models in AI')
readme_emojis = readme_emojis.replace('## 1. The Macro Chronological Evolution', '## ⏳ 1. The Macro Chronological Evolution')
readme_emojis = readme_emojis.replace('## 2. Core Architectural & Model Variants', '## 🏗️ 2. Core Architectural & Model Variants')
readme_emojis = readme_emojis.replace('## 3. High-Capacity Dimension Scaling & MRL Losses', '## 📉 3. High-Capacity Dimension Scaling & MRL Losses')
readme_emojis = readme_emojis.replace('## 4. Production Engineering Challenges & Hardware Solutions', '## ⚙️ 4. Production Engineering Challenges & Hardware Solutions')
readme_emojis = readme_emojis.replace('## 5. Frontier Real-World AI Industrial Applications', '## 🌍 5. Frontier Real-World AI Industrial Applications')
readme_emojis = readme_emojis.replace('## References', '## 📚 References')
readme_emojis = readme_emojis.replace('## Follow-Up Options Matrix', '## 🔮 Follow-Up Options Matrix')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_emojis)

os.system('git add . && git commit --allow-empty -m "added emojis and banner" && git push')

# Decorate with badges and SEO to the left
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

readme = readme.replace('<p align="center"><img src="assets/banner.svg" alt="Banner"></p>', '<p align="center"><img src="assets/banner.svg" alt="Banner"></p>\n\n<p align="center">\n  ' + left_badges + '\n</p>')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

os.system('git add . && git commit --allow-empty -m "seo optimised and badges to left added" && git push')

# Add badges to right
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

readme = readme.replace(left_badges, left_badges + '\n  ' + right_badge)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

os.system('git add . && git commit --allow-empty -m "badges to right added" && git push')

# Star History
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Embedding-Models&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chartrepos=ishandutta2007/Awesome-Embedding-Models&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chartrepos=ishandutta2007/Awesome-Embedding-Models&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chartrepos=ishandutta2007/Awesome-Embedding-Models&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

readme += star_history

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

os.system('git add . && git commit --allow-empty -m "star history added" && git push')

# Replace chartrepos with chart?repos
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

readme = readme.replace('chartrepos', 'chart?repos')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

os.system('git add . && git commit --allow-empty -m "fixed star plot" && git push')

# Replace awesome link
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

readme = readme.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

os.system('git add . && git commit --allow-empty -m "invalid awesome link fixed" && git push')

print("All decoration and tracking commits completed.")
