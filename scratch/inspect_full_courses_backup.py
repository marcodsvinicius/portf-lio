with open(r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\full_original_courses.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\noloco_found_context.txt"

with open(output_path, "w", encoding="utf-8") as out:
    idx = text.find("Noloco Certified Expert")
    while idx != -1:
        out.write(f"Match found at position {idx}!\n")
        context = text[max(0, idx-10000):idx+10000]
        out.write("--- CONTEXT ---\n")
        cleaned = context.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
        out.write(cleaned)
        out.write("\n" + "="*80 + "\n\n")
        idx = text.find("Noloco Certified Expert", idx+1)

print("Wrote matches to", output_path)
