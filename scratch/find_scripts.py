import re

with open('Case-Hub-de-Obras.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
scripts = re.findall(r'<script.*?>.*?</script>', content, re.DOTALL)
for i, script in enumerate(scripts):
    print(f"Script {i+1}:")
    print(script[:200] + ('...' if len(script) > 200 else ''))
    print("-" * 40)
