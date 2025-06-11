from textnode import TextNode, TextType

def main():
    node = TextNode('Toto je nejaky text mojho nodu', TextType.LINK, 'https://www.boot.dev')
    print(node)

main()