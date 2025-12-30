import os
from generate_page import *

def generate_pages_recursive(
    dir_path_content: str,
    template_path: str,
    destination_dir_path: str
) -> None:
    print(f"Generating pages from {dir_path_content} to {destination_dir_path}...")

    if not os.path.exists(destination_dir_path):
        print("Destination directory does not exist. Creating...")
        os.makedirs(destination_dir_path)
        print("destination directory created!")
        
    for entry in os.listdir(dir_path_content):
        print(f"Current entry: {entry}")
        from_path = os.path.join(dir_path_content, entry)
        destination_path = os.path.join(destination_dir_path, entry)

        if os.path.isdir(from_path):
            print("Entry IS a dir...")
            generate_pages_recursive(from_path, template_path, destination_path)
            continue

        if not entry.endswith(".md"):
            print("Entry IS NOT a MarkDown file - skipping")
            continue

        print("Entry IS a MarkDown file...")
        generate_page(from_path, template_path, destination_path.replace(".md", ".html"))

    print("Complete!")
