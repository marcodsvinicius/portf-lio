import os, re

files = [
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Design-System.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Hub-de-Obras.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Rebalanceamento-Carteira.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Tour-Guiado.html",
]

old_btt_block_pattern = r'  <!-- Botão Flutuante Voltar ao Topo -->.*?</script>'

new_btt_block = '''  <!-- Botão Flutuante Voltar ao Topo -->
  <button id="back-to-top" aria-label="Voltar ao topo" style="position:fixed;bottom:24px;z-index:9999;width:48px;height:48px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:rgba(0,0,0,0.6);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(255,255,255,0.1);box-shadow:0 4px 20px rgba(0,0,0,0.4);color:white;cursor:pointer;opacity:0;transition:opacity 0.3s ease,transform 0.3s ease,border-color 0.3s ease,color 0.3s ease;pointer-events:none;outline:none;" onmouseenter="this.style.borderColor='rgba(204,255,0,0.4)';this.style.color='#ccff00'" onmouseleave="this.style.borderColor='rgba(255,255,255,0.1)';this.style.color='white'">
    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>
  </button>
  <script>
    (function() {
      var btn = document.getElementById('back-to-top');
      var menuBtn = document.getElementById('mobile-menu-btn');
      if (!btn) return;

      function alignWithMenu() {
        if (menuBtn) {
          var rect = menuBtn.getBoundingClientRect();
          btn.style.right = (window.innerWidth - rect.right) + 'px';
        } else {
          btn.style.right = '24px';
        }
      }

      function updateVisibility() {
        if (window.scrollY > 300) {
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
          btn.style.transform = 'translateY(0)';
        } else {
          btn.style.opacity = '0';
          btn.style.pointerEvents = 'none';
          btn.style.transform = 'translateY(8px)';
        }
      }

      alignWithMenu();
      window.addEventListener('scroll', updateVisibility, { passive: true });
      window.addEventListener('resize', alignWithMenu);
      btn.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    })();
  </script>'''

for file_path in files:
    print(f"\nProcessing {os.path.basename(file_path)}...")
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read().replace("\r\n", "\n")

    match = re.search(old_btt_block_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_btt_block + content[match.end():]
        print("  -> Replaced BTT block with aligned version")
    else:
        print("  -> BTT block pattern not found!")

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  -> Saved")

print("\nDone!")
