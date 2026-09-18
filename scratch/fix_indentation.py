import glob

two_space_footer = """  <footer class="w-full relative z-10 px-6 md:px-12">
    <div class="max-w-7xl mx-auto w-full border-t border-white/5">
      <div class="py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
        <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
      </div>
    </div>
  </footer>"""

four_space_footer = """    <footer class="w-full relative z-10 px-6 md:px-12">
      <div class="max-w-7xl mx-auto w-full border-t border-white/5">
        <div class="py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
          <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
        </div>
      </div>
    </footer>"""

files_to_update = glob.glob("Case-*.html")

for file in files_to_update:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if two_space_footer in content:
        content = content.replace(two_space_footer, four_space_footer)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed indentation in {file}")
    else:
        print(f"Two space footer not found in {file}")
