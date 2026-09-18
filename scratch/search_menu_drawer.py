with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = list(re.finditer(r'mobile-menu-drawer', content, re.IGNORECASE))
print(f"Found {len(matches)} mobile-menu-drawer matches:")
for m in matches:
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"Match at {m.start()}: {content[start:end].strip()}")
