import re

with open("index.html", "r", encoding="utf-8", newline="") as f:
    content = f.read().replace("\r\n", "\n")

# Test OceanPact indicator match
pact_indicator_old = 'absolute -left-[32px] md:-left-[57px] top-1.5 w-4 h-4 rounded-full bg-[#B7E500] border-4 border-[#050505] group-hover:scale-125 transition-all'
if pact_indicator_old in content:
    print("Found OceanPact indicator!")
else:
    print("WARNING: OceanPact indicator NOT found!")

# Test OceanPact bullet color
bullet_old = '<span class="text-[#B7E500] mx-1.5 md:mx-2 select-none">'
if bullet_old in content:
    print("Found OceanPact bullet!")
else:
    # Let's see what is there
    match = re.search(r'OceanPact \| Stefanini.*?(<span class=".*?".*?>.</span>)', content, re.DOTALL)
    if match:
        print("Alternative bullet match:", repr(match.group(1)))
    else:
        print("WARNING: OceanPact bullet NOT found!")

# Test OceanPact date span
date_old = '<span class="text-[#B7E500] font-bold text-[9px] md:text-xs uppercase tracking-wider">Dez. 2025 - até o momento</span>'
if date_old in content:
    print("Found OceanPact date!")
else:
    # Let's search with regex
    match = re.search(r'OceanPact \| Stefanini.*?<span class="text-\[#B7E500\] font-bold text-\[9px\] md:text-xs uppercase tracking-wider">(.*?)</span>', content, re.DOTALL)
    if match:
        print("Alternative date match:", repr(match.group(0)))
    else:
        print("WARNING: OceanPact date NOT found!")

# Test BB, GameOn, MAG, Cypher, Nelogica date spans
spans_to_test = [
    '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Nov. 2024 - Nov. 2025</span>',
    '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Jun 2024 - Atual</span>',
    '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Ago 2023 - Nov 2024</span>',
    '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Nov 2023 - Ago 2024</span>',
    '<span class="font-bold text-[9px] md:text-xs uppercase tracking-wider text-gray-500">Out 2021 - Abr 2023</span>'
]

for s in spans_to_test:
    if s in content:
        print(f"Found span: {s[:60]}...")
    else:
        print(f"WARNING: Span NOT found: {s[:60]}...")
        # Search with regex
        clean_s = re.sub(r'<span class=".*?">', '', s).replace('</span>', '')
        match = re.search(rf'<span class="[^"]*">{re.escape(clean_s)}</span>', content)
        if match:
            print("  But regex found:", repr(match.group(0)))
        else:
            print("  Regex also failed to find:", clean_s)
