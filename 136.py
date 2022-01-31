# Single Number
from ast import List


def singleNumber(self, nums: List[int]) -> int:

    result = 0
    for n in nums:
        result ^= n
    return result
