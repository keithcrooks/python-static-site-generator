import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(
            str(node),
            'HTMLNode(a, Boot.dev, [], href="https://www.boot.dev" target="_blank")'
        )

if __name__ == "__main__":
    unittest.main()
