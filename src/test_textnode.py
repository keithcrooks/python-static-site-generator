import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a code text node", TextType.CODE)
        self.assertEqual(str(node), "TextNode(This is a code text node, code, None)")

    def test_link_defined(self):
        url = "https://www.boot.dev"
        node = TextNode("This is a link text node", TextType.LINK, url)
        self.assertEqual(str(node), "TextNode(This is a link text node, link, https://www.boot.dev)")

    def test_link_undefined(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()
