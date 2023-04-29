class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        return closest_sum