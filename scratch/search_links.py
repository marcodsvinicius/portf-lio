import os
import re

files_to_scan = [
    "index.html",
    "index.jhtml",
    "Case-Design-System.html",
    "Case-Hub-de-Obras.html",
    "Case-Rebalanceamento-Carteira.html",
    "Case-Tour-Guiado.html"
]

workspace_dir = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio"

for fname in files_to_scan:
    fpath = os.path.join(workspace_dir, fname)
    if not os.path.exists(fpath):
        print(f"File {fname} does not exist.")
        continue
    
    print(f"\n=== SCANNING {fname} ===")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        # Find any references to Case-*.html or index.html in href
        if "index.html" in line or "Case-" in line:
            print(f"Line {idx}: {line.strip()}")
