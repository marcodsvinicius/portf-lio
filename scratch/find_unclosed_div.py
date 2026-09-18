import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's tokenise the HTML into open tags, close tags, and comments
# We will focus on div tags.
tokens = re.split(r'(<!--.*?-->|<div[^>]*>|</div>)', content, flags=re.DOTALL)

stack = []
line_no = 1

for token in tokens:
    line_no += token.count("\n")
    if token.startswith("<!--"):
        continue
    elif token.startswith("<div"):
        # print(f"Open div at line {line_no}: {token[:60]}")
        stack.append((line_no, token))
    elif token == "</div>":
        if stack:
            stack.pop()
        else:
            print(f"Error: unmatched </div> at line {line_no}")

print("\n--- Remaining Unclosed Divs ---")
for idx, (l, t) in enumerate(stack):
    print(f"#{idx+1} Open div at line {l}: {t[:120]}")
