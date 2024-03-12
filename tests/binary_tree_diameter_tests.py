import unittest
from src.binary_tree_diameter import *


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

        self.assertEqual(max_binary_tree_diameter(binary_tree.root), 5)

    def test_case_2(self):
        binary_tree = BinaryTree()
        binary_tree.insert(50)
        binary_tree.insert(31)
        binary_tree.insert(80)
        binary_tree.insert(28)
        binary_tree.insert(40)
        binary_tree.insert(20)
        binary_tree.insert(39)
        binary_tree.insert(42)
        binary_tree.insert(19)
        binary_tree.insert(25)
        binary_tree.insert(45)
        binary_tree.insert(48)

        self.assertEqual(max_binary_tree_diameter(binary_tree.root), 7)


if __name__ == '__main__':
    unittest.main()
