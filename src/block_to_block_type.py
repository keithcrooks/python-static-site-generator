import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

HEADING_REGEX = re.compile(r"^#{1,6} [^\n]+$")

def block_to_block_type(block: str) -> BlockType:
    block = block.strip()

    if is_heading(block):
        return BlockType.HEADING

    if is_code(block):
        return BlockType.CODE

    if is_quote(block):
        return BlockType.QUOTE

    if is_ordered_list(block):
        return BlockType.ORDERED_LIST

    if is_unordered_list(block):
        return BlockType.UNORDERED_LIST

    return BlockType.PARAGRAPH

def is_code(block: str) -> bool:
    return block.startswith("```") and block.endswith("```")

def is_heading(block: str) -> bool:
    return bool(HEADING_REGEX.fullmatch(block))

def is_quote(block :str) -> bool:
    return all(line.startswith('>') for line in block.splitlines())

def is_ordered_list(block :str) -> bool:
    lines = block.splitlines()
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            return False

    return True

def is_unordered_list(block :str) -> bool:
    return all(line.startswith('- ') for line in block.splitlines())
