import os
import json

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")
output_path = r"c:\Users\mvsilva23\OneDrive - Stefanini\Documentos\Portfolio\scratch\full_writes.txt"

with open(output_path, "w", encoding="utf-8") as out:
    if os.path.exists(transcript_path):
        with open(transcript_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                # Search for write_to_file calls that write index.html
                if "write_to_file" in line and "index.html" in line:
                    # Let's see if this contains Noloco Certified Expert
                    if "Noloco Certified Expert" in line:
                        out.write(f"Line {idx} matches write_to_file containing Noloco!\n")
                        # Just dump the first 5000 chars to see what it is
                        out.write(line[:5000] + "...\n")
                elif "replace_file_content" in line and "index.html" in line:
                    if "Noloco Certified Expert" in line:
                        out.write(f"Line {idx} matches replace_file_content containing Noloco!\n")
                        out.write(line[:5000] + "...\n")
        print("Done scanning for full writes/replaces")
    else:
        print("Transcript not found")
