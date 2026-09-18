import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the start of OceanPact/Stefanini and print up to 5000 characters after to see the rest of the list
match = re.search(r'OceanPact \| Stefanini', content)
if match:
    idx = match.start()
    start_pos = max(0, idx - 500)
    end_pos = min(len(content), idx + 8000)
    print(content[start_pos:end_pos])
else:
    print("OceanPact | Stefanini not found")
