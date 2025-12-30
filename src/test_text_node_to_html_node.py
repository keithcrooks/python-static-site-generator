import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "./image.png")
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is an image node")
        self.assertDictEqual(html_node.props, {"src": "./image.png", "alt": "This is an image node"})

if __name__ == "__main__":
    unittest.main()
