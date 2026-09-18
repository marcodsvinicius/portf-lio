with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("mobile-menu-drawer")
if idx != -1:
    # Let's search for matches in script tags
    import re
    matches = [m.start() for m in re.finditer(r'mobile-menu-drawer', content)]
    for m in matches:
        print(content[m-200:m+400])
        print("-" * 40)
else:
    print("mobile-menu-drawer not found in script tags")
