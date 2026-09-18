import glob

old_footer = """  <footer class="w-full border-t border-white/5 relative z-10 px-6 md:px-12">
    <div class="max-w-7xl mx-auto w-full">
      <div class="py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
        <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
      </div>
    </div>
  </footer>"""

new_footer = """  <footer class="w-full relative z-10 px-6 md:px-12">
    <div class="max-w-7xl mx-auto w-full border-t border-white/5">
      <div class="py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
        <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
      </div>
    </div>
  </footer>"""

files_to_update = glob.glob("Case-*.html") + ["index.html"]

for file in files_to_update:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {file} (index indent)")
    elif old_footer.replace("  <footer", "    <footer").replace("  </footer", "    </footer") in content:
        old_indent = old_footer.replace("  <", "    <")
        new_indent = new_footer.replace("  <", "    <")
        content = content.replace(old_indent, new_indent)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {file} (case indent)")
    else:
        print(f"Footer not found in {file}")
