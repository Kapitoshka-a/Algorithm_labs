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


def binary_tree_diameter(current_node):
    if current_node:
        return 1 + max(binary_tree_diameter(current_node.left), binary_tree_diameter(current_node.right))
    return 0


def max_binary_tree_diameter(root_node):
    if not root_node:
        return 0

    stack = [(root_node, 0)]
    max_diameter = 0

    while stack:
        current_node, current_diameter = stack.pop()

        left_root_tree_len = binary_tree_diameter(current_node.left)
        right_root_tree_len = binary_tree_diameter(current_node.right)

        max_diameter = max(max_diameter, 1 + left_root_tree_len + right_root_tree_len)

        if current_node.left:
            stack.append((current_node.left, current_diameter + 1))

        if current_node.right:
            stack.append((current_node.right, current_diameter + 1))

    return max_diameter
