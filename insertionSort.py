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

print(insertionSort([9,8,7,6,5,4,3,2]))
