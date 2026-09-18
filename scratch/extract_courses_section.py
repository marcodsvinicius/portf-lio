import re

with open(r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\html_4065.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\courses_extracted_4065.html"

# Let's clean the line prefix in lines (they have line number prefix "650: ...")
cleaned_lines = []
for line in lines:
    m = re.match(r'^\s*\d+:\s*(.*)', line)
    if m:
        cleaned_lines.append(m.group(1))
    else:
        cleaned_lines.append(line)

content = "\n".join(cleaned_lines)

# Now find Cursos e Especializações and extract the space-y-6 block
start_idx = content.find("Cursos e Especializações")
if start_idx != -1:
    div_start = content.find('<div class="space-y-6">', start_idx)
    if div_start != -1:
        # Let's find the closing div of this space-y-6 block.
        # Since each course card is a div.group, we want to find the final closing div.
        # We can extract a generous context and count divs.
        chunk = content[div_start:div_start+15000]
        # Let's find the closing tag for the space-y-6 div.
        # The structure is:
        # <div class="space-y-6">
        #    <div class="group">
        #       ...
        #    </div>
        #    ...
        # </div>
        # Let's write the cleaned lines or the chunk to the output
        with open(output_path, "w", encoding="utf-8") as out:
            out.write(chunk)
        print(f"Wrote extracted courses to {output_path}")
else:
    print("Could not find Cursos e Especializações in html_4065.html")
