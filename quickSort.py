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

print(quickSort([9,8,7,6,5,4,2,3,1], 0, 8))