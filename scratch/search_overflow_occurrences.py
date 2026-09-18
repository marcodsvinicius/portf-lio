with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = list(re.finditer(r'\.overflow|\.style\.overflow|overflow', content, re.IGNORECASE))
print(f"Found {len(matches)} overflow matches:")
for m in matches:
    start = max(0, m.start() - 60)
    end = min(len(content), m.end() + 60)
    print(f"Match at {m.start()}: {content[start:end].strip()}")
