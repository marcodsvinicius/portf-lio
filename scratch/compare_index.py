with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("index.jhtml", "r", encoding="utf-8") as f:
    jhtml = f.read()

print("index.html length:", len(html))
print("index.jhtml length:", len(jhtml))

# Let's search for the OceanPact string in both
if "OceanPact | Stefanini" in html and "OceanPact | Stefanini" in jhtml:
    print("OceanPact | Stefanini exists in both files.")
else:
    print("Error: OceanPact | Stefanini is missing in one of them.")
