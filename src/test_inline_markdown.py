import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
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
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_nodes_image_with_malformed_markdown(self):
        node = TextNode(
            "This text has malformed markdown ![missing-url]( and ![alt-without](https://example.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                # The entire input text should remain as a single TextNode
                # because no valid image markdown can be parsed from it
                TextNode(
                    "This text has malformed markdown ![missing-url]( and ![alt-without](https://example.com)",
                    TextType.TEXT
                )
            ],
            new_nodes,
        )

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )

    def test_split_nodes_link_with_malformed_markdown(self):
        node = TextNode(
            "This text has malformed markdown [missing-url]( and [alt-without](https://example.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                # The entire input text should remain as a single TextNode
                # because no valid image markdown can be parsed from it
                TextNode(
                    "This text has malformed markdown [missing-url]( and [alt-without](https://example.com)",
                    TextType.TEXT
                )
            ],
            new_nodes,
        )
