import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\found_courses_output.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if "Cursos e Especializações" in line and "Noloco" in line:
                    out.write(f"Match found at line {idx}!\n")
                    start = line.find("Cursos e Especializações")
                    content = line[start:start+10000].replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
                    out.write(content)
                    out.write("\n" + "="*100 + "\n")
        print("Done writing to", output_path)
    else:
        print("Transcript not found")
