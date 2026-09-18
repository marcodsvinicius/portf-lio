with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Show the back-to-top button HTML in full
idx = content.find('id="back-to-top"')
print("BACK-TO-TOP BUTTON:")
print(content[idx-10:idx+400])
print("\n---\n")

# Find lucide.createIcons calls
import re
for m in re.finditer(r'lucide\.createIcons', content):
    print("createIcons at:", m.start())
    print(content[m.start()-50:m.start()+200])
    print("---")
