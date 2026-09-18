with open(r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\walkthrough.md", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
print(f"Total lines: {len(lines)}")
print("--- LAST 60 LINES ---")
for i in range(max(0, len(lines)-60), len(lines)):
    print(f"{i+1:4d}: {lines[i]}")
