class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        if not self.root:
            self.root = Node(element)
        else:
            self._insert_recursively(self.root, element)

    def _insert_recursively(self, current_node, element):
        if element < current_node.element:
            if current_node.left is None:
                current_node.left = Node(element)
            else:
                self._insert_recursively(current_node.left, element)
        else:
            if current_node.right is None:
                current_node.right = Node(element)
            else:
                self._insert_recursively(current_node.right, element)


def max_binary_tree_diameter(root_node):
    max_diameter = 0

    def binary_tree_diameter(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_len = binary_tree_diameter(node.left)
        right_len = binary_tree_diameter(node.right)

        max_diameter = max(max_diameter, left_len + right_len)

        return 1 + max(left_len, right_len)

    binary_tree_diameter(root_node)
    return max_diameter
