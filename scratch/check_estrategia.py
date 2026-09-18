import os

log_dir = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs"
transcript_path = os.path.join(log_dir, "transcript.jsonl")

if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if "Vanguarda da IA" in line and "target" in line and "check_estrategia" not in line:
                pos = line.find("Vanguarda da IA")
                start = line.rfind("<div class=", 0, pos)
                if start == -1:
                    start = line.rfind("<div class=\\\"", 0, pos)
                if start != -1:
                    end = line.find("</div>", pos)
                    if end == -1:
                        end = line.find("<\\/div>", pos)
                    if end != -1:
                        block = line[start:end+10].replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/').replace('\\\\r', '\r')
                        print(f"Match at line {idx}:")
                        print(block)
                        print("="*80)
                        break
else:
    print("Transcript not found")
