#lab2
#TASK1
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  
        self.tail = None
        self.count = 0 
        print("Created new LinkedList")
        print("Current size:", self.count)
        print("Head:", self.head)
    #TASK2
    def append(self, element):
        """Add an element to the end of the list"""
        new_node = Node(element)
        
        if self.head is None:
          
            self.head = new_node
            self.tail = new_node
        else:
            
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1
        print(f"Appended {element} to the list")
    
    def get(self, index):
        """Retrieve an element at a specific index"""
        if index < 0 or index >= self.count:
            print("Index out of bounds")
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        
        print(f"Element at index {index}: {current.data}")
        return current.data
    
    def set(self, index, element):
        """Replace an element at a specific index"""
        if index < 0 or index >= self.count:
            print("Index out of bounds")
            return
        
        current = self.head
        for i in range(index):
            current = current.next
        
        current.data = element
        print(f"Set element at index {index} to {element}")
    
    def size(self):
        """Return the current number of elements"""
        print("Current size:", self.count)
        return self.count
    
    def prepend(self, element):
        """Add an element at the beginning of the list"""
        new_node = Node(element)
        
        if self.head is None:
           
            self.head = new_node
            self.tail = new_node
        else:
          
            new_node.next = self.head
            self.head = new_node
        
        self.count += 1
        print(f"Prepended {element} to the list")
    
    def print_list(self):
        """Print all elements in the linked list"""
        if self.head is None:
            print("Linked list: []")
            return
        
        result = "["
        current = self.head
        while current:
            result += str(current.data) + " "
            current = current.next
        result = result.strip() + "]" 
        print(f"Linked list: {result}")

# Example usage
if __name__ == "__main__":
    # Task 1: Create the LinkedList
    my_list = LinkedList()
    
    # Task 2: Implement Basic Operations
    my_list.append(5)      
    my_list.get(0)          
    my_list.set(0, 10)      
    my_list.get(0)          
    my_list.size()         
    my_list.prepend(10)     
    my_list.append(5)       
    my_list.print_list()    