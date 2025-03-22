import os
from block_markdown import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        content = f.read()
    print(f"Read content from {from_path}")

    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()

    with open(template_path, 'r') as f:
        template = f.read()
    print(f"Read template from {template_path}")

    title = extract_title(content)
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    print(f"Writing to {dest_path}")
    with open(dest_path, 'w') as f:
        f.write(full_html)
