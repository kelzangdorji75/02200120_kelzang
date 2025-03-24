class ArrayStack:
    def __init__(self, capacity=10):
        self._capacity = capacity  # Default capacity
        self._stack = []  # Internal list to store stack elements
        self._top = -1  # Index to track the top element
        print(f"Created new ArrayStack with capacity: {self._capacity}")

    def push(self, element):
        if len(self._stack) >= self._capacity:
            print("Stack overflow: Cannot push element")
            return
        self._stack.append(element)
        self._top += 1
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack underflow: Cannot pop element")
            return None
        popped_element = self._stack.pop()
        self._top -= 1
        print(f"Popped element: {popped_element}")
        return popped_element

    def peek(self):
        if self.is_empty():
            print("Stack is empty: No top element")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]

    def is_empty(self):
        return self._top == -1

    def size(self):
        return self._top + 1

    def display(self):
        print(f"Display stack: {self._stack}")

# Example Usage:
stack = ArrayStack()
print("Stack is empty:", stack.is_empty())
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.peek()
stack.pop()
print("Stack size:", stack.size())
stack.display()
