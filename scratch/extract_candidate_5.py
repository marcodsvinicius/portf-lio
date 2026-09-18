import os
import json

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\candidate_5_full_block.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if '"step_index":4065' in line or '"step_index": 4065' in line or 'Cypher Financial AI' in line:
                    # Let's clean the line
                    cleaned = line.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
                    # Look for the courses block in cleaned
                    courses_start = cleaned.find("Cursos e Especializações")
                    if courses_start != -1:
                        # Grab a large chunk
                        chunk = cleaned[courses_start:courses_start+25000]
                        out.write(f"Line {idx} matches!\n")
                        out.write(chunk)
                        out.write("\n" + "="*80 + "\n\n")
        print("Done writing candidate 5 matches to", output_path)
    else:
        print("Transcript not found")
