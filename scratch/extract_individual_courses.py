import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\found_figma_output.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if "Figma Avançado" in line:
                    out.write(f"Match found at line {idx}!\n")
                    # Let's print out 2000 chars around it
                    pos = line.find("Figma Avançado")
                    block = line[max(0, pos-1000):pos+1500].replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
                    out.write(block)
                    out.write("\n" + "="*100 + "\n")
        print("Done writing to", output_path)
    else:
        print("Transcript not found")
