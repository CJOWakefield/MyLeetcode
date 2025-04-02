from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i_max, j_min, k_max = nums[0], float('inf'), 0
        res = 0
        for i in range(1, len(nums)):
            if j_min != float('inf'): res = max(res, (i_max - j_min) * nums[i])
            if nums[i] > i_max: 
                i_max = nums[i]
            elif nums[i] < j_min: j_min = nums[i]
            elif nums[i] > k_max: 
                k_max = nums[i]
                if j_min != float('inf'): res = max(res, (i_max - j_min) * k_max)
        return res
    
    def maximumTripletValue_prefix(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i in range(n-1): left[i+1] = max(nums[i], left[i])
        for i in range(n-2, -1, -1): right[i] = max(nums[i+1], right[i+1])
        
        res = 0
        for i in range(1, n-1):
            res = max(res, (left[i]-nums[i]) * right[i])
        return res
    
# Notes: First solution not successful. Issues for small edge cases, quicker to change strategy than identify the exact issues. Prefix sum
# first thought but wanted to attempt in single pass. In the end, prefix sum more efficient and straightforward.

if __name__ == "__main__":
    problem = Solution()
    print(problem.maximumTripletValue(nums = [12,6,1,2,7]))
    print(problem.maximumTripletValue(nums = [1,10,3,4,19]))
    print(problem.maximumTripletValue(nums = [1,2,3]))
    print(problem.maximumTripletValue(nums = [18,15,8,13,10,9,17,10,2,16,17]))
    print(problem.maximumTripletValue(nums = [8,6,3,13,2,12,19,5,19,6,10,11,9]))

    print(problem.maximumTripletValue_prefix(nums = [12,6,1,2,7]))
    print(problem.maximumTripletValue_prefix(nums = [1,10,3,4,19]))
    print(problem.maximumTripletValue_prefix(nums = [1,2,3]))
    print(problem.maximumTripletValue_prefix(nums = [18,15,8,13,10,9,17,10,2,16,17]))
    print(problem.maximumTripletValue_prefix(nums = [8,6,3,13,2,12,19,5,19,6,10,11,9]))