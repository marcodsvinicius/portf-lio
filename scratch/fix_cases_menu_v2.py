import os
import re

case_files = [
    "Case-Design-System.html",
    "Case-Hub-de-Obras.html",
    "Case-Rebalanceamento-Carteira.html",
    "Case-Tour-Guiado.html"
]

# We will define a search pattern that matches the whole mobile-menu-drawer block,
# including the nav links, the original social media block, and the "Voltar aos Projetos" block.

drawer_pattern = re.compile(
    r'(<!-- Menu Lateral / Painel Compacto \(Dentro do Limiter para alinhamento no desktop\) -->\s*<div id="mobile-menu-drawer".*?<!-- Link para Voltar aos Projetos no rodapé da gaveta mobile -->\s*<div class="border-t border-white/10 pt-6">.*?Voltar aos Projetos.*?</a>\s*</div>\s*</div>)',
    re.DOTALL
)

new_drawer = """<!-- Menu Lateral / Painel Compacto (Dentro do Limiter para alinhamento no desktop) -->
      <div id="mobile-menu-drawer" class="pointer-events-auto absolute top-20 right-0 w-64 h-auto bg-[#050505]/95 backdrop-blur-2xl border border-white/10 rounded-2xl z-40 p-6 flex flex-col justify-between transform transition-all duration-300 ease-in-out opacity-0 pointer-events-none scale-95">
        <div class="flex flex-col gap-6">
          
          <!-- Links de Navegação -->
          <nav class="flex flex-col gap-3 pt-2">
            <a href="#cenario" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-gray-400 hover:text-[#ccff00] hover:bg-white/5 transition-all duration-300 font-montserrat font-bold text-xs uppercase tracking-wider" data-mobile-section="cenario">
              <i data-lucide="compass" class="w-4 h-4"></i>
              Cenário
            </a>
            <a href="#estrategia" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-gray-400 hover:text-[#ccff00] hover:bg-white/5 transition-all duration-300 font-montserrat font-bold text-xs uppercase tracking-wider" data-mobile-section="estrategia">
              <i data-lucide="target" class="w-4 h-4"></i>
              Estratégia
            </a>
            <a href="#solucao" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-gray-400 hover:text-[#ccff00] hover:bg-white/5 transition-all duration-300 font-montserrat font-bold text-xs uppercase tracking-wider" data-mobile-section="solucao">
              <i data-lucide="layers" class="w-4 h-4"></i>
              Solução
            </a>
            <a href="#valor-gerado" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-gray-400 hover:text-[#ccff00] hover:bg-white/5 transition-all duration-300 font-montserrat font-bold text-xs uppercase tracking-wider" data-mobile-section="valor-gerado">
              <i data-lucide="trending-up" class="w-4 h-4"></i>
              Impacto
            </a>
            <a href="#aprendizados" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-gray-400 hover:text-[#ccff00] hover:bg-white/5 transition-all duration-300 font-montserrat font-bold text-xs uppercase tracking-wider" data-mobile-section="aprendizados">
              <i data-lucide="award" class="w-4 h-4"></i>
              Aprendizados
            </a>
            <a href="https://marcodsvinicius.com/#contact" class="mobile-nav-link flex items-center gap-3 px-4 py-3 rounded-xl text-gray-400 hover:text-[#ccff00] hover:bg-white/5 transition-all duration-300 font-montserrat font-bold text-xs uppercase tracking-wider">
              <i data-lucide="mail" class="w-4 h-4"></i>
              Contato
            </a>
          </nav>
        </div>
        
        <!-- Rodapé do Menu (Redes Sociais e Botão Voltar) -->
        <div class="flex flex-col gap-6 mt-6 pt-6 border-t border-white/10">
          <!-- Redes Sociais com Espaçamento Premium e Separadores -->
          <div class="flex justify-center items-center gap-5">
            <a href="https://www.linkedin.com/in/marcodsvinicius/" target="_blank" class="text-gray-400 hover:text-[#CCFF00] hover:scale-110 active:scale-95 transition-all duration-300" aria-label="LinkedIn">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
              </svg>
            </a>
            <div class="w-px h-4 bg-white/10"></div>
            <a href="https://br.pinterest.com/marcodsvinicius/" target="_blank" class="text-gray-400 hover:text-[#CCFF00] hover:scale-110 active:scale-95 transition-all duration-300" aria-label="Pinterest">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 0C5.372 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.162 0 7.396 2.967 7.396 6.93 0 4.135-2.607 7.462-6.227 7.462-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.27 1.042-1.002 2.35-1.492 3.146 1.124.347 2.317.535 3.554.535 6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/>
              </svg>
            </a>
            <div class="w-px h-4 bg-white/10"></div>
            <a href="https://medium.com/@marcodsvinicius" target="_blank" class="text-gray-400 hover:text-[#CCFF00] hover:scale-110 active:scale-95 transition-all duration-300" aria-label="Medium">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.54 12a6.8 6.8 0 01-6.77 6.82A6.8 6.8 0 010 12a6.8 6.8 0 016.77-6.82A6.8 6.8 0 0113.54 12zM20.96 12a6.8 6.8 0 01-3.46 5.86 6.8 6.8 0 010-11.72A6.8 6.8 0 0120.96 12zM24 12a6.8 6.8 0 01-1.3 2.91 6.8 6.8 0 010-5.82A6.8 6.8 0 0124 12z"/>
              </svg>
            </a>
            <div class="w-px h-4 bg-white/10"></div>
            <a href="https://github.com/marcodsvinicius?tab=repositories" target="_blank" class="text-gray-400 hover:text-[#CCFF00] hover:scale-110 active:scale-95 transition-all duration-300" aria-label="GitHub">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
              </svg>
            </a>
          </div>
          
          <!-- Link para Voltar aos Projetos no rodapé da gaveta mobile -->
          <a href="https://marcodsvinicius.com/" class="flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-white/60 hover:text-[#ccff00] hover:bg-white/5 border border-white/10 transition-all font-montserrat font-bold text-xs uppercase tracking-wider">
            <i data-lucide="arrow-left" class="w-4 h-4"></i>
            Voltar aos Projetos
          </a>
        </div>
      </div>"""

for filename in case_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the drawer with the new premium design
        new_content, count = drawer_pattern.subn(new_drawer, content)
        if count > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated menu drawer in {filename}")
        else:
            print(f"Failed to find match in {filename}. Checking manual replace...")
            # Let's try simple replacement for the start div
            start_str = '<!-- Menu Lateral / Painel Compacto (Dentro do Limiter para alinhamento no desktop) -->'
            end_str = 'Voltar aos Projetos\n          </a>\n        </div>\n      </div>'
            if start_str in content:
                idx_start = content.index(start_str)
                idx_end = content.find('Voltar aos Projetos', idx_start)
                if idx_end != -1:
                    # find the next </div></div> closure
                    close_idx = content.find('</div>', idx_end) # closing a
                    close_idx = content.find('</div>', close_idx + 1) # closing button div
                    close_idx = content.find('</div>', close_idx + 1) # closing drawer div
                    
                    full_match = content[idx_start:close_idx + 6]
                    new_content = content.replace(full_match, new_drawer)
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Manually replaced menu drawer in {filename}")
                else:
                    print(f"Could not locate end in {filename}")
            else:
                print(f"Could not locate start in {filename}")
    else:
        print(f"File not found: {filename}")
