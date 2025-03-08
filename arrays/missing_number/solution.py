def missing_number(nums: list[int]) -> int:
    nums.sort()
    for i in range(nums[0], len(nums)):
        if i != nums[i]:
            return i
    return len(nums)


def missing_number_range(nums: list[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)
