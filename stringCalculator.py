def add(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return int(nums)
    if len(nums) == 3:
        return int(nums[0]) + int(nums[-1])