from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        
        split_text_list = node.text.split(delimiter)

        if len(split_text_list) % 2 == 0:
            raise ValueError(f"Error: Invalid MarkDown - missing closing delimiter '{delimiter}'")
        
        for i in range(len(split_text_list)):
            text = split_text_list[i]

            if not text:
                continue

            type = TextType.TEXT if i % 2 == 0 else text_type

            new_list.append(TextNode(text, type))

    return new_list

def split_nodes_image(old_nodes: list[TextNode]):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        matches = extract_markdown_images(node.text)

        if not matches:
            new_list.append(node)
            continue

        text = node.text
        for (alt_text, url) in matches:
            sections = text.split(f"![{alt_text}]({url})", 1)

            if sections[0]:
                new_list.append(TextNode(sections[0], TextType.TEXT))

            new_list.append(TextNode(alt_text, TextType.IMAGE, url))

            text = sections[1]

        if text:
            new_list.append(TextNode(text, TextType.TEXT))

    return new_list

def split_nodes_link(old_nodes):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        matches = extract_markdown_links(node.text)

        if not matches:
            new_list.append(node)
            continue

        text = node.text
        for (link_text, url) in matches:
            sections = text.split(f"[{link_text}]({url})", 1)

            if sections[0]:
                new_list.append(TextNode(sections[0], TextType.TEXT))

            new_list.append(TextNode(link_text, TextType.LINK, url))

            text = sections[1]

        if text:
            new_list.append(TextNode(text, TextType.TEXT))

    return new_list
