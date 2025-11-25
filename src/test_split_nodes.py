import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()
