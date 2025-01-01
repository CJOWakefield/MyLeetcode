def rob(nums: list[int]) -> int:
    curr, no_curr = nums[0], 0
    for i in range(1, len(nums)):
        new_curr, no_curr = no_curr + nums[i], max(curr, no_curr)
        curr = new_curr
    return max(curr, no_curr)


if __name__ == '__main__':
    print(rob([1, 4, 6, 1, 2, 3, 4, 5, 6, 9, 1, 3, 7]))
