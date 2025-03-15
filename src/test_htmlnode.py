import unittest

from htmlnode import HTMLNode

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
