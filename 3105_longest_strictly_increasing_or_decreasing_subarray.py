def longestMonotonicSubarray(nums: list[int]) -> int:
    increasing, decreasing, res = 1, 1, 0
    if len(nums) == 1: return 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            increasing += 1
            decreasing = 1
        elif nums[i] < nums[i-1]:
            increasing = 1
            decreasing += 1
        else:
            increasing = decreasing = 1
        res = max(increasing, decreasing, res)
    return res

if __name__ == '__main__':
    print(longestMonotonicSubarray([1, 2, 3, 2, 7, 6, 1]))
