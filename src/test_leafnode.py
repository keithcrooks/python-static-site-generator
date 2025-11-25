import unittest

from leafnode import LeafNode

class TestLeadNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "There's no need to shout!")
        self.assertEqual(node.to_html(), "<b>There's no need to shout!</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev" target="_blank">Boot.dev</a>')

if __name__ == "__main__":
    unittest.main()
