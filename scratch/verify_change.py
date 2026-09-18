with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Transformando")
if idx != -1:
    print("Verification in index.html:")
    print(content[idx-50:idx+150])
else:
    print("Verification failed: not found")
