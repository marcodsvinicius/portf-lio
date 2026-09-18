with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if '<!-- PROJETO' in line or '<a href="https://marcodsvinicius.com/' in line or 'Case-' in line:
            print(line.strip()[:150])
