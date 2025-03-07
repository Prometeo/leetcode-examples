def duplicated_elements_set(nums: list[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    return True


def duplicated_elements_brute_force(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == nums[i] and j != i:
                return True

    return False
