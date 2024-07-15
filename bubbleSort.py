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

print(bubbleSort([9,8,7,6,5,4,3,2,1]))
