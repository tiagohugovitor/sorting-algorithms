# Quick Sort is an efficient and widely used sorting method.
# It selects a pivot element and partitions the array into subarrays of elements
# less than and greater than the pivot, then recursively sorts the subarrays.

# Time complexity: O(nlogn)
# Space complexity: O(logn), due to the recursive stack usage.

import random

def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)
        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)
    return array

def partition(array, start, end):
    pivot = random.randint(start, end)
    array[start], array[pivot] = array[pivot], array[start]
    p = start + 1
    q = start + 1
    while q <= end: 
        if(array[q] < array[start]):
            array[p], array[q] = array[q], array[p]
            p += 1
        q += 1
    array[start], array[p-1] = array[p-1], array[start]
    return p-1

# e.g: print(quickSort([9,8,7,6,5,4,2,3,1], 0, 8))
