import os

# Target files
files_to_update = ["index.html", "index.jhtml"]

target_block_to_replace = """    </div>
  </div>
</div>

  <!-- Overlay de Fundo (Backdrop Blur) -->"""

replacement_block = """    </div>
  </div>
</div>
</div>

  <!-- Overlay de Fundo (Backdrop Blur) -->"""

duplicate_script_block = """  <!-- Dependências: Fontes, Tailwind CSS e Ícones -->
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Estilos Personalizados -->
  <style>
    .font-montserrat {
      font-family: 'Montserrat', sans-serif;
    }
    
    /* Animação suave para a borda da foto */
    @keyframes border-pulse {
      0%, 100% { border-color: rgba(183, 229, 0, 0.3); }
      50% { border-color: rgba(183, 229, 0, 0.8); }
    }
  </style>"""

for file_path in files_to_update:
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify if block exists
    if target_block_to_replace in content:
        print("-> Found target div closing block.")
        content = content.replace(target_block_to_replace, replacement_block, 1)
    else:
        print("-> WARNING: Target div closing block NOT found!")

    # Verify if duplicate script block exists
    if duplicate_script_block in content:
        print("-> Found duplicate script block.")
        content = content.replace(duplicate_script_block, "")
    else:
        print("-> WARNING: Duplicate script block NOT found!")

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Saved {file_path}")

print("Done! Running comparison...")
os.system("python compare.py")
