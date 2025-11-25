from textnode import TextNode, TextType

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
