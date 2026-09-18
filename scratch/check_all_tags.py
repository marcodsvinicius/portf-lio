import glob

for filename in glob.glob("*.html") + glob.glob("*.jhtml"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    div_open = content.count("<div")
    div_close = content.count("</div>")
    section_open = content.count("<section")
    section_close = content.count("</section")
    
    if div_open != div_close or section_open != section_close:
        print(f"File {filename} is unbalanced:")
        print(f"  div open: {div_open}, close: {div_close} (diff: {div_open - div_close})")
        print(f"  section open: {section_open}, close: {section_close} (diff: {section_open - section_close})")
    else:
        print(f"File {filename} is balanced.")
