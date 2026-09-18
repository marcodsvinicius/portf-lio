import json
import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\extracted_courses.txt"

found_blocks = []
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if "IA Generativa para Profissionais Criativos" in line and "Liderança com Inovação" in line:
                idx = line.find("IA Generativa para Profissionais Criativos")
                block = line[max(0, idx-1000):idx+3000]
                found_blocks.append(block)

    with open(output_path, "w", encoding="utf-8") as out:
        for idx, block in enumerate(found_blocks):
            out.write(f"--- BLOCK {idx} ---\n")
            out.write(block)
            out.write("\n\n")
    print(f"Extracted {len(found_blocks)} blocks to scratch/extracted_courses.txt")
else:
    print("Transcript not found")
