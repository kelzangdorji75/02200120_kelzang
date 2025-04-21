#PART 2
def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            accesses += 2  # Reading left[i] and right[j]
            comparisons += 1  # One comparison between left[i] and right[j]
            if left[i] <= right[j]:
                result.append(left[i])
                accesses += 1  # Writing to result
                i += 1
            else:
                result.append(right[j])
                accesses += 1  # Writing to result
                j += 1

        while i < len(left):
            result.append(left[i])
            accesses += 1  # Writing to result
            i += 1

        while j < len(right):
            result.append(right[j])
            accesses += 1  # Writing to result
            j += 1

        return result

    def sort(subarray):
        nonlocal accesses, comparisons
        n = len(subarray)
        if n <= 1:
            return subarray

        mid = n // 2

        # Count accesses for slicing (each slice accesses all elements once)
        accesses += n

        left = sort(subarray[:mid])
        right = sort(subarray[mid:])
        return merge(left, right)

    accesses += len(arr)  # Copy the original array
    sorted_arr = sort(arr[:])

    return sorted_arr, comparisons, accesses
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list, num_comparisons, num_accesses = merge_sort(original_list)

print("Original List:", original_list)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", num_comparisons)
print("Number of array accesses:", num_accesses)
