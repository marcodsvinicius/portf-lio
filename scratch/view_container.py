with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Nelogica")
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("Nelogica not found")
