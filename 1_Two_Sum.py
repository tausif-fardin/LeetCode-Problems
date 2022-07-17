from operator import le
from typing import List
# Brute force solution


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i]+nums[j]
            if sum == target:
                return [i, j]

# O(n) better solution


def twoSum(self, nums: List[int], target: int) -> List[int]:
    complementMap = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if num in complementMap:
            return [complementMap[num], i]
        else:
            complementMap[complement] = i

# O(nlogn)


def twoSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1

    while left < right:
        currentSum = array[left]+array[right]
        if(currentSum == targetSum):
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
