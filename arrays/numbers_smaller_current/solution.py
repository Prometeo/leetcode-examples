def smaller_numbers(nums: list[int]) -> list[int] | None:
    ordered_nums: list = sorted((nums))
    nums_map: dict = {}
    result: list = list()
    for i, num in enumerate(ordered_nums):
        if num not in nums_map:
            nums_map[num] = i

    for i in nums:
        result.append(nums_map[i])
    return result
