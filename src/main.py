from copystatic import copy_static_files
from generate_page import generate_page

def main():
    copy_static_files()
    generate_page('content/index.md', 'template.html', 'public/index.html')


main()
