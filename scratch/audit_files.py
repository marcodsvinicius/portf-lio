import os

def check_html_well_formed(filepath):
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check 1: Nested <script> tags
        # Search for "<script" and check if another "<script" appears before "</script>"
        scripts = list(re.finditer(r'<script.*?>', content, re.IGNORECASE))
        end_scripts = list(re.finditer(r'</script>', content, re.IGNORECASE))
        
        # Simple stack-based check for nested tags
        tag_stack = []
        # Find all open/close tags for script
        tokens = []
        for s in scripts:
            tokens.append((s.start(), 'open', s.group()))
        for es in end_scripts:
            tokens.append((es.start(), 'close', es.group()))
        tokens.sort(key=lambda x: x[0])
        
        in_script = False
        for pos, t_type, raw in tokens:
            if t_type == 'open':
                if in_script:
                    errors.append(f"Nested <script> tag detected at position {pos}: {raw}")
                in_script = True
            else:
                if not in_script:
                    errors.append(f"Orphan </script> close tag detected at position {pos}")
                in_script = False

        # Check 2: Unclosed divs/sections - simple check
        open_divs = len(re.findall(r'<div\b', content, re.IGNORECASE))
        close_divs = len(re.findall(r'</div>', content, re.IGNORECASE))
        if open_divs != close_divs:
            errors.append(f"Div mismatch: {open_divs} opening divs vs {close_divs} closing divs")

        open_sections = len(re.findall(r'<section\b', content, re.IGNORECASE))
        close_sections = len(re.findall(r'</section>', content, re.IGNORECASE))
        if open_sections != close_sections:
            errors.append(f"Section mismatch: {open_sections} opening sections vs {close_sections} closing sections")

        # Check 3: Check Lucide icons initialization
        if 'lucide.createIcons()' not in content and 'lucide' in content:
            errors.append("Lucide JS included or used but lucide.createIcons() not found")

        # Check 4: Check if there's FOUC fix for mobile menu drawer in <style> block
        if '#mobile-menu-drawer:not(.opacity-100)' not in content:
            errors.append("FOUC CSS fix for #mobile-menu-drawer:not(.opacity-100) not found")

        # Check 5: Check back-to-top button
        if 'id="back-to-top"' in content:
            if 'style="position:fixed;bottom:24px;' not in content and 'position:fixed;' not in content:
                errors.append("back-to-top exists but does not use inline CSS style for position")
            if 'alignWithMenu' not in content:
                errors.append("back-to-top exists but does not have dynamic alignWithMenu JS function")

    except Exception as e:
        errors.append(f"Failed to parse file: {e}")
    return errors

import re
search_dir = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio"
html_files = [
    "index.html", "index.jhtml",
    "Case-Design-System.html", "Case-Hub-de-Obras.html",
    "Case-Rebalanceamento-Carteira.html", "Case-Tour-Guiado.html"
]

for filename in html_files:
    filepath = os.path.join(search_dir, filename)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        print(f"File: {filename} ({size} bytes)")
        errors = check_html_well_formed(filepath)
        if errors:
            for err in errors:
                print(f"  [ERROR] {err}")
        else:
            print("  [OK] No major structural issues/bugs found.")
    else:
        print(f"File: {filename} does not exist!")

# Also compare index.html and index.jhtml
html_path = os.path.join(search_dir, "index.html")
jhtml_path = os.path.join(search_dir, "index.jhtml")
if os.path.exists(html_path) and os.path.exists(jhtml_path):
    with open(html_path, "rb") as f:
        h_bytes = f.read()
    with open(jhtml_path, "rb") as f:
        j_bytes = f.read()
    if h_bytes == j_bytes:
        print("index.html and index.jhtml are identical (byte-for-byte).")
    else:
        print("index.html and index.jhtml differ!")
        # Print differences
        diff_indices = [i for i in range(min(len(h_bytes), len(j_bytes))) if h_bytes[i] != j_bytes[i]]
        print(f"  First mismatch at byte {diff_indices[0] if diff_indices else 'length mismatch'}")
