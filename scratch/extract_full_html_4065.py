import os
import json

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\html_4065.html"

if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if idx == 1548:
                # Load the JSON line
                data = json.loads(line)
                content = data.get("content", "")
                # Find index.html contents
                # The content starts with "Created At: ..." and has showing lines
                # Let's save the whole content to a file
                with open(output_path, "w", encoding="utf-8") as out:
                    out.write(content)
                print(f"Successfully wrote content from line {idx} to {output_path}")
                break
else:
    print("Transcript not found")
