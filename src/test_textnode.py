import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node3 = TextNode('This is a text node', TextType.BOLD_TEXT)
        node4 = TextNode('This another text node', TextType.BOLD_TEXT)
        self.assertNotEqual(node3, node4)
    
    def test_not_text_type(self):
        node5 = TextNode('This is a text node', TextType.BOLD_TEXT)
        node6 = TextNode('This is a text node', TextType.ITALIC_TEXT)
        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()
    