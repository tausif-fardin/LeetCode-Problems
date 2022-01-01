def containsDuplicate(self, nums: List[int]) -> bool:
    num = set()

    for i in range(len(nums)):
        if nums[i] in num:
            return True
        else:
            num.add(nums[i])
    return False
