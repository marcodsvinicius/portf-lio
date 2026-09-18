with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find back-to-top or similar button
import re

# Find the "voltar" or "back" button near the header
matches = [(m.start(), m.group()) for m in re.finditer(r'(back-to-top|voltar-topo|arrow-up|Voltar ao topo|scroll-to-top)', content, re.IGNORECASE)]
for start, match in matches:
    print(f"Found: '{match}' at {start}")
    print(content[start-300:start+400])
    print("---")
