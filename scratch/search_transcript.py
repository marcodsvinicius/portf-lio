import json

log_path = r"C:\Users\mvsilva23\.gemini\antigravity\brain\bb31168c-07f7-4f3e-add8-cb9056432b34\.system_generated\logs\transcript.jsonl"

try:
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'intro-screen' in line or 'intro' in line.lower() or 'sessionStorage' in line:
                data = json.loads(line)
                if data['type'] == 'USER_INPUT' or data['type'] == 'PLANNER_RESPONSE':
                    content = data.get('content', '')
                    if 'intro' in content.lower() or 'sessionStorage' in content:
                        print(f"[{data['type']}] {content[:300]}...\n")
except Exception as e:
    print(f"Error reading transcript: {e}")
