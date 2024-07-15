# Bucket Sort divides the unsorted list into a finite number of "buckets", each of which
# is then sorted individually using a stable sorting method like insertion sort or by
# applying Bucket Sort recursively.

# Time complexity: O(n + k), where n is the number of elements in the array and k is the number
# of buckets.
# Space complexity is O(n + k), due to the auxiliary data structures used for sorting and storage of buckets.

from insertionSort import insertionSort

def bucketSort(nums):
    numBuckets = 10
    buckets = [[] for _ in range(numBuckets)]

    for num in nums:
        index = int(num * numBuckets)
        buckets[index].append(num)

    for i in range(numBuckets):
        insertionSort(buckets[i])
    
    k = 0
    for i in range(numBuckets):
        for num in buckets[i]:
            nums[k] = num
            k += 1

    return nums

# e.g: print(bucketSort([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]))
