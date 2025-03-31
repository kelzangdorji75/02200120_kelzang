#LAB 4-Part 1
class ArrayQueue:
    def __init__(self, capacity=10):
        # Initialize the queue with a given capacity or default to 10
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        print(f"Created new Queue with capacity: {self.capacity}")
        print(f"Queue is empty: {self.is_empty()}")
    
    def is_empty(self):
        # Check if the queue is empty
        return self.size == 0
    
    def is_full(self):
        # Check if the queue is full
        return self.size == self.capacity
    
    def enqueue(self, element):
        # Add an element to the rear of the queue
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.queue[self.rear] = element
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        print(f"Enqueued {element} to the queue")
        self.display()
    
    def dequeue(self):
        # Remove and return the element at the front of the queue
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued element: {element}")
        self.display()
        return element
    
    def peek(self):
        # Return the element at the front without removing it
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]
    
    def size(self):
        # Return the current number of elements in the queue
        return self.size
    
    def display(self):
        # Show all elements in the queue
        if self.is_empty():
            print("Queue is empty")
        else:
            elements = []
            i = self.front
            for _ in range(self.size):
                elements.append(self.queue[i])
                i = (i + 1) % self.capacity
            print(f"Display queue: {elements}")


# Example usage:
queue = ArrayQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(f"Front element: {queue.peek()}")
queue.dequeue()
print(f"Queue size: {queue.size}")