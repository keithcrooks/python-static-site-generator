from htmlnode import HTMLNode
from block_to_block_type import *
from leafnode import *
from markdown_to_blocks import *
from parentnode import *
from text_node_to_html_node import *
from text_to_textnodes import *

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        if not block.strip():
            continue

        children.append(block_to_html_node(block))

    return ParentNode("div", children)

def text_to_children(text: str) -> list[HTMLNode]:
    children = []

    for text_node in text_to_textnodes(text):
        children.append(text_node_to_html_node(text_node))

    return children

def block_to_html_node(block: str) -> HTMLNode:
    type = block_to_block_type(block)

    match type:
        case BlockType.CODE:
            tag = "pre"
            lines = block.splitlines()
            text = "\n".join(lines[1:-1]) + "\n"
            children = [LeafNode("code", text)]

        case BlockType.HEADING:
            level = 0

            for char in block:
                if char != "#":
                    break

                level += 1

            tag = f"h{level}"

            text = block[level:].strip()
            children = text_to_children(text)

        case BlockType.PARAGRAPH:
            tag = "p"
            text = block.replace("\n", " ")
            children = text_to_children(text)

        case BlockType.QUOTE:
            tag = "blockquote"
            text = block.replace("> ", "").replace(">\n", "\n")
            children = text_to_children(text)

        case BlockType.ORDERED_LIST:
            tag ="ol"
            
            children = []

            for item in block.splitlines():
                item = item.strip()
                if not item:
                    continue

                dot_index = item.find(".")
                item = item[dot_index+1:].strip()
                children.append(ParentNode("li", text_to_children(item)))

            # for item in block.split()

        case BlockType.UNORDERED_LIST:
            tag = "ul"
            
            children = []

            for item in block.splitlines():
                item = item.strip()
                if not item:
                    continue

                children.append(ParentNode("li", text_to_children(item[2:])))

    return ParentNode(tag, children)
