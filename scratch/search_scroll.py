import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()

print("--- OVERFLOW / SCROLL / HIDDEN / LOADER / PRELOADER OCCURRENCES ---")
for i, line in enumerate(lines, 1):
    # Match interesting terms
    if any(term in line.lower() for term in ["overflow", "scroll", "loader", "fouc", "preloader", "style.body", "document.body.style", "hidden"]):
        # But filter out extremely common stuff like just 'hidden' in tailwind class if too many, 
        # let's print them anyway with line numbers
        print(f"{i:4d}: {line.strip()[:120]}")
