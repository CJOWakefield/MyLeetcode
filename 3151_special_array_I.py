def isArraySpecial(nums: list[int]) -> bool:
    if len(nums) == 1: return True
    for i in range(len(nums)-1):
        if nums[i] % 2 == nums[i+1] % 2: return False
    return True

if __name__ == '__main__':
    print(isArraySpecial([1, 2, 2, 6, 1, 2, 1, 4, 3]))
