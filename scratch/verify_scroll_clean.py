import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's extract the main elements and check their parent context.
# We will trace the depth at major section declarations:
# - <section id="hero"
# - <section id="projects"
# - <section id="skills"
# - <section id="about"
# - <section id="contact"

tokens = re.split(r'(<div[^>]*>|</div>|<section[^>]*>|</section>)', content)
depth = 0
for t in tokens:
    if not t:
        continue
    if t.startswith("<div"):
        depth += 1
    elif t == "</div>":
        depth -= 1
    elif t.startswith("<section"):
        print(f"Section {t.strip()[:60]} is declared at nesting depth: {depth}")
    elif t == "</section>":
        pass
