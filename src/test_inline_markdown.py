import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links
)

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

        node = TextNode("This is text with **bolded words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bolded words", TextType.BOLD),
        ])

        node = TextNode("This is an _italic word_ test.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is an ", TextType.TEXT),
            TextNode("italic word", TextType.ITALIC),
            TextNode(" test.", TextType.TEXT),
        ])

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/test1.png) and another ![image](https://i.imgur.com/test2.png)"
        )
        self.assertListEqual([
            ("image", "https://i.imgur.com/test1.png"),
            ("image", "https://i.imgur.com/test2.png"),
        ], matches)

    def test_extract_markdown_images_no_images(self):
        matches = extract_markdown_images("This is text with no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_no_text(self):
        matches = extract_markdown_images("")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)
        
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com) and another [link](https://www.yahoo.com)"
        )
        self.assertListEqual([
            ("link", "https://www.google.com"),
            ("link", "https://www.yahoo.com"),
        ], matches)

    def test_extract_markdown_links_no_links(self):
        matches = extract_markdown_links("This is text with no links")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_no_text(self):
        matches = extract_markdown_links("")
        self.assertListEqual([], matches)
