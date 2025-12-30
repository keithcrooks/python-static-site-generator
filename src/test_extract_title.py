import unittest

from extract_title import *

class TestExtractTitle(unittest.TestCase):
    def test_title_found(self):
        markdown = """# Hello, World!

This is a paragraph and should not be included in the return value.

## This is a H2 level heading. This should not be included in the result either!

"""
        title = extract_title(markdown)

        self.assertEqual(title, "Hello, World!")

    def test_title_not_found(self):
        markdown = """This is a paragraph and should not be included in the return value.

## This is a H2 level heading. This should not be included in the result either!

"""

        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()
