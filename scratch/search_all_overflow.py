import glob
import re

for filename in glob.glob("*.html") + glob.glob("*.jhtml"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = re.findall(r'overflow[^;]*;?', content)
    if matches:
        print(f"\n--- OVERFLOWS IN {filename} ---")
        for m in set(matches):
            print(f"  {m}")
