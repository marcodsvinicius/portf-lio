import os

# Target files
files_to_update = [
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\index.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\index.jhtml"
]

target_size = 76472

def update_file(file_path):
    print(f"\nProcessing {os.path.basename(file_path)}...")
    
    # Read file with LF preservation
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read().replace("\r\n", "\n")

    # Define target string for Experience 8 (LivreLab)
    old_livrelab_block = """            <!-- Experiência 8 -->
            <div class="relative group">
              <div class="absolute -left-[30px] md:-left-[55px] top-2 w-3 h-3 rounded-full bg-white/20 border-2 border-[#050505] group-hover:bg-[#B7E500] group-hover:scale-110 transition-all"></div>
              <h4 class="font-montserrat text-xl font-bold text-white mb-1">Professor de Programação e Design</h4>
              <div class="text-[11px] md:text-sm text-gray-400 mb-4 font-medium whitespace-nowrap">
                <span class="text-white">LivreLab</span>
                <span class="text-gray-500 mx-1.5 md:mx-2 select-none">•</span>
                <span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Mar 2020 - Set 2021 (1 ano e 7 meses)</span>
              </div>
              <p class="text-gray-400 text-base leading-relaxed font-light">
                Ministrei aulas de design, game design e programação para crianças e adolescentes. Também colaborei diretamente com o CEO na análise e desenvolvimento de anúncios estratégicos, na criação de peças publicitárias para todas as redes sociais da escola e no desenvolvimento e manutenção técnica da plataforma online de ensino dos alunos.
              </p>
            </div>"""

    # New block with Experience 9 (DarwinX) appended
    new_livrelab_block = old_livrelab_block + """

            <!-- Experiência 9 -->
            <div class="relative group">
              <div class="absolute -left-[30px] md:-left-[55px] top-2 w-3 h-3 rounded-full bg-white/20 border-2 border-[#050505] group-hover:bg-[#B7E500] group-hover:scale-110 transition-all"></div>
              <h4 class="font-montserrat text-xl font-bold text-white mb-1">Desenvolvedor React</h4>
              <div class="text-[11px] md:text-sm text-gray-400 mb-4 font-medium whitespace-nowrap">
                <span class="text-white">DarwinX</span>
                <span class="text-gray-500 mx-1.5 md:mx-2 select-none">•</span>
                <span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Mar 2021 - Jul 2021 (5 meses)</span>
              </div>
              <p class="text-gray-400 text-base leading-relaxed font-light">
                Atuação no desenvolvimento e componentização de interfaces responsivas utilizando React. Foco na criação de elementos de UI reutilizáveis, consumo de APIs RESTful e colaboração próxima com a equipe de design para assegurar a fidelidade visual e a melhor experiência de uso no produto.
              </p>
            </div>"""

    if old_livrelab_block in content:
        content = content.replace(old_livrelab_block, new_livrelab_block)
        print("-> Added Experience 9 (DarwinX)")
    else:
        # Check if already added
        if "DarwinX" in content:
            print("-> Experience 9 (DarwinX) already added")
        else:
            print("Error: LivreLab experience block not found in content!")
            return

    # Split to apply compensation logic
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
        
        # Calculate current bytes len
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

# Execute for both files
for f in files_to_update:
    update_file(f)
