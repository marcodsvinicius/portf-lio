import os, re

files = [
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Design-System.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Hub-de-Obras.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Rebalanceamento-Carteira.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Tour-Guiado.html",
]

# 1. Remove the old floating back-to-top button block
old_btt_block = '''  <!-- Botão Flutuante Voltar ao Topo -->
  <a href="#" id="back-to-top" class="fixed bottom-6 right-6 z-50 flex items-center justify-center w-12 h-12 bg-[#050505] text-white border border-white/10 rounded-full shadow-[0_4px_20px_rgba(0,0,0,0.5)] opacity-0 pointer-events-none transition-all duration-300 transform translate-y-4 hover:border-[#ccff00] hover:text-[#ccff00] backdrop-blur-xl hover:-translate-y-1">
    <i data-lucide="arrow-up" class="w-5 h-5"></i>
  </a>'''

# 2. New inline back-to-top button in header, left of logo — same style as hamburger
# Inject it inside the existing logo div wrapper, before the logo <a>
old_logo_wrapper = '''      <!-- Logo MV. -->
      <div class="pointer-events-auto">
        <a id="logo-box" href="https://marcodsvinicius.com/" class="w-12 h-12 flex items-center justify-center rounded-xl bg-transparent border border-transparent shadow-none active:scale-95 transition-all duration-300 hover:border-[#ccff00]/40 font-montserrat font-black text-lg tracking-tighter text-[#B7E500] hover:text-[#CCFF00]" aria-label="Página Inicial">
          MV.
        </a>
      </div>'''

new_logo_wrapper = '''      <!-- Botão Voltar ao Topo (header) + Logo MV. -->
      <div class="pointer-events-auto flex items-center gap-2">
        <a href="#" id="back-to-top" aria-label="Voltar ao topo" class="w-12 h-12 flex items-center justify-center rounded-xl bg-transparent border border-transparent shadow-none active:scale-95 transition-all duration-300 hover:border-[#ccff00]/40 text-white hover:text-[#ccff00] opacity-0 pointer-events-none [-webkit-tap-highlight-color:transparent] outline-none">
          <i data-lucide="arrow-up" class="w-6 h-6"></i>
        </a>
        <a id="logo-box" href="https://marcodsvinicius.com/" class="w-12 h-12 flex items-center justify-center rounded-xl bg-transparent border border-transparent shadow-none active:scale-95 transition-all duration-300 hover:border-[#ccff00]/40 font-montserrat font-black text-lg tracking-tighter text-[#B7E500] hover:text-[#CCFF00]" aria-label="Página Inicial">
          MV.
        </a>
      </div>'''

# 3. Replace the scroll JS to show/hide the NEW header button (not the old floating one)
# Old scroll listener for back-to-top
old_btt_script_pattern = r"document\.addEventListener\('DOMContentLoaded', \(\) => \{[\s\S]*?const bttBtn = document\.getElementById\('back-to-top'\);[\s\S]*?\}\);\s*</script>"

new_btt_script = """<script>
    // Botão Voltar ao Topo — aparece após rolar além do hero
    document.addEventListener('DOMContentLoaded', () => {
      const bttBtn = document.getElementById('back-to-top');
      if (!bttBtn) return;

      // Inicializa ícone assim que a página carrega
      lucide.createIcons();

      const SCROLL_THRESHOLD = window.innerHeight * 0.8;

      window.addEventListener('scroll', () => {
        if (window.scrollY > SCROLL_THRESHOLD) {
          bttBtn.classList.remove('opacity-0', 'pointer-events-none');
          bttBtn.classList.add('opacity-100', 'pointer-events-auto');
        } else {
          bttBtn.classList.add('opacity-0', 'pointer-events-none');
          bttBtn.classList.remove('opacity-100', 'pointer-events-auto');
        }
      });

      bttBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    });
  </script>"""

for file_path in files:
    print(f"\nProcessing {os.path.basename(file_path)}...")
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read().replace("\r\n", "\n")

    # Step 1: Remove old floating button
    if old_btt_block in content:
        content = content.replace(old_btt_block, "")
        print("  -> Removed old floating back-to-top button")
    else:
        print("  -> Old floating button not found (may already be updated)")

    # Step 2: Insert new button in header alongside logo
    if old_logo_wrapper in content:
        content = content.replace(old_logo_wrapper, new_logo_wrapper)
        print("  -> Inserted new header back-to-top button")
    elif "back-to-top" in content and "flex items-center gap-2" in content:
        print("  -> Header button already inserted")
    else:
        print("  -> WARNING: logo wrapper not found!")

    # Step 3: Replace old scroll script
    match = re.search(old_btt_script_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_btt_script + content[match.end():]
        print("  -> Replaced back-to-top scroll script")
    else:
        # Check if already replaced
        if "SCROLL_THRESHOLD" in content:
            print("  -> Script already updated")
        else:
            print("  -> WARNING: old BTT script pattern not found!")

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  -> Saved {os.path.basename(file_path)}")

print("\nAll done!")
