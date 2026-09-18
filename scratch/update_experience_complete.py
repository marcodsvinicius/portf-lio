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

    # 1. OceanPact: Remove highlight and set standard colors
    # Replace indicators
    old_pact_indicator = 'absolute -left-[32px] md:-left-[57px] top-1.5 w-4 h-4 rounded-full bg-[#B7E500] border-4 border-[#050505] group-hover:scale-125 transition-all'
    new_pact_indicator = 'absolute -left-[30px] md:-left-[55px] top-2 w-3 h-3 rounded-full bg-white/20 border-2 border-[#050505] group-hover:bg-[#B7E500] group-hover:scale-110 transition-all'
    
    if old_pact_indicator in content:
        content = content.replace(old_pact_indicator, new_pact_indicator)
        print("-> Updated OceanPact indicator")
    else:
        print("-> OceanPact indicator already updated or not found")
        
    # Replace bullet point and date classes for OceanPact
    old_bullet_pact = '<span class="text-[#B7E500] mx-1.5 md:mx-2 select-none">'
    new_bullet_pact = '<span class="text-gray-500 mx-1.5 md:mx-2 select-none">'
    if old_bullet_pact in content:
        content = content.replace(old_bullet_pact, new_bullet_pact)
        print("-> Updated OceanPact bullet point style")
        
    old_date_pact = '<span class="text-[#B7E500] font-bold text-[9px] md:text-xs uppercase tracking-wider">Dez. 2025 - até o momento</span>'
    new_date_pact = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Dez. 2025 - até o momento</span>'
    if old_date_pact in content:
        content = content.replace(old_date_pact, new_date_pact)
        print("-> Updated OceanPact date highlight style")

    # 2. Banco do Brasil: add "(1 ano e 1 mês)"
    old_bb = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Nov. 2024 - Nov. 2025</span>'
    new_bb = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Nov. 2024 - Nov. 2025 (1 ano e 1 mês)</span>'
    if old_bb in content:
        content = content.replace(old_bb, new_bb)
        print("-> Updated Banco do Brasil duration")
        
    # 3. GameOn: Jun 2024 - Mar de 2025 (10 meses)
    old_gameon = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Jun 2024 - Atual</span>'
    new_gameon = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Jun 2024 - Mar de 2025 (10 meses)</span>'
    if old_gameon in content:
        content = content.replace(old_gameon, new_gameon)
        print("-> Updated GameOn date and duration")

    # 4. Mag Seguros: Ago 2023 - Nov 2024 (4 meses)
    old_mag = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Ago 2023 - Nov 2024</span>'
    new_mag = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Ago 2023 - Nov 2024 (4 meses)</span>'
    if old_mag in content:
        content = content.replace(old_mag, new_mag)
        print("-> Updated Mag Seguros duration")

    # 5. Cypher Financial: Nov 2023 - Ago 2024 (10 meses)
    old_cypher = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Nov 2023 - Ago 2024</span>'
    new_cypher = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Nov 2023 - Ago 2024 (10 meses)</span>'
    if old_cypher in content:
        content = content.replace(old_cypher, new_cypher)
        print("-> Updated Cypher Financial duration")

    # 6. Nelogica: Out 2021 - Abr 2023 (1 ano e 7 meses)
    old_nelogica = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Out 2021 - Abr 2023</span>'
    new_nelogica = '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Out 2021 - Abr 2023 (1 ano e 7 meses)</span>'
    if old_nelogica in content:
        content = content.replace(old_nelogica, new_nelogica)
        print("-> Updated Nelogica duration")

    # 7. Append two new experiences at the end of Nelogica
    old_nelogica_end = """              <p class="text-gray-400 text-base leading-relaxed font-light">
                Planejamento estratégico de soluções para o mercado financeiro. Liderança da criação e governança do primeiro Design System do ecossistema de criptoativos da empresa, otimizando arquiteturas de informação complexas.
              </p>
            </div>"""

    new_nelogica_end = old_nelogica_end + """

            <!-- Experiência 7 -->
            <div class="relative group">
              <div class="absolute -left-[30px] md:-left-[55px] top-2 w-3 h-3 rounded-full bg-white/20 border-2 border-[#050505] group-hover:bg-[#B7E500] group-hover:scale-110 transition-all"></div>
              <h4 class="font-montserrat text-xl font-bold text-white mb-1">UI Designer e Desenvolvedor Front End</h4>
              <div class="text-[11px] md:text-sm text-gray-400 mb-4 font-medium whitespace-nowrap">
                <span class="text-white">Freelance</span>
                <span class="text-gray-500 mx-1.5 md:mx-2 select-none">•</span>
                <span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Fev 2020 - Jan 2022 (2 anos)</span>
              </div>
              <p class="text-gray-400 text-base leading-relaxed font-light">
                Atuação autônoma no desenvolvimento ponta a ponta de produtos digitais, unindo design e programação. Criação de interfaces modernas no Figma, Elementor, Photoshop e Illustrator, com implementação técnica em WordPress, HTML5, CSS3, JavaScript e jQuery. Uso estratégico de Hotjar e Google Analytics para análise de dados e otimização de conversões.
              </p>
            </div>

            <!-- Experiência 8 -->
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

    if old_nelogica_end in content:
        content = content.replace(old_nelogica_end, new_nelogica_end)
        print("-> Added Experience 7 (Freelance) and Experience 8 (LivreLab)")
    else:
        print("-> Nelogica end not found or already updated")

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
