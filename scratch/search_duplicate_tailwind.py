with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# search for cdn.tailwindcss.com script tags
import re
matches = list(re.finditer(r'<script[^>]*src="https://cdn\.tailwindcss\.com"[^>]*>', content))
print(f"Found {len(matches)} matches:")
for m in matches:
    # get context around match
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"Match at {m.start()}:\n{content[start:end]}\n---")
