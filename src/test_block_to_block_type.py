import unittest

from block_to_block_type import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph - albeit, very short!"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code(self):
        block = """```Python
def hello(name):
    if not name:
        name = "world"

    print(f"Hello, {name}!")
```"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote(self):
        block = """
> I have a dream that my four little children will one day live in a nation
> where they will not be judged by the color of their skin
> but by the content of their character.
"""

        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = """- Eggs
- Sausage
- Chips
- Beans
"""

    def test_ordered_list(self):
        block = """1. Eggs
2. Sausage
3. Chips
4. Beans
"""

        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_headings_1(self):
        block = "# Heading level 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_headings_2(self):
        block = "## Heading level 2"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_headings_3(self):
        block = "### Heading level 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_headings_4(self):
        block = "#### Heading level 4"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_headings_5(self):
        block = "##### Heading level 5"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_headings_6(self):
        block = "###### Heading level 6"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)


if __name__ == "__main__":
    unittest.main()
