class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        curr_min = curr_max = nums[0]
        res_max = res_min = nums[0]

        for i in range(1, len(nums)):
            res_max = max(res_max + nums[i], nums[i])
            res_min = min(res_min + nums[i], nums[i])

            curr_max = max(curr_max, res_max)
            curr_min = min(curr_min, res_min)

        return max(abs(curr_max), abs(curr_min))
    
    # Prefix sum version vs Kadane's algorithm. Prefix more efficient.

    ## Intuition: Difference between max and min prefix will provide absolute max for any subarray with the array.
    ## e.g. [1, -3, 2, 3, -4] -> prefix sums [1, -2, 0, 3, -1]. Therefore, max_sum = 3 (index 3), min_sum = -2 (index 1).
    ## So... abs_max = 3 - (-2) = 5.
    def maxAbsoluteSum_prefix_sum(self, nums: list[int]) -> int:
        curr, min_sum, max_sum = 0, 0, 0
        for num in nums:
            curr += num
            min_sum = min(min_sum, curr)
            max_sum = max(max_sum, curr)
        return max_sum - min_sum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAbsoluteSum([1,2,3,4,5]))
    print(sol.maxAbsoluteSum([-1,-2,-3,-4,-5]))
    print(sol.maxAbsoluteSum([1,2,3,-2,5,-1]))
    print(sol.maxAbsoluteSum([-1,2,-3,4,-5]))
    print(sol.maxAbsoluteSum([-1,2,-3,4,-5]))
