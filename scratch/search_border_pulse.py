with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("border-pulse count:", content.count("border-pulse"))
