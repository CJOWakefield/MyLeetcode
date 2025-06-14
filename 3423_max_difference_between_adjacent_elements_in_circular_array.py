from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = abs(nums[-1] - nums[0])
        for i in range(len(nums)-1):
            curr = abs(nums[i] - nums[i+1])
            diff = max(curr, diff)
        return diff
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxAdjacentDistance(nums = [1, 2, 4]))
    print(solution.maxAdjacentDistance(nums = [-5, -10, -5]))