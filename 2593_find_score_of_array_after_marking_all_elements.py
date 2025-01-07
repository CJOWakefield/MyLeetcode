def findScore(nums: list[int]) -> int:
    res, pos, n = 0, 0, len(nums)
    while pos < n:
        odd = even = 0
        while pos + 1 < n and nums[pos] > nums[pos+1]:
            if pos & 1: odd += nums[pos]
            else: even += nums[pos]
            pos += 1
        res += (odd if (pos & 1) else even) + nums[pos]
        print(pos, odd, even, res, nums[pos])
        pos += 2
    return res

if __name__ == '__main__':
    print(findScore([2, 1, 3, 4, 5, 2]))
