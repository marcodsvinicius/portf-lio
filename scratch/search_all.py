import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        if 'intro' in content.lower() or 'sessionStorage' in content or 'localStorage' in content:
            print(f"Found something in {file}")
            
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if 'intro' in line.lower() or 'sessionStorage' in line or 'localStorage' in line:
                    print(f"  Line {i+1}: {line.strip()[:100]}")
