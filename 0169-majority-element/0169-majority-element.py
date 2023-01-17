class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, value in dic.items():
            if value > len(nums)/2:
                return key
        