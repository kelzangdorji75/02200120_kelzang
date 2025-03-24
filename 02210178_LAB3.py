#LAB3 Task 3 and 4
class Node:
    def __init__(self, data=None):
        self.data = data  # Stores the element
        self.next = None  # Points to the next node in the stack

class LinkedStack:
    def __init__(self):
        self.top = None  # Points to the first node (head of the linked list)
        self.size = 0  # Tracks the number of elements in the stack
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.size == 0
    
    def push(self, element):
        """Add an element to the top of the stack."""
        new_node = Node(element)  # Create a new node
        new_node.next = self.top  # Link new node to the current top node
        self.top = new_node  # Update top to the new node
        self.size += 1  # Increase size of the stack
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        """Remove and return the element at the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")  # Stack is empty
        popped_data = self.top.data  # Get the data of the top node
        self.top = self.top.next  # Update top to the next node
        self.size -= 1  # Decrease size of the stack
        print(f"Popped element: {popped_data}")
        self.display()

    def peek(self):
        """Return the element at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")  # Stack is empty
        return self.top.data  # Return the data of the top node
    
    def size(self):
        """Return the current number of elements in the stack."""
        return self.size
    
    def display(self):
        """Display all elements in the stack."""
        if self.is_empty():
            print("Display stack: []")
            return
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(f"Display stack: {elements}")
    
# Example usage:
stack = LinkedStack()
print("Created new LinkedStack")
print(f"Stack is empty: {stack.is_empty()}")  # True

# Perform operations
stack.push(10)  # Push 10
stack.push(20)  # Push 20
stack.push(30)  # Push 30

# Peek the top element
print(f"Top element: {stack.peek()}")  # 30

# Pop the top element
stack.pop()  # Pop 30

# Check stack size
print(f"Stack size: {stack.size}")  # 2