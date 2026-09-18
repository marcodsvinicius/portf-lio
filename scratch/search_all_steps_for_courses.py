import os
import json

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\full_course_occurrences.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if "IA Generativa para Profissionais Criativos" in line and "Liderança com Inovação" in line:
                    # Let's decode this line and see if there are any tool calls or content with the full list of courses
                    cleaned = line.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
                    # We can print the step_index and basic info
                    out.write(f"--- MATCH AT LINE {idx} ---\n")
                    # Let's search for '<div class="group">' and write around it
                    pos = cleaned.find("IA Generativa para Profissionais Criativos")
                    # Let's extract a very large block of text around it, say 15000 characters!
                    block = cleaned[max(0, pos-4000):pos+8000]
                    out.write(block)
                    out.write("\n" + "="*100 + "\n\n")
        print("Done writing occurrences to", output_path)
    else:
        print("Transcript not found")
