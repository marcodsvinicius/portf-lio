with open("Case-Rebalanceamento-Carteira.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's find `<style>` and print the next 200 characters
idx = content.find("<style>")
if idx != -1:
    print("Found <style> in Case-Rebalanceamento-Carteira.html:")
    print(content[idx:idx+250])
else:
    print("<style> not found")
