def check(nums: list[int]) -> bool:
    rotations = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            rotations += 1
            if rotations > 1: return False
    return True

if __name__ == '__main__':
    print(check(nums = [3,4,5,1,2]))
