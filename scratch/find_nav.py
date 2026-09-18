with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Cenário")
if idx != -1:
    print(content[idx-1200:idx])
else:
    print("Cenário not found")
