import glob
import re

for filename in glob.glob("Case-*.html"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # search for RODAPÉ or similar at the bottom of the case studies
    print(f"\n--- FOOTER REGION IN {filename} ---")
    lines = content.splitlines()
    # find lines containing DESIGN & CODE or MARCO VINICIUS or similar near the bottom
    for i, line in enumerate(lines, 1):
        if "DESIGN & CODE" in line or "DESIGN  &  CODE" in line:
            start = max(0, i - 5)
            end = min(len(lines), i + 10)
            print(f"Lines {start} to {end}:")
            for j in range(start, end):
                print(f"  {j+1:4d}: {lines[j]}")
            break
