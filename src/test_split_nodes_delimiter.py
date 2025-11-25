import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_zero_delimiters(self):
        node = TextNode("Just plain text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(result, [node])

    def test_single_instance(self):
        node = TextNode("This is *bold* text", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(
            result,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ]
        )

    def test_double_instance(self):
        node = TextNode("This _one_ and _two_ things", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(
            result,
            [
                TextNode("This ", TextType.TEXT),
                TextNode("one", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.ITALIC),
                TextNode(" things", TextType.TEXT),
            ]
        )

    def test_match_at_start(self):
        node = TextNode("*start* and more", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(
            result,
            [
                TextNode("start", TextType.BOLD),
                TextNode(" and more", TextType.TEXT),
            ]
        )

    def test_match_at_end(self):
        node = TextNode("More and *end*", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.BOLD)

        self.assertEqual(
            result,
            [
                TextNode("More and ", TextType.TEXT),
                TextNode("end", TextType.BOLD),
            ]
        )

    def test_invalid_markdown(self):
        node = TextNode("This is `broken", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_text_type(self):
        node = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(result, [node])
