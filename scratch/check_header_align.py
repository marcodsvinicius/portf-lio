with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Show the current header structure with the hamburger right side
idx = content.find("mobile-menu-btn")
print("HEADER HAMBURGER CONTEXT:")
print(content[idx-600:idx+300])
