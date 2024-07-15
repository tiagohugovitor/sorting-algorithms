# Bubble Sort is a simple comparison-based sorting algorithm.
# It works by repeatedly stepping through the list to be sorted, comparing each pair
# of adjacent items and swapping them if they are in the wrong order. This process
# is repeated until the list is sorted.

# Time Complexity: o(n²)
# Space Complexity: O(1), in place

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        changed = False
        for j in range(0, n - i -1):
            if array[j+1] < array[j]:
                array[j], array[j+1] = array[j+1], array[j]
                changed = True
        if not changed:
            break
    return array

# e.g: print(bubbleSort([9,8,7,6,5,4,3,2,1]))
