with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Show the full BTT button and its script
idx = content.find('id="back-to-top"')
print("=== BTT BUTTON HTML ===")
print(content[idx-50:idx+350])

# Find the BTT script
import re
match = re.search(r'// Botão Voltar ao Topo.*?</script>', content, re.DOTALL)
if match:
    print("\n=== BTT SCRIPT ===")
    print(match.group())
else:
    print("\nBTT script not found by pattern")
    # Try to find SCROLL_THRESHOLD
    idx2 = content.find('SCROLL_THRESHOLD')
    if idx2 != -1:
        print(content[idx2-200:idx2+500])
    else:
        print("SCROLL_THRESHOLD also not found!")
