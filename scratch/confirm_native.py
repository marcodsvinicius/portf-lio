with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('id="back-to-top"')
print("=== BUTTON ===")
print(content[idx-50:idx+500])

import re
match = re.search(r'// Botão Voltar ao Topo.*?</script>', content, re.DOTALL)
if match:
    print("\n=== SCRIPT ===")
    print(match.group())
