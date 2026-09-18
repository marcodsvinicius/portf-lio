with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Count curly braces
open_braces = css.count("{")
close_braces = css.count("}")

print(f"style.css: {open_braces} open braces vs {close_braces} close braces.")
if open_braces != close_braces:
    print("[ERROR] Mismatched curly braces in style.css!")
else:
    print("[OK] Braces match perfectly.")
