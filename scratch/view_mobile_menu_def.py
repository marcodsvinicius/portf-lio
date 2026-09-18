with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find "mobile-menu" or class lists
idx = content.find("id=\"mobile-menu\"")
if idx != -1:
    print(content[idx-100:idx+500])
else:
    print("mobile-menu not found in Case-Rebalanceamento-Carteira.html")
