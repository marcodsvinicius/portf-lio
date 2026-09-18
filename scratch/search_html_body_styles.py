import glob
import re

for filename in glob.glob("*.html") + glob.glob("*.jhtml"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    style_blocks = re.findall(r'<style[^>]*>([\s\S]*?)</style>', content)
    for i, block in enumerate(style_blocks):
        # Let's extract specific rules like html {...} and body {...} or html,body {...}
        matches = re.finditer(r'(html|body|html\s*,\s*body)\s*\{([^}]*)\}', block, re.IGNORECASE)
        for m in matches:
            selector = m.group(1).strip()
            body = m.group(2).strip().replace("\n", " ")
            print(f"File {filename}: {selector} -> {body}")
