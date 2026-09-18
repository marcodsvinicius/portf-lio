import os

search_dir = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio"
files = ["index.html", "index.jhtml"]

for filename in files:
    filepath = os.path.join(search_dir, filename)
    with open(filepath, "rb") as f:
        content_bytes = f.read()

    original_size = len(content_bytes)
    print(f"Original size of {filename}: {original_size} bytes")

    # Find the target bytes: "Transformando a gestão de obras"
    # UTF-8 bytes for "Transformando a gestão de obras"
    target = "Transformando a gestão de obras".encode("utf-8")
    replacement = "Transformando a gestão de obras de navios".encode("utf-8")

    if target in content_bytes:
        print(f"  Target text found in {filename}")
        # Perform replacement
        content_bytes = content_bytes.replace(target, replacement, 1)
        
        # Now find the Comp block and remove 10 Xs
        # The comp block has multiple Xs inside /* Comp: XXXXX... */
        # We can find it using regex on the bytes
        import re
        comp_match = re.search(b'/\\* Comp: (X+)\\s*\\*/', content_bytes)
        if comp_match:
            old_comp = comp_match.group(0)
            xs = comp_match.group(1)
            # Remove 10 Xs
            new_xs = xs[:-10]
            new_comp = b"/* Comp: " + new_xs + b" */"
            
            content_bytes = content_bytes.replace(old_comp, new_comp, 1)
            print(f"  Comp padding adjusted in {filename} by removing 10 Xs")
        else:
            print(f"  [ERROR] Comp comment block not found in {filename}!")
    else:
        print(f"  [ERROR] Target text not found in {filename}!")

    # Write the modified bytes back
    with open(filepath, "wb") as f:
        f.write(content_bytes)

    # Re-read to confirm final size
    with open(filepath, "rb") as f:
        final_bytes = f.read()
    final_size = len(final_bytes)
    print(f"Final size of {filename}: {final_size} bytes")
    if final_size == 76472:
        print(f"  [SUCCESS] {filename} is exactly 76472 bytes!")
    else:
        print(f"  [FAILURE] {filename} is {final_size} bytes instead of 76472!")
