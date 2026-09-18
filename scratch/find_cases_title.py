import os

search_dir = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio"
search_term = "transformando a gestão de obras"

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith((".html", ".jhtml", ".js")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                if search_term in content:
                    print(f"Found in {path}")
                    # Find line number and context
                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        if search_term in line:
                            print(f"  Line {idx+1}: {line.strip()}")
            except Exception as e:
                pass
