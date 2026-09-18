import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\original_noloco_layout.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if "Noloco Academy - Concluído em" in line or "Meluca - Concluído em" in line:
                    out.write(f"Match found at line {idx}!\n")
                    pos = line.find("Noloco Academy - Concluído em")
                    if pos == -1:
                        pos = line.find("Meluca - Concluído em")
                    block = line[max(0, pos-1000):pos+3000].replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
                    out.write(block)
                    out.write("\n" + "="*100 + "\n")
        print("Done writing to", output_path)
    else:
        print("Transcript not found")
