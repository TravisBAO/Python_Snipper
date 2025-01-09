from markdownify import markdownify
import os

files_dir = r'C:\Users\Travis Bao\Downloads\Nunit'
for filename in os.listdir(files_dir):
    f = os.path.join(files_dir, filename)
    file = open(f, "r", encoding='utf-8').read()
    html = markdownify(file, heading_style="ATX")

print(html)

