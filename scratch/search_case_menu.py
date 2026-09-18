with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Cenário")
if idx != -1:
    print(content[idx-500:idx+1000])
else:
    print("Not found in Case-Rebalanceamento-Carteira.html")
