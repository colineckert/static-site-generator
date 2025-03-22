from copystatic import copy_static_files
from generate_page import generate_pages_recursive

def main():
    copy_static_files()
    generate_pages_recursive('content', 'template.html', 'public')


main()
