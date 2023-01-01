class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum=0;
        leftSum=0;
        for i in nums:
            totalSum = totalSum+i
        for i in range(len(nums)):
            if(totalSum-leftSum-nums[i]==leftSum):
                return i
            leftSum+=nums[i]
        return -1
        