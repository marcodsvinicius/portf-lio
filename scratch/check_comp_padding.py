with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "Comp:"
idx = content.find("Comp:")
if idx != -1:
    print("Found Comp in index.html:")
    print(content[idx-100:idx+200])
else:
    print("Comp not found in index.html")

with open("index.jhtml", "r", encoding="utf-8") as f:
    jcontent = f.read()

jidx = jcontent.find("Comp:")
if jidx != -1:
    print("Found Comp in index.jhtml:")
    print(jcontent[jidx-100:jidx+200])
else:
    print("Comp not found in index.jhtml")
