def productExceptSelf(nums: list[int]) -> list[int]:
    left_count, right_count = 1, 1
    left_vals, right_vals = [0] * len(nums), [0] * len(nums)

    for i in range(len(nums)):
        left, right = i, -i-1
        left_vals[left], right_vals[right] = left_count, right_count
        left_count *= nums[left]
        right_count *= nums[right]

    # print(left_vals, right_vals)
    return [l*r for l, r in zip(left_vals, right_vals)]

# Notes: Some convoluted intuition here. Two lists, iterating essentially in parallel. One multiplies the aggregate from the left, and the other from the right.
#        so with both lists from each direction, we can just multiply the value at each indices between the two lists to multiply with the aggregate up to that point on the left,
#        and up to that point from the right.

if __name__ == '__main__':
    print(productExceptSelf([1, 4, 7, 10, -1, 3, 6]))
