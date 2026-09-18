with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# let's find the character index 26542 and get the line number and lines around it
lines = content.splitlines()
char_cnt = 0
for i, line in enumerate(lines, 1):
    char_cnt += len(line) + 1 # +1 for newline
    if char_cnt >= 26542:
        print(f"Around line {i}:")
        for j in range(max(0, i-10), min(len(lines), i+15)):
            print(f"{j+1:4d}: {lines[j]}")
        break
