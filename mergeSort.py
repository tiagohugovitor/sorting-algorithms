# Merge Sort is a divide-and-conquer sorting method.
# It recursively splits the array into halves until each subarray has a single element,
# then merges these subarrays back together in a sorted manner.

# Time complexity: O(nlogn)
# Space complexity: O(n), due to the additional temporary arrays used for merging.

def mergeSort(array, start, end):
    if start < end:
        mid = (start + end) //2
        mergeSort(array, start, mid)
        mergeSort(array, mid + 1, end)
        merge(array, start, mid, end)
    return array

def merge(array, start, mid, end):
    left = [0] * (mid - start + 1)
    right = [0] * (end - mid)

    for i in range(mid - start + 1):
        left[i] = array[start + i]

    for i in range(end - mid):
        right[i] = array[mid + 1 + i]

    leftPointer = 0
    rightPointer = 0
    
    while leftPointer < (mid - start + 1) and rightPointer < (end - mid):
        if(left[leftPointer] <= right[rightPointer]):
            array[start + leftPointer + rightPointer] = left[leftPointer]
            leftPointer += 1
        else:
            array[start + leftPointer + rightPointer] = right[rightPointer]
            rightPointer += 1
    
    while leftPointer < (mid - start + 1):
        array[start + leftPointer + rightPointer] = left[leftPointer]
        leftPointer += 1
    
    while rightPointer < (end - mid):   
        array[start + leftPointer + rightPointer] = right[rightPointer]
        rightPointer += 1

# e.g: print(mergeSort([9,8,7,6], 0, 3))
