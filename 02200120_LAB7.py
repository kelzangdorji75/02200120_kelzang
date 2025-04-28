# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self, root_value=None):
        print("Created new Binary Tree")
        if root_value is None:
            self.root = None
            print("Root: None")
        else:
            self.root = Node(root_value)
            print(f"Root: {self.root.value}")

# Example usage
# Create an empty binary tree
tree = BinaryTree()
