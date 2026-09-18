import os, re

files = [
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Design-System.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Hub-de-Obras.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Rebalanceamento-Carteira.html",
    r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\Case-Tour-Guiado.html",
]

# ── 1. HEADER: revert back to original (remove back-to-top from header, restore simple logo wrapper) ──
old_logo_with_btt = '''      <!-- Botão Voltar ao Topo (header) + Logo MV. -->
      <div class="pointer-events-auto flex items-center gap-2">
        <a href="#" id="back-to-top" aria-label="Voltar ao topo" class="w-12 h-12 flex items-center justify-center rounded-xl bg-transparent border border-transparent shadow-none active:scale-95 transition-all duration-300 hover:border-[#ccff00]/40 text-white hover:text-[#ccff00] opacity-0 pointer-events-none [-webkit-tap-highlight-color:transparent] outline-none">
          <i data-lucide="arrow-up" class="w-6 h-6"></i>
        </a>
        <a id="logo-box" href="https://marcodsvinicius.com/" class="w-12 h-12 flex items-center justify-center rounded-xl bg-transparent border border-transparent shadow-none active:scale-95 transition-all duration-300 hover:border-[#ccff00]/40 font-montserrat font-black text-lg tracking-tighter text-[#B7E500] hover:text-[#CCFF00]" aria-label="Página Inicial">
          MV.
        </a>
      </div>'''

restored_logo = '''      <!-- Logo MV. -->
      <div class="pointer-events-auto">
        <a id="logo-box" href="https://marcodsvinicius.com/" class="w-12 h-12 flex items-center justify-center rounded-xl bg-transparent border border-transparent shadow-none active:scale-95 transition-all duration-300 hover:border-[#ccff00]/40 font-montserrat font-black text-lg tracking-tighter text-[#B7E500] hover:text-[#CCFF00]" aria-label="Página Inicial">
          MV.
        </a>
      </div>'''

# ── 2. FLOATING BUTTON: fixed bottom-right, aligned with hamburger column ──
# right-6 md:right-12 mirrors the px-6 md:px-12 padding of the header container
new_floating_btt = '''  <!-- Botão Flutuante Voltar ao Topo -->
  <button id="back-to-top" aria-label="Voltar ao topo" class="fixed bottom-6 right-6 md:right-12 z-50 w-12 h-12 flex items-center justify-center rounded-xl bg-black/60 backdrop-blur-xl border border-white/10 shadow-lg text-white hover:text-[#ccff00] hover:border-[#ccff00]/40 active:scale-95 transition-all duration-300 opacity-0 pointer-events-none [-webkit-tap-highlight-color:transparent] outline-none">
    <i data-lucide="arrow-up" class="w-6 h-6"></i>
  </button>'''

# ── 3. NEW SCROLL SCRIPT ──
new_btt_script = '''  <script>
    // Botão Voltar ao Topo
    document.addEventListener('DOMContentLoaded', () => {
      const bttBtn = document.getElementById('back-to-top');
      if (!bttBtn) return;

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

      bttBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    });
  </script>'''

# Pattern to find where to insert the floating button — just before </body>
insert_before = '</body>'

# Old script pattern to replace
old_script_pattern = r'<script>\s*// Botão Voltar ao Topo.*?</script>'

for file_path in files:
    print(f"\nProcessing {os.path.basename(file_path)}...")
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        content = f.read().replace("\r\n", "\n")

    # Step 1: Restore original logo wrapper (remove BTT from header)
    if old_logo_with_btt in content:
        content = content.replace(old_logo_with_btt, restored_logo)
        print("  -> Restored original logo wrapper (removed BTT from header)")
    else:
        print("  -> Logo already restored or pattern not matched")

    # Step 2: Remove any leftover old floating button (from before our last change)
    old_floating_patterns = [
        '  <!-- Botão Flutuante Voltar ao Topo -->\n  <a href="#" id="back-to-top"',
        '  <!-- Botão Flutuante Voltar ao Topo -->\n  <button id="back-to-top"',
    ]
    for pat in old_floating_patterns:
        if pat in content:
            # Find and remove the whole block up to </a> or </button>
            idx = content.find(pat)
            end_a = content.find('</a>', idx)
            end_btn = content.find('</button>', idx)
            # pick whichever closes first
            candidates = [x for x in [end_a, end_btn] if x != -1]
            if candidates:
                end_idx = min(candidates) + max(len('</a>'), len('</button>'))
                # strip surrounding blank lines
                block = content[idx:end_idx]
                content = content.replace(block, '', 1)
                print("  -> Removed old floating button block")
            break

    # Step 3: Insert new floating button before </body>
    if 'id="back-to-top"' not in content:
        content = content.replace(insert_before, new_floating_btt + '\n\n' + insert_before)
        print("  -> Inserted new fixed floating back-to-top button")
    else:
        print("  -> back-to-top already present in file (check manually)")

    # Step 4: Replace or insert the scroll script
    match = re.search(old_script_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_btt_script + content[match.end():]
        print("  -> Replaced back-to-top scroll script")
    elif 'SCROLL_THRESHOLD' not in content:
        # Insert the script before </body>
        content = content.replace(insert_before, new_btt_script + '\n\n' + insert_before)
        print("  -> Inserted new back-to-top scroll script")
    else:
        print("  -> Scroll script already up to date")

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  -> Saved {os.path.basename(file_path)}")

print("\nAll done!")
