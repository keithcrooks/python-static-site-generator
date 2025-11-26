def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")

    return [block.strip("\n") for block in blocks]
