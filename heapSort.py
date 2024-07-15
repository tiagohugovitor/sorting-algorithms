# Heap Sort is an efficient sorting method based on the Heap data structure.
# It builds a max heap from the input array and then repeatedly extracts the largest
# element from the heap (the root) and places it in its correct position in the array.
# This process is repeated until the entire array is sorted.

# Time Complexity: O(nlogn)
# Space Complexity: O(1), in place

def parent(index):
    return (index - 1) // 2

def left(index):
    return (2 * index) + 1

def right(index):
    return (2 * index) + 2

def buildMaxHeap(array, heapSize):
    for i in range(heapSize//2 -1, -1, -1):
        fixMaxHeap(array, heapSize, i)

def fixMaxHeap(array, heapSize, index):
    l = left(index)
    r = right(index)
    if l < heapSize and array[l] > array[index]:
        max = l
    else:
        max = index
    if r < heapSize and array[r] > array[max]:
        max = r
    if max != index:
        array[index], array[max] = array[max], array[index]
        fixMaxHeap(array, heapSize, max)

def heapSort(array):
    heapSize = len(array)
    buildMaxHeap(array, heapSize)
    for i in range(heapSize - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapSize -= 1
        fixMaxHeap(array, heapSize, 0)
    return array

# e.g: print(heapSort([9,7,6,4,3]))
