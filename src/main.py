from textnode import TextNode, TextType

def main():
    print("Hello, World!")
    textnode = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(textnode.__repr__())

main()
