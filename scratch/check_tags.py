with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# simple count of div and section open/close tags
div_open = content.count("<div")
div_close = content.count("</div>")
section_open = content.count("<section")
section_close = content.count("</section")
body_open = content.count("<body")
body_close = content.count("</body>")
html_open = content.count("<html")
html_close = content.count("</html>")

print(f"div open: {div_open}, close: {div_close}")
print(f"section open: {section_open}, close: {section_close}")
print(f"body open: {body_open}, close: {body_close}")
print(f"html open: {html_open}, close: {html_close}")
