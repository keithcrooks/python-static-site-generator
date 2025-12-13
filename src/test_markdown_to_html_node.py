import unittest

from htmlnode import HTMLNode
from markdown_to_html_node import *

class TestMarkdownToHTMLNode(unittest.TestCase):
    # def test_return_type(self):
    #     node = markdown_to_html_node("")
    #     self.assertIsInstance(node, HTMLNode)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        md = """
This is my list of dead good stuff ordered by me favourite!

1. Food
2. Beer
3. Music

Do you like it?
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is my list of dead good stuff ordered by me favourite!</p><ol><li>Food</li><li>Beer</li><li>Music</li></ol><p>Do you like it?</p></div>",
        )

    def test_unordered_list(self):
        md = """
This is my list of dead good stuff!

- Food
- Beer
- Music

Do you like it?
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is my list of dead good stuff!</p><ul><li>Food</li><li>Beer</li><li>Music</li></ul><p>Do you like it?</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
