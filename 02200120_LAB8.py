#TASK1
#PART1
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    # Utility method to get the height of a node
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    # Utility method to calculate balance factor
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    # Left-Right rotation
    def left_right_rotate(self, node):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    # Right-Left rotation
    def right_left_rotate(self, node):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    # Insert value into the AVL tree
    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            return root  # No duplicates allowed

        # Update the height of the current node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Check if the node became unbalanced
        balance = self.get_balance(root)

        # Left Heavy case
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right Heavy case
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right case
        if balance > 1 and value > root.left.value:
            return self.left_right_rotate(root)

        # Right-Left case
        if balance < -1 and value < root.right.value:
            return self.right_left_rotate(root)

        return root

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    # Delete value from the AVL tree
    def delete(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        # Update the height of the current node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Check if the node became unbalanced
        balance = self.get_balance(root)

        # Left Heavy case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right Heavy case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right case
        if balance > 1 and self.get_balance(root.left) < 0:
            return self.left_right_rotate(root)

        # Right-Left case
        if balance < -1 and self.get_balance(root.right) > 0:
            return self.right_left_rotate(root)

        return root

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    # Search for a value in the AVL tree
    def search(self, root, value):
        if root is None or root.value == value:
            return root

        if value < root.value:
            return self.search(root.left, value)

        return self.search(root.right, value)

    def search_value(self, value):
        return self.search(self.root, value)

    # Get the height of the tree
    def get_tree_height(self):
        return self.get_height(self.root)

    # Check if the tree is balanced
    def is_balanced(self):
        return self.get_balance(self.root) in [-1, 0, 1]

    # Get the node with the minimum value
    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Helper function to print the tree in level-order
    def print_tree(self):
        if not self.root:
            print("The tree is empty")
            return

        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(str(node.value))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(" ".join(level_nodes))

# Example Usage
avl_tree = AVLTree()
avl_tree.insert_value(10)
avl_tree.insert_value(20)
avl_tree.insert_value(30)
avl_tree.insert_value(25)
avl_tree.insert_value(5)

print("Tree after insertions:")
avl_tree.print_tree()  # Should print the tree structure

avl_tree.delete_value(20)
print("\nTree after deleting 20:")
avl_tree.print_tree()  # Should print the tree structure after deletion
