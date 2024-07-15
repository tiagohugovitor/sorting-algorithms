# Counting Sort is suitable for sorting integers within a specific range.
# It counts occurrences of each element, adjusts these counts to determine
# the final positions of elements in the sorted array, and places each
# element accordingly.

# Time complexity: O(n + k), where n is the number of elements in the array and k is the range of the elements.
# Space complexity is O(n + k), due to auxiliary data structures used for counting and sorting.

def countingSort(nums, k):
    count = [0] * (k + 1)
    numsSorted = [0] * len(nums)
    for j in range(0, len(nums)):
        count[nums[j]] += 1
    for j in range(1, k+1):
        count[j] = count[j] + count[j-1]
    for j in range(len(nums) - 1, -1, -1):
        numsSorted[count[nums[j]] - 1] = nums[j]
        count[nums[j]] -= 1
    return numsSorted 

# e.g: print(countingSort([3,3,4,5,6,7,1,2,3], 9))
