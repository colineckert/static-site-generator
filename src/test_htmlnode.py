import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('p', 'this is a paragraph').props_to_html()
        node2 = HTMLNode('p', 'this is a paragraph').props_to_html()
        self.assertEqual(node, node2)

        node = HTMLNode('div', None, [HTMLNode('div', 'test inner div')]).props_to_html()
        node2 = HTMLNode('div', None, [HTMLNode('div', 'test inner div')]).props_to_html()
        self.assertEqual(node, node2)

        node = HTMLNode('a', 'test link', None, { 'href': 'https://example.com' }).props_to_html()
        node2 = HTMLNode('a', 'test link', None, { 'href': 'https://example.com' }).props_to_html()
        self.assertEqual(node, node2)

        node = HTMLNode('img', None, None, { 'src': 'https://example.com/image.jpg' }).props_to_html()
        node2 = HTMLNode('img', None, None, { 'src': 'https://example.com/image.jpg' }).props_to_html()
        self.assertEqual(node, node2)

        node = HTMLNode('button', 'Click me', None, { 'type': 'button' }).props_to_html()
        node2 = HTMLNode('button', 'Click me', None, { 'type': 'button' }).props_to_html()
        self.assertEqual(node, node2)

        node = HTMLNode('button', 'Click me', None, { 'type': 'Submit' }).props_to_html()
        node2 = HTMLNode('button', 'Click me', None, { 'type': 'button' }).props_to_html()
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, div!")
        self.assertEqual(node.to_html(), "<div>Hello, div!</div>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, link!", { "href": "https://example.com" })
        self.assertEqual(node.to_html(), '<a href="https://example.com">Hello, link!</a>')
