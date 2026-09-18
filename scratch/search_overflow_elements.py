import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# find all HTML elements that have overflow-hidden or overflow-y-hidden or similar classes
matches = re.finditer(r'<[a-zA-Z0-9\-]+[^>]*class="[^"]*(overflow|h-screen|h-full|fixed)[^"]*"[^>]*>', content)
print("--- ELEMENTS WITH OVERFLOW/H-SCREEN/H-FULL/FIXED CLASSES ---")
for m in matches:
    print(f"Match: {m.group()[:150]}")
