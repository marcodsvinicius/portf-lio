import glob
import re

files_to_update = ["Case-Design-System.html", "Case-Hub-de-Obras.html", "Case-Rebalanceamento-Carteira.html"]

new_section = """    <!-- 06. NEXT STEPS / FOOTER -->
    <footer class="py-24 px-6 md:px-12 border-t border-white/5 bg-gradient-to-t from-white/5 to-transparent text-center">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-3xl font-bold uppercase mb-6">Gostou deste projeto?</h2>
        <p class="text-gray-400 mb-8">
          Estou disponível para novos desafios e colaborações. Vamos construir experiências incríveis juntos.
        </p>
        <div class="flex flex-col sm:flex-row-reverse justify-center gap-4 w-full max-w-2xl mx-auto">
          <a href="mailto:contato@marcodsvinicius.com" class="w-full sm:w-auto px-8 py-4 sm:px-6 sm:py-3 sm:text-sm bg-[#ccff00] text-black font-bold uppercase tracking-widest hover:bg-white transition-colors rounded-sm text-center whitespace-nowrap flex items-center justify-center">
            Entrar em Contato
          </a>
          <a href="https://marcodsvinicius.com/" class="w-full sm:w-auto px-8 py-4 sm:px-6 sm:py-3 sm:text-sm border border-white/20 hover:border-[#ccff00] hover:text-[#ccff00] font-bold uppercase tracking-widest transition-colors rounded-sm text-center whitespace-nowrap flex items-center justify-center gap-2">
            <i data-lucide="arrow-left" class="w-4 h-4"></i>
            Voltar aos Projetos
          </a>
        </div>
      </div>
    </footer>"""

for file in files_to_update:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We use a regex to match the old block
    # It starts with "    <!-- 06. NEXT STEPS / FOOTER -->" and ends at the next "    </footer>"
    pattern = re.compile(r'    <!-- \d{2}\. NEXT STEPS / FOOTER -->\s*<footer class="py-24 px-6 md:px-12 border-t border-white/5 bg-gradient-to-t from-white/5 to-transparent text-center">.*?</footer>', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(new_section, content)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Replaced Next Steps section in {file}")
    else:
        # Fallback regex in case comment is slightly different
        pattern2 = re.compile(r'    <!-- .*?NEXT STEPS / FOOTER.*? -->\s*<footer.*?</footer>', re.DOTALL)
        if pattern2.search(content):
            content = pattern2.sub(new_section, content)
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Replaced Next Steps section in {file} (using fallback regex)")
        else:
            print(f"Could not find the section in {file}")
