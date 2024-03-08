import unittest
from servises.binary_tree_diameter import *


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_max_binary_tree_diameter(self):
        binary_tree = BinaryTree()
        binary_tree.insert(1)
        binary_tree.insert(3)
        binary_tree.insert(2)
        binary_tree.insert(7)
        binary_tree.insert(4)
        binary_tree.insert(8)
        binary_tree.insert(5)
        binary_tree.insert(9)
        binary_tree.insert(6)

        self.assertEqual(max_binary_tree_diameter(binary_tree.root), 6)


if __name__ == '__main__':
    unittest.main()
