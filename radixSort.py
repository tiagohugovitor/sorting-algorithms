# Radix Sort sorts integers by processing digits individually, from the least
# significant digit (LSD) to the most significant digit (MSD). It repeatedly
# uses a stable sorting method like Counting Sort for each digit position,
# producing a fully sorted list.

# Time complexity: O(d * (n + k)), where d is the number of digits in the longest number,
# n is the number of elements, and k is the range of the input. 
# Space complexity is O(n + k), due to auxiliary data structures used for counting and sorting.


def countingSortForRadix(nums, exp):
    count = [0] * 10
    numsSorted = [0] * len(nums)

    for j in range(len(nums)):
        digit = (nums[j] // exp) % 10
        count[digit] += 1

    for j in range(1, 10):
        count[j] += count[j - 1]

    for j in range(len(nums) - 1, -1, -1):
        digit = (nums[j] // exp) % 10
        numsSorted[count[digit] - 1] = nums[j]
        count[digit] -= 1
        j -= 1

    return numsSorted


def radixSort(nums):
    maxNum = nums[0]
    for number in nums:
        if number > maxNum:
            maxNum = number
    exp = 1
    while maxNum // exp > 0:
        nums = countingSortForRadix(nums, exp)
        exp *= 10
    return nums

# e.g: print(radixSort([170, 45, 75, 90, 802, 24, 2, 66]))
