with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('id="back-to-top"')
print(content[idx-400:idx+600])
