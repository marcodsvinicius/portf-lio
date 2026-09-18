import os, re

files = [
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Design-System.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Hub-de-Obras.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Rebalanceamento-Carteira.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Tour-Guiado.html",
]

# ── NEW button: use inline style="opacity:0" instead of Tailwind opacity-0
# This way the button is hidden via native CSS — no Tailwind dependency ──
old_button = '''  <!-- Botão Flutuante Voltar ao Topo -->
  <button id="back-to-top" aria-label="Voltar ao topo" class="fixed bottom-6 right-6 md:right-12 z-50 w-12 h-12 flex items-center justify-center rounded-xl bg-black/60 backdrop-blur-xl border border-white/10 shadow-lg text-white hover:text-[#ccff00] hover:border-[#ccff00]/40 active:scale-95 transition-all duration-300 opacity-0 pointer-events-none [-webkit-tap-highlight-color:transparent] outline-none">
    <i data-lucide="arrow-up" class="w-6 h-6"></i>
  </button>'''

new_button = '''  <!-- Botão Flutuante Voltar ao Topo -->
  <button id="back-to-top" aria-label="Voltar ao topo" style="position:fixed;bottom:24px;right:24px;z-index:9999;width:48px;height:48px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:rgba(0,0,0,0.6);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(255,255,255,0.1);box-shadow:0 4px 20px rgba(0,0,0,0.4);color:white;cursor:pointer;opacity:0;transition:opacity 0.3s ease,transform 0.3s ease,border-color 0.3s ease,color 0.3s ease;pointer-events:none;outline:none;" onmouseenter="this.style.borderColor='rgba(204,255,0,0.4)';this.style.color='#ccff00'" onmouseleave="this.style.borderColor='rgba(255,255,255,0.1)';this.style.color='white'">
    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>
  </button>'''

# ── NEW script: pure JS, no Tailwind classes, no Lucide dependency ──
old_script_pattern = r'<script>\s*// Botão Voltar ao Topo.*?</script>'

new_script = '''  <script>
    // Botão Voltar ao Topo
    (function() {
      var btn = document.getElementById('back-to-top');
      if (!btn) return;
      var threshold = 300; // px from top — aparece cedo o suficiente

      function updateVisibility() {
        if (window.scrollY > threshold) {
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
          btn.style.transform = 'translateY(0)';
        } else {
          btn.style.opacity = '0';
          btn.style.pointerEvents = 'none';
          btn.style.transform = 'translateY(8px)';
        }
      }

      window.addEventListener('scroll', updateVisibility, { passive: true });
      updateVisibility(); // run on load

      btn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    })();
  </script>'''

for file_path in files:
    print(f"\nProcessing {os.path.basename(file_path)}...")
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read().replace("\r\n", "\n")

    # Replace button
    if old_button in content:
        content = content.replace(old_button, new_button)
        print("  -> Replaced button with native CSS version")
    else:
        print("  -> Old button pattern not matched — checking for inline style version")
        # Check if already updated
        if 'position:fixed;bottom:24px' in content:
            print("  -> Already updated")
        else:
            print("  -> WARNING: button not found!")

    # Replace script
    match = re.search(old_script_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_script + content[match.end():]
        print("  -> Replaced scroll script with pure JS version")
    else:
        print("  -> Script pattern not matched")

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  -> Saved")

print("\nDone!")
