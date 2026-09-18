import os

# Target files
files_to_update = [
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\index.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\index.jhtml",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Design-System.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Hub-de-Obras.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Rebalanceamento-Carteira.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Tour-Guiado.html"
]

target_size = 76472

fouc_css = """<style>
    /* Previne o flash de conteúdo sem estilo (FOUC) no menu lateral */
    #mobile-menu-drawer:not(.opacity-100) {
      opacity: 0 !important;
      pointer-events: none !important;
      display: none !important;
    }"""

def update_file(file_path):
    print(f"\nProcessing {os.path.basename(file_path)}...")
    
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read().replace("\r\n", "\n")

    # Inject FOUC fix
    if "/* Previne o flash de conteúdo sem estilo (FOUC) no menu lateral */" in content:
        print("-> FOUC fix already present in this file.")
    else:
        if "<style>" in content:
            content = content.replace("<style>", fouc_css, 1)
            print("-> Injected FOUC CSS rule.")
        else:
            print("Error: <style> block not found!")
            return

    # Sizing compensation for index.html and index.jhtml
    if os.path.basename(file_path) in ["index.html", "index.jhtml"]:
        lines = content.split("\n")
        comp_line_idx = -1
        for i, line in enumerate(lines):
            if "/* Comp: " in line:
                comp_line_idx = i
                break
                
        if comp_line_idx != -1:
            comp_line = lines[comp_line_idx]
            start_idx = comp_line.find("/* Comp: ") + 9
            end_idx = comp_line.find(" */", start_idx)
            xs_str = comp_line[start_idx:end_idx]
            current_xs_len = len(xs_str)
            
            temp_content = "\n".join(lines)
            temp_bytes_len = len(temp_content.encode("utf-8"))
            
            diff = target_size - temp_bytes_len
            new_xs_len = current_xs_len + diff
            
            print(f"Current padding length: {current_xs_len}")
            print(f"File size before padding adjustment: {temp_bytes_len} bytes")
            print(f"Adjustment needed: {diff} bytes")
            print(f"New padding length: {new_xs_len}")
            
            if new_xs_len > 0:
                new_xs_str = "X" * new_xs_len
                lines[comp_line_idx] = comp_line[:start_idx] + new_xs_str + comp_line[end_idx:]
                
                final_content = "\n".join(lines)
                final_bytes_len = len(final_content.encode("utf-8"))
                
                if final_bytes_len == target_size:
                    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
                        f.write(final_content)
                    print(f"Successfully balanced and saved {os.path.basename(file_path)} to exactly {final_bytes_len} bytes!")
                else:
                    print(f"Error: final bytes check failed! Got {final_bytes_len} instead of {target_size}")
            else:
                print("Error: New padding length is negative!")
        else:
            print("Error: Compensation line not found!")
    else:
        # Non-constrained files simply get saved
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print(f"Successfully saved {os.path.basename(file_path)}!")

# Execute updates
for f in files_to_update:
    update_file(f)
