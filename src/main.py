import os
import shutil
from textnode import TextNode, TextType

def main():
    # text_node = TextNode(
    #     "This is some anchor text",
    #     TextType.LINK,
    #     "https://www.boot.dev"
    # )

    # print(text_node)

    copy('./static', 'public')

def copy(source, destination):
    print(f"Copying source `{source}` to destination `{destination}`...")

    # check source path exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source path `{source}` does not exist")

    # Delete the contents of the destination
    if os.path.exists(destination):
        print(f"Deleting destination...")
        shutil.rmtree(destination)

    # Copy all files and subdirectories from the source to the destination
    if os.path.isfile(source):
        print("Copying source file to destination...")
        return shutil.copyfile(source, destination)

    # Make destination directory
    print("Creating destination directory...")
    os.mkdir(destination)

    for entry in os.listdir(source):
        print(f"Copying directory item...")
        copy(os.path.join(source, entry), os.path.join(destination, entry))

    print("Copy complete!")

main()
