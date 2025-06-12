import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "Ahoj, svet!")
        self.assertEqual(node1, '<p>Ahoj, svet!</p>')
        

    def test_not_eq(self):
        node3 = LeafNode()
        node4 = LeafNode()
        self.assertNotEqual(node3, node4)

    def test_not_text_type(self):
        node5 = LeafNode()
        node6 = LeafNode()
        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()