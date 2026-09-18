import os

path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\extracted_individual_clean.txt"
if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if "===" in line:
                print(line.strip())
else:
    print("extracted_individual_clean.txt not found")
