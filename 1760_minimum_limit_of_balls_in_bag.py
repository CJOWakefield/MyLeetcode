def minimumSize(nums: list[int], maxOperations: int) -> int:
    left, right = 1, max(nums)
    while left < right:
        mp = (left + right) // 2
        bags = sum((num-1) // mp for num in nums)
        if bags <= maxOperations: right = mp
        else: left = mp + 1
    return right

if __name__ == '__main__':
    print(minimumSize(nums = [2,4,8,2], maxOperations = 4))
