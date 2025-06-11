import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode('p', 'ahoj kokotko', {'class': 'picovina'})
        node2 = HTMLNode('p', 'ahoj kokotko', {'class': 'picovina'})
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node3 = HTMLNode('p', 'ahoj kokotko', {'class': 'picovina'})
        node4 = HTMLNode('p', 'ahoj picusko', {'class': 'picovina'})
        self.assertNotEqual(node3, node4)
    
    def test_not_text_type(self):
        node5 = HTMLNode('a', 'google', {'class': 'kokotinka', 'href': 'https://www.google.com'})
        node6 = HTMLNode('a', 'ahoj kokotko', {'class': 'kokotinka', 'href': 'https://www.bing.com'})
        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()