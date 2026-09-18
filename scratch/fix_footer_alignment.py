import glob

# The proper nested structure guarantees that max-w-7xl takes 100% width
# and the inner flex container left-aligns correctly.
correct_footer = """  <!-- RODAPÉ FINAL -->
  <footer class="w-full border-t border-white/5 relative z-10 px-6 md:px-12">
    <div class="max-w-7xl mx-auto w-full">
      <div class="py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
        <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
      </div>
    </div>
  </footer>"""

files_to_update = glob.glob("Case-*.html") + ["index.html"]

for file in files_to_update:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We will search for the faulty footer block and replace it.
    # The faulty block looks like:
    faulty_block = """    <!-- RODAPÉ FINAL -->
    <footer class="w-full border-t border-white/5 relative z-10 px-6 md:px-12">
      <div class="max-w-7xl mx-auto py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
        <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
      </div>
    </footer>"""
    
    faulty_block_index = """  <!-- RODAPÉ FINAL -->
  <footer class="w-full border-t border-white/5 relative z-10 px-6 md:px-12">
    <div class="max-w-7xl mx-auto py-8 flex justify-start items-center text-sm text-gray-400 font-mono">
      <span>Design feito por Marco Vinicius e Código elaborado no Antigravity.</span>
    </div>
  </footer>"""

    if faulty_block in content:
        content = content.replace(faulty_block, correct_footer.replace("  <!--", "    <!--"))
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {file} (case indent)")
    elif faulty_block_index in content:
        content = content.replace(faulty_block_index, correct_footer)
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {file} (index indent)")
    else:
        print(f"Could not find faulty block in {file}")
