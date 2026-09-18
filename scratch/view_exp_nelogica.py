with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for '<span class="text-white">Nelogica</span>'
idx = content.find('<span class="text-white">Nelogica</span>')
if idx != -1:
    print(content[idx:idx+1500])
else:
    print("Nelogica experience block not found")
