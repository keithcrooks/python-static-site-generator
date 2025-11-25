import re

def extract_markdown_images(text):
    return re.findall(r"!\[([\d\w\s]+)\]\(([\d\w:\/\.]+)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[([\d\w\s]+)\]\(([^\(\)]*)\)", text)
