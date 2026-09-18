import os
import re

dir_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio"
files = [f for f in os.listdir(dir_path) if f.endswith(".html") or f.endswith(".jhtml") or f.endswith(".js")]

for fname in files:
    fpath = os.path.join(dir_path, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"=== File: {fname} ===")
    # Find all hrefs/srcs or lines containing Case-, .html, marcodsvinicius
    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        if "marcodsvinicius" in line or "Case-" in line or "index.html" in line:
            print(f"{idx}: {line.strip()}")
