with open("index.html", "rb") as f:
    content = f.read()

idx = content.find(b"Transformando a")
if idx != -1:
    print("Found in index.html:")
    print(content[idx-100:idx+200])
else:
    print("Not found in index.html")

with open("index.jhtml", "rb") as f:
    jcontent = f.read()

jidx = jcontent.find(b"Transformando a")
if jidx != -1:
    print("Found in index.jhtml:")
    print(jcontent[jidx-100:jidx+200])
else:
    print("Not found in index.jhtml")
