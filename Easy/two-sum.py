def two_sum(nums, target):
    for i in range(len(nums)):
        if len(nums) == 1:
            return i
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))
