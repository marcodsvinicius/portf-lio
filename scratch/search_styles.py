with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = list(re.finditer(r'<style[^>]*>([\s\S]*?)</style>', content))
print(f"Found {len(matches)} style blocks:")
for i, m in enumerate(matches, 1):
    print(f"Block {i} (char {m.start()} to {m.end()}):\n{m.group(1).strip()[:400]}\n...")
