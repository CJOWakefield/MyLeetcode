def rob_II(nums: list[int]) -> int:
    res = []
    if len(nums) < 2:
        return max(nums)

    for arr in [nums[1:], nums[:-1]]:
        curr, no_curr = arr[0], 0
        for i in range(1, len(arr)):
            new_curr, no_curr = no_curr + arr[i], max(curr, no_curr)
            curr = new_curr
        res.append(max(curr, no_curr))
    return max(res)

if __name__ == '__main__':
    print(rob_II([1, 2, 3, 4, 5, 6, 7, 8, 9]))
