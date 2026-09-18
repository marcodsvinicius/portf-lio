with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("mobile-menu")
if idx != -1:
    print(content[idx-100:idx+600])
else:
    print("mobile-menu not found in index.html")
