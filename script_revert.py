import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update img-card CSS back to normal 3D float (without flip)
css_target = r"""\s*\.img-card \{\s*text-align: left;[\s\S]*?\.img-card:hover \.card-front, \.img-card:hover \.card-back \{\s*border-color: #ffd700;\s*box-shadow: 0 30px 60px rgba\(255, 215, 0, 0\.4\);\s*\}"""

css_replacement = r"""
        .img-card {
            background: rgba(255, 255, 255, 0.4);
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid rgba(212, 175, 55, 0.5); /* Gold border */
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            text-align: left;
            transform-style: preserve-3d;
            animation: float-3d 6s ease-in-out infinite;
            transition: all 0.4s ease;
        }
        .img-card:nth-child(even) { animation-delay: 2s; }
        .img-card:nth-child(3n) { animation-delay: 3.5s; }
        
        .img-card:hover { 
            animation: none;
            transform: translateY(-15px) scale(1.05) rotateX(0) rotateY(0); 
            border-color: #ffd700;
            box-shadow: 0 30px 60px rgba(255, 215, 0, 0.4);
        }"""
html = re.sub(css_target, css_replacement, html, count=1)

# 2. Extract contents back from card-front and delete card-back wrappers
card_regex = re.compile(
    r'<div class="img-card reveal-pop" onclick="this\.classList\.toggle\(\'flipped\'\)">\s*'
    r'<div class="card-inner">\s*'
    r'<div class="card-front">\s*'
    r'(.*?)\s*'
    r'</div>\s*'
    r'<div class="card-back"[\s\S]*?</div>\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)

html = card_regex.sub(r'<div class="img-card reveal-pop">\n                    \1\n                </div>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Revert completed.')
