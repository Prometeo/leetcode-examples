def two_sum(nums: list[int], target: int) -> list:
    if len(nums) == 2:
        return [0, 1]
    for i in nums:
        r = target - i
        if r in nums and (nums.index(i) != nums.index(r)):
            return [nums.index(i), nums.index(r)]
    return []


def two_sum_hm(nums: list[int], target: int) -> list:
    hash_map = {}
    for k, v in enumerate(nums):
        r = target - v
        if r in hash_map:
            return [k, hash_map[r]]
        else:
            hash_map[v] = k
    return []
