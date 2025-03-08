def find_missing_numbers(nums: list[int]) -> list:
    missing_numbers = []
    set_of_values = set(nums)
    # range_of_numbers = [i for i in range(1, len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        if i not in set_of_values:
            missing_numbers.append(i)
    return missing_numbers
