import os
from block_markdown import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    with open(from_path, 'r') as f:
        content = f.read()

    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()

    with open(template_path, 'r') as f:
        template = f.read()

    title = extract_title(content)
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file_name in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, file_name)
        if os.path.isfile(file_path):
            generate_page(file_path, template_path, os.path.join(dest_dir_path, file_name.replace('.md', '.html')))
        elif os.path.isdir(file_path):
            generate_pages_recursive(file_path, template_path, os.path.join(dest_dir_path, file_name))
