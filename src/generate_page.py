import os
from extract_title import *
from markdown_to_html_node import *

def generate_page(from_path: str, template_path: str, destination_path: str) -> None:
    print(f"Generating page from {from_path} to {destination_path} using {template_path}")

    markdown = get_file_contents(from_path)
    template = get_file_contents(template_path)

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template \
        .replace("{{ Title }}", title) \
        .replace("{{ Content }}", content)
    
    destination_dir = os.path.dirname(destination_path)

    if not os.path.isdir(destination_dir):
        os.mkdir(destination_dir)

    write_file_contents(destination_path, html)

def get_file_contents(path: str) -> str:
    with open(path, mode="r") as f:
        content = f.read()

    return content

def write_file_contents(path: str, contents) -> None:
    with open(path, mode="w") as f:
        f.write(contents)
