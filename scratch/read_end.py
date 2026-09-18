with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Show the last 3000 characters to see the exact order of button and script near </body>
print(content[-3000:])
