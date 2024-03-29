class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf') for _ in range(n)]
        dp[0] = 0
        for i in range(n):
            for j in range(nums[i]+1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n-1]



