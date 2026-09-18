import os
import json

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\all_certificates_found.txt"

keywords = [
    ("Design System Specialist", "Design System Specialist"),
    ("Liderança com Inovação", "Liderança com Inovação"),
    ("Fundamentos de Agentes de IA", "Agentes de IA"),
    ("Inteligência Artificial Generativa", "Inteligência Artificial Generativa")
]

results = {}
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if "find_all_certificates.py" in line or "inspect_courses.py" in line:
                continue
            for name, kw in keywords:
                if kw in line:
                    if name not in results:
                        results[name] = []
                    pos = line.find(kw)
                    block = line[max(0, pos-1000):pos+1500].replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
                    results[name].append((idx, block))

with open(output_path, "w", encoding="utf-8") as out:
    for name, list_matches in results.items():
        out.write(f"=== Keyword: {name} (found {len(list_matches)} times) ===\n")
        if list_matches:
            chosen = None
            for idx, block in reversed(list_matches):
                if '<div class="group">' in block:
                    chosen = (idx, block)
                    break
            if chosen is None:
                chosen = list_matches[-1]
            idx, block = chosen
            out.write(f"Occurred at line {idx}:\n")
            div_idx = block.find('<div class="group">')
            if div_idx != -1:
                out.write(block[div_idx:div_idx+1200])
            else:
                out.write(block[:1200])
        out.write("\n" + "=" * 80 + "\n")
print("Done writing to", output_path)
