import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update img-card CSS
css_target = r"\s*\.img-card \{\s*background: rgba\(255, 255, 255, 0\.4\);[\s\S]*?transition: all 0\.4s ease;\n\s*\}"
css_replacement = r"""
        .img-card {
            text-align: left;
            perspective: 1500px;
            animation: float-3d 6s ease-in-out infinite;
            transition: transform 0.4s ease;
            cursor: pointer;
            border-radius: 15px;
        }
        .card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
        }
        .img-card.flipped .card-inner {
            transform: rotateY(180deg);
        }
        .card-front, .card-back {
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 15px;
            border: 1px solid rgba(212, 175, 55, 0.5);
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            overflow: hidden;
        }
        .card-front {
            position: relative;
        }
        .card-back {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            transform: rotateY(180deg);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.9);
            text-align: center;
            padding: 20px;
        }"""
html = re.sub(css_target, css_replacement, html, count=1)

# Modify img-card hover state to target card-front instead, or keep shadow on card-inner
hover_target = r"\.img-card:hover \{ \n\s*animation: none;\n\s*transform: translateY\(-15px\) scale\(1\.05\) rotateX\(0\) rotateY\(0\); \n\s*border-color: #ffd700;\n\s*box-shadow: 0 30px 60px rgba\(255, 215, 0, 0\.4\);\n\s*\}"
hover_replacement = r""".img-card:hover { 
            animation: none;
            transform: translateY(-15px) scale(1.05) rotateX(0) rotateY(0); 
        }
        .img-card:hover .card-front, .img-card:hover .card-back {
            border-color: #ffd700;
            box-shadow: 0 30px 60px rgba(255, 215, 0, 0.4);
        }"""
html = re.sub(hover_target, hover_replacement, html, count=1)


# 2. Reveal CSS
zoom_out_target = r"\.reveal-zoom-out \{ opacity: 0; transform: scale\(1\.15\); transition: all 1\.2s cubic-bezier\(0\.175, 0\.885, 0\.32, 1\.275\); \}"
zoom_out_replacement = r""".reveal-zoom-out { opacity: 0; transform: scale(1.15); transition: all 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .reveal-text { opacity: 0; transform: translateY(60px) skewY(6deg); transition: all 1s cubic-bezier(0.2, 0.8, 0.2, 1); }"""
html = re.sub(zoom_out_target, zoom_out_replacement, html, count=1)

active_target = r"\.reveal\.active, \.reveal-left\.active, \.reveal-right\.active, \.reveal-up\.active, \.reveal-pop\.active, \.reveal-zoom-out\.active \{ opacity: 1; transform: translate\(0\) scale\(1\); \}"
active_replacement = r""".reveal.active, .reveal-left.active, .reveal-right.active, .reveal-up.active, .reveal-pop.active, .reveal-zoom-out.active, .reveal-text.active { opacity: 1; transform: translate(0) scale(1) skewY(0); }"""
html = re.sub(active_target, active_replacement, html, count=1)

# JS Query
js_target = r"querySelectorAll\('\.reveal, \.reveal-left, \.reveal-right, \.reveal-up, \.reveal-pop, \.reveal-zoom-out'\);"
js_replacement = r"querySelectorAll('.reveal-text, .reveal-left, .reveal-right, .reveal-up, .reveal-pop, .reveal-zoom-out');"
html = re.sub(js_target, js_replacement, html, count=1)

# 3. Replace container reveal to fix child blocking
html = html.replace('class="container reveal"', 'class="container"')

# 4. Replace reveal-up with reveal-text
html = html.replace('class="section-title reveal-up"', 'class="section-title reveal-text"')
html = html.replace('class="subtitle reveal-up"', 'class="subtitle reveal-text"')

# 5. Fix HTML to wrap front/back
def wrap_card(m):
    inner = m.group(1).strip()
    return f'''
                <div class="img-card reveal-pop" onclick="this.classList.toggle('flipped')">
                    <div class="card-inner">
                        <div class="card-front">
                            {inner}
                        </div>
                        <div class="card-back">
                            <img src="images/logo.png" alt="Sun Shine Logo" style="width: 140px; height: auto; margin-bottom: 20px;">
                            <h3 style="color: var(--primary);">Sun Shine</h3>
                            <p style="color: var(--text-dark); margin-top: 10px;">Premium Dental Care</p>
                        </div>
                    </div>
                </div>'''

# Match each img-card. 
card_regex = re.compile(r'<div class="img-card reveal-pop">(.*?)</div>\s*(?=<!--|<div class="img-card|</div>)', re.DOTALL)
html = card_regex.sub(wrap_card, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Script execution completed.')
