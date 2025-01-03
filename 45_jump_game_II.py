def jump(nums: list[int]) -> int:
    res, curr_max, total_max = 0, 0, 0
    for i in range(len(nums)-1):
        total_max = max(total_max, i + nums[i])
        print(i, nums[i], curr_max, total_max)
        if i == curr_max:
            res += 1
            curr_max = total_max
    return res

if __name__ == '__main__':
    print(jump([2,3,1,1,4]))
