class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0;
        newNums=[];
        for i in nums:
            sum = sum+i
            newNums.append(sum)
        return newNums