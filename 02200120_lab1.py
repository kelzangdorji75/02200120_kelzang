#Task 1
#Task 1
class CustomList:
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._size = 0  
        self._array = [None] * self._capacity 
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")


my_list = CustomList()

#Task 2
class SimpleList:
    def __init__(self):
        self.data = []
    
    def append(self, element):
        self.data.append(element)
        print(f"Appended {element} to the list")
    
    def get(self, index):
        if 0 <= index < len(self.data):
            print(f"Element at index {index}: {self.data[index]}")
        else:
            print("Invalid index")
    
    def set(self, index, element):
        if 0 <= index < len(self.data):
            self.data[index] = element
            print(f"set element at index {index} to {element}")
        else:
            print("Invalid index")
    
    def size(self):
        print(f"currrent size: {len(self.data)}")

# Example usage
lst = SimpleList()
lst.append(5)
lst.get(0)
lst.set(0, 10)
lst.get(0)
lst.size()          