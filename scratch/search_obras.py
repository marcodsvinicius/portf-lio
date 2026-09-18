with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# Find occurrences of "obras" or "gestão" case-insensitively
matches = [m.start() for m in re.finditer(r'(obras|gestão|gestao|navios)', content, re.IGNORECASE)]
for m in matches[:10]:
    print(content[m-100:m+200])
    print("-" * 50)
