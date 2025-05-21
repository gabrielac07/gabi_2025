import os

md_dir = "navigation"
ipynb_dir = "_notebooks"  # Corrected folder name

md_links = []
ipynb_links = []

# Collect Markdown files
for filename in sorted(os.listdir(md_dir)):
    if filename.endswith(".md"):
        path = os.path.join(md_dir, filename)
        name = os.path.splitext(filename)[0].replace('_', ' ').title()
        md_links.append(f'<li><a href="{path}">{name}</a></li>')

# Collect Jupyter Notebook files
for filename in sorted(os.listdir(ipynb_dir)):
    if filename.endswith(".ipynb"):
        path = os.path.join(ipynb_dir, filename)
        name = os.path.splitext(filename)[0].replace('_', ' ').title()
        ipynb_links.append(f'<li><a href="{path}">{name}</a></li>')

# Output the HTML block
print("<!-- START AUTO-GENERATED LINKS -->")
print("<h2>Markdown Pages</h2>")
print("<ul>")
print("\n".join(md_links))
print("</ul>")
print("<h2>Jupyter Notebooks</h2>")
print("<ul>")
print("\n".join(ipynb_links))
print("</ul>")
print("<!-- END AUTO-GENERATED LINKS -->")
