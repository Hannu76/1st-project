import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = r'<div class="card-back">\s*<img src="images/logo\.png"[^>]*>\s*<h3.*?</h3>\s*<p.*?</p>\s*</div>'
replacement = r'''<div class="card-back" style="padding: 0; background: transparent; border: none;">
                            <img src="images/logo_wall.jpg" alt="Sun Shine 3D Logo" style="width: 100%; height: 100%; object-fit: cover; border-radius: 15px; border: 1px solid rgba(212, 175, 55, 0.5);">
                        </div>'''

html = re.sub(target, replacement, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
