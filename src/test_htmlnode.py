import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props_and_children(self):
        node = LeafNode("button", "Click me", { "type": "button" })
        parent_node = ParentNode("div", [node], { "class": "container" })
        self.assertEqual(parent_node.to_html(), '<div class="container"><button type="button">Click me</button></div>')

    def test_to_html_without_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_tag(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
