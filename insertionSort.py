# Insertion Sort is a simple and intuitive sorting method.
# It iterates through the array, taking one element at a time and inserting it
# into its correct position among the previously sorted elements. This process
# continues until the entire array is sorted.

# Time complexity: O(n²)
# Space complexity: O(1), in place

def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        j = i - 1
        value = array[i]
        while j >= 0 and value < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = value
    return array

# e.g: print(insertionSort([9,8,7,6,5,4,3,2]))
