with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the header with hamburger button and logo
idx = content.find("mobile-menu-btn")
if idx != -1:
    print(content[idx-800:idx+600])
