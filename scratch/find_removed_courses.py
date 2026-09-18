import json
import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")

if os.path.exists(transcript_path):
    print("Transcript found! Searching...")
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if "IA Generativa para Profissionais Criativos" in line or "Liderança com Inovação" in line:
                # Print a part of the line that might contain the HTML code
                idx = line.find("IA Generativa para Profissionais Criativos")
                print(line[max(0, idx-500):idx+1500])
                print("=" * 80)
else:
    print("Transcript not found at", transcript_path)
