# Approach-1
def maxSubArray(self, nums: List[int]) -> int:
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub

# Approch-2 using Kadane's Algorithm


def maxSubArray(self, nums: List[int]) -> int:
    maximum = max(nums)

    # if the list contains all negative values, return the maximum element
    if maximum < 0:
        return maximum

    # stores the maximum sum sublist found so far
    max_so_far = 0

    # stores the maximum sum of sublist ending at the current position
    max_ending_here = 0

    # do for each element of a given list
    for i in nums:

        # update the maximum sum of sublist "ending" at index `i` (by adding the
        # current element to maximum sum ending at previous index `i-1`)
        max_ending_here = max_ending_here + i

        # if the maximum sum is negative, set it to 0 (which represents
        # an empty sublist)
        max_ending_here = max(max_ending_here, 0)

        # update the result if the current sublist sum is found to be greater
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
