import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "Ahoj, svet!")
        node2 = LeafNode("p", "Ahoj, svet!")
        self.assertEqual(node1, node2)
    
    def test_eq(self):
        node3 = LeafNode("div", "Ahoj, kokoti !!!")
        node4 = LeafNode("div", "Ahoj, kokoti !!!")
        self.assertEqual(node3, node4)
        
    def test_eq(self):
        node3 = LeafNode("a", "Klikni na mňa!", {'class': 'picovina', 'href': 'https://www.google.com'})
        node4 = LeafNode("a", "Klikni na mňa!", {'class': 'picovina', 'href': 'https://www.google.com'})
        self.assertEqual(node3, node4)
        
    def test_not_eq(self):
        node4 = LeafNode("a", "Klikni na mňa!", {'class': 'picovina', 'href': 'https://www.google.com'})
        node5 = LeafNode("a", "Klikni na mňa hned!", {'class': 'picovina', 'href': 'https://www.bing.com'})
        self.assertNotEqual(node4, node5)
    

if __name__ == "__main__":
    unittest.main()
        
