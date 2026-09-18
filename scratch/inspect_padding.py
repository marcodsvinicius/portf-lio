with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Search for the Comp comment
import re
match = re.search(r'/\* Comp: (X+)\s*\*/', content)
if match:
    x_string = match.group(1)
    print(f"Found Comp comment with {len(x_string)} Xs.")
    print(f"Total comment length: {len(match.group(0))}")
else:
    print("Comp comment not found!")

# Let's count bytes of the file
with open("index.html", "rb") as f:
    raw_bytes = f.read()
print(f"Current file size: {len(raw_bytes)} bytes")
