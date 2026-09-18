import json
import os
import re

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")

# We want to find any HTML blocks containing certifications
# Let's search the transcript for index.html content updates or views
found_htmls = []
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f):
            if "Cursos e Especializações" in line:
                # Find all occurrences of HTML-like blocks
                matches = re.findall(r'<div class=\\"space-y-6\\">.*?<\/div>', line)
                for m in matches:
                    decoded = m.replace('\\"', '"').replace('\\n', '\n').replace('\\r', '\r').replace('\\/', '/')
                    if "Noloco" in decoded or "Meluca" in decoded:
                        found_htmls.append((line_num, decoded))

print(f"Found {len(found_htmls)} HTML blocks")
for line_num, html in found_htmls[:5]:
    print(f"--- Block at line {line_num} ---")
    print(html[:1000])
    print("...")
    print(html[-500:])
    print("="*80)
