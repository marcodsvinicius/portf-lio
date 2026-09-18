with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Show logo area to confirm BTT is NOT there
idx = content.find("Logo MV.")
print("=== HEADER LOGO AREA ===")
print(content[idx:idx+500])

# Show floating button
idx2 = content.find('id="back-to-top"')
print("\n=== FLOATING BTT BUTTON ===")
print(content[idx2-80:idx2+350])
