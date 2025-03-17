import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_eq(self):
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
