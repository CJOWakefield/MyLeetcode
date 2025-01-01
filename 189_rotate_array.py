def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        curr = nums.pop()
        nums.insert(0, curr)

    return nums


if __name__ == '__main__':
    print(rotate([1, 2, 3, 4, 5], 5))
