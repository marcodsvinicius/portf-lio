with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# search for <footer> tags or elements with id/class 'footer'
import re
matches = list(re.finditer(r'<footer|id="footer"|class="[^"]*footer', content, re.IGNORECASE))
print(f"Found {len(matches)} footer matches:")
for m in matches:
    start = max(0, m.start() - 200)
    end = min(len(content), m.end() + 600)
    print(f"Match at {m.start()}:\n{content[start:end]}\n---")
