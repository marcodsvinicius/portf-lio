import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\exact_step_1693.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                if idx == 1693:
                    out.write(line.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/'))
                    print("Wrote line 1693 to exact_step_1693.txt")
                    break
    else:
        print("Transcript not found")
