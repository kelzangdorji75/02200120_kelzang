class CustomList:
    def __init__(self, capacity=10):
        self._capacity = capacity  
        self._size = 0  
        self._array = [None] * self._capacity 
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")


my_list = CustomList()