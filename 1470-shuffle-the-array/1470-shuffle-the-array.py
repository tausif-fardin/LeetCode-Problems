class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums) // 2):
            result[2 * i] = nums[i]
            result[2 * i + 1] = nums[i + len(nums) // 2]
        return result