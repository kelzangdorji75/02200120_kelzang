#LAB5 PART2 (using recursive binary search)

def binary_search(arr, target, low=0, high=None, comparisons=0): 
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1, comparisons  #

    mid = (low + high) // 2
    comparisons += 1 

    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search(arr, target, low, mid - 1, comparisons)


arr = [12, 23, 34, 45, 56, 67, 89]  
target = 56  

print("Sorted List:", arr)
print(f"Searching for {target} using Binary Search...")

index, comparisons = binary_search(arr, target)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {comparisons}")