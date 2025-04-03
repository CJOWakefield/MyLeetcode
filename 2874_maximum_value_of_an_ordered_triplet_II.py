from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * (n+1), [0] * (n+1)
        for i in range(n): 
            left[i+1] = max(nums[i], left[i])
            right[n-i-1] = max(nums[n-i-1], right[n-i])
        return max(max(0, (left[i]-nums[i]) * right[i+1]) for i in range(1, n-1))
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.maximumTripletValue(nums = [12,6,1,2,7]))
    print(problem.maximumTripletValue(nums = [1,10,3,4,19]))
    print(problem.maximumTripletValue(nums = [1,2,3]))
    print(problem.maximumTripletValue(nums = [2,3,1]))
    print(problem.maximumTripletValue(nums = [10,13,6,2]))
    