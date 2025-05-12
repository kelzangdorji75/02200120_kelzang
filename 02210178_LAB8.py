class Node:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(value=None, color='black')
        self.root = self.NIL

    def insert(self, value):
        new_node = Node(value, left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if not parent:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_left(k.parent.parent)
        self.root.color = 'black'

    def search(self, value):
        def _search(node):
            if node == self.NIL or value == node.value:
                return node
            if value < node.value:
                return _search(node.left)
            return _search(node.right)

        result = _search(self.root)
        return result != self.NIL

    def get_black_height(self):
        def _black_height(node):
            if node == self.NIL:
                return 1
            left_black_height = _black_height(node.left)
            if node.color == 'black':
                return left_black_height + 1
            return left_black_height

        return _black_height(self.root)

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, value):
        z = self.root
        while z != self.NIL:
            if z.value == value:
                break
            elif value < z.value:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            return  # Value not found

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    s = x.parent.left
                if s.right.color == 'black' and s.left.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.rotate_left(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'


# Example Usage
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
print("Search 20:", rb_tree.search(20))  # True
print("Black Height:", rb_tree.get_black_height())
rb_tree.delete(20)
print("Search 20 after delete:", rb_tree.search(20))  # False
print("Black Height after delete:", rb_tree.get_black_height())

##tree
class Node:
    def __init__(self, value, color='red', left=None, right=None, parent=None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return f"{self.value}({self.color[0]})"  # Shows value and first letter of color


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(value=None, color='black')
        self.root = self.NIL

    def print_tree(self):
        if self.root == self.NIL:
            print("Empty Tree")
            return
        self._print_tree(self.root, "", True)

    def _print_tree(self, node, indent, last):
        """Recursive method to print the tree structure"""
        if node != self.NIL:
            print(indent, end="")
            if last:
                print("└─", end="")
                indent += "  "
            else:
                print("├─", end="")
                indent += "│ "

            print(node)
            
            # Determine children to print
            children = []
            if node.left != self.NIL:
                children.append(node.left)
            if node.right != self.NIL:
                children.append(node.right)
            
            for i, child in enumerate(children):
                self._print_tree(child, indent, i == len(children) - 1)

    # [Rest of your existing RedBlackTree methods...]
    def insert(self, value):
        new_node = Node(value, left=self.NIL, right=self.NIL)
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if not parent:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k.parent and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.rotate_left(k.parent.parent)
        self.root.color = 'black'

    def search(self, value):
        def _search(node):
            if node == self.NIL or value == node.value:
                return node
            if value < node.value:
                return _search(node.left)
            return _search(node.right)

        result = _search(self.root)
        return result != self.NIL

    def get_black_height(self):
        def _black_height(node):
            if node == self.NIL:
                return 1
            left_black_height = _black_height(node.left)
            if node.color == 'black':
                return left_black_height + 1
            return left_black_height

        return _black_height(self.root)

    def transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def delete(self, value):
        z = self.root
        while z != self.NIL:
            if z.value == value:
                break
            elif value < z.value:
                z = z.left
            else:
                z = z.right

        if z == self.NIL:
            return  # Value not found

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    s = x.parent.right
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.rotate_right(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    s = x.parent.left
                if s.right.color == 'black' and s.left.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.rotate_left(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'


# Example Usage
rb_tree = RedBlackTree()
print("Initial tree:")
rb_tree.print_tree()

values_to_insert = [10, 20, 30, 15, 25, 5, 35]
for value in values_to_insert:
    rb_tree.insert(value)
    print(f"\nAfter inserting {value}:")
    rb_tree.print_tree()

print("\nSearch 20:", rb_tree.search(20))  # True
print("Black Height:", rb_tree.get_black_height())

rb_tree.delete(20)
print("\nAfter deleting 20:")
rb_tree.print_tree()

print("Search 20 after delete:", rb_tree.search(20))  # False
print("Black Height after delete:", rb_tree.get_black_height())