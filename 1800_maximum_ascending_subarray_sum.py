def maxAscendingSum(nums: list[int]) -> int:
    res = curr = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]: curr += nums[i]
        else: curr = nums[i]
        res = max(curr, res)
    return res

if __name__ == '__main__':
    print(maxAscendingSum([10, 20, 30, 5, 10, 50]))
