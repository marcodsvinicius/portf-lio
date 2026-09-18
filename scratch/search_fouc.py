with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
for i, line in enumerate(lines, 1):
    if "fouc" in line.lower() or "flash" in line.lower() or "prevent" in line.lower():
        print(f"{i:4d}: {line.strip()[:150]}")
