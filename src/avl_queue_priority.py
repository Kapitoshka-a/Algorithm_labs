class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


class AVL_Priority_Queue:
    def __init__(self):
        self.root = None

    @staticmethod
    def height(node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def updated_height(self, node):
        return 1 + max(self.height(node.left), self.height(node.right))

    def rotate_left(self, node):
        right_node = node.right
        right_left_node = right_node.left

        right_node.left = node
        node.right = right_left_node

        node.height = self.updated_height(node)
        right_node.height = self.updated_height(right_node)

        return right_node

    def rotate_right(self, node):
        left_node = node.left
        left_right_node = left_node.right

        left_node.right = node
        node.left = left_right_node

        node.height = self.updated_height(node)
        left_node.height = self.updated_height(left_node)

        return left_node

    def balance(self, node):
        self.updated_height(node)
        balance = self.balance_factor(node)
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        elif balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        elif balance > 1 and self.balance_factor(node.left) < 0:
            node.right = self.rotate_left(node.left)
            return self.rotate_right(node.right)
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def _insert(self, root, value, priority):
        if not root:
            return Node(value, priority)

        if priority > root.priority:
            root.left = self._insert(root.left, value, priority)
        elif priority <= root.priority:
            root.right = self._insert(root.right, value, priority)

        # Update height and balance the node
        return self.balance(root)

    def insert(self, priority, value):
        self.root = self._insert(self.root, value, priority)

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.value)
            self.inorder(root.right, result)

    def display(self):
        result = []
        self.inorder(self.root, result)
        return result if self.root else None


