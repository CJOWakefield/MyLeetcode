def waysToSplitArray(nums: list[int]) -> int:
    res, left, right = 0, 0, sum(nums)
    for i in range(len(nums)-1):
        left += nums[i]
        right -= nums[i]
        if left >= right: res += 1
    return res

if __name__ == '__main__':
    print(waysToSplitArray([1, 7, 10, -4, -6, 3, 9, 4, 1, -2, 0, 1]))
