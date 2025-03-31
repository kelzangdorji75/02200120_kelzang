#Part 2: Queue implementation using Linked List 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        print("Created new LinkedQueue")

    def is_empty(self):
        return self._size == 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued {element} to the queue")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        print(f"Dequeued element: {removed_data}")
        return removed_data
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty, no front element")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data
    
    def size(self):
        print(f"Queue size: {self._size}")
        return self._size
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Display queue:[" + ",".join(elements) + "]")

# Example Usage:
queue = LinkedQueue()
print("Queue is empty:", queue.is_empty())
queue.enqueue(10)
queue.display()
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
queue.peek()
queue.dequeue()
queue.display()
queue.size()
