import glob
import re

files_to_update = glob.glob("Case-*.html")

for file in files_to_update:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Target the link inside the mobile menu drawer
    old_target = """<a href="https://marcodsvinicius.com/" class="flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-white/60 hover:text-[#ccff00] hover:bg-white/5 border border-white/10 transition-all font-montserrat font-bold text-xs uppercase tracking-wider">
            <i data-lucide="arrow-left" class="w-4 h-4"></i>
            Voltar aos Projetos
          </a>"""
          
    new_target = """<a href="https://marcodsvinicius.com/" class="flex items-center justify-center gap-2 px-2 py-3 rounded-xl text-white/60 hover:text-[#ccff00] hover:bg-white/5 border border-white/10 transition-all font-montserrat font-bold text-[11px] uppercase tracking-wide whitespace-nowrap">
            <i data-lucide="arrow-left" class="w-4 h-4 shrink-0"></i>
            Voltar aos Projetos
          </a>"""

    if old_target in content:
        content = content.replace(old_target, new_target)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed menu button in {file}")
    else:
        # Try a regex in case whitespace is slightly different
        pattern = re.compile(r'<a href="https://marcodsvinicius\.com/" class="flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-white/60 hover:text-\[#ccff00\] hover:bg-white/5 border border-white/10 transition-all font-montserrat font-bold text-xs uppercase tracking-wider">\s*<i data-lucide="arrow-left" class="w-4 h-4"></i>\s*Voltar aos Projetos\s*</a>')
        if pattern.search(content):
            content = pattern.sub(new_target, content)
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed menu button in {file} via regex")
        else:
            print(f"Target button not found in {file}")
