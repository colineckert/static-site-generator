import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extracted_images = extract_markdown_images(old_node.text)

        if old_node.text_type != TextType.TEXT or len(extracted_images) % 2 != 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for image_alt, image_link in extracted_images:
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            remaining_text = sections[1]
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extracted_links = extract_markdown_links(old_node.text)

        if old_node.text_type != TextType.TEXT or len(extracted_links) % 2 != 0:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for link_text, link_url in extracted_links:
            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            remaining_text = sections[1]
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
