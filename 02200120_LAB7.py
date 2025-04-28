#TASK1: Implementthe Node and Binary Tree Class Structure
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

# Create an empty binary tree
tree = BinaryTree()

#TASK2:Implement Tree Information Methods
# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree class
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is None:
            self.root = None
        else:
            self.root = Node(root_value)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self):
        if self.root is None:
            return True
        queue = [self.root]
        end = False
        while queue:
            current = queue.pop(0)
            if current:
                if end:
                    return False
                queue.append(current.left)
                queue.append(current.right)
            else:
                end = True
        return True

# Example usage
bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

# Output required information
print("Tree Height:", bt.height(bt.root))
print("Total Nodes:", bt.size(bt.root))
print("Leaf Nodes Count:", bt.count_leaves(bt.root))
print("Is Full Binary Tree:", bt.is_full_binary_tree(bt.root))
print("Is Complete Binary Tree:", bt.is_complete_binary_tree())

