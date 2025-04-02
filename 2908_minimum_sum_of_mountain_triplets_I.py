from typing import List

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [nums[0]] * n, [nums[-1]] * n
        for i in range(n-1): left[i+1] = min(nums[i], left[i])
        for i in range(n-2, -1, -1): right[i] = min(nums[i], right[i+1])

        res = float('inf')
        for i in range(1, n-1):
            if left[i] < nums[i] and right[i] < nums[i]: res = min(res, (left[i] + nums[i] + right[i]))
        return res if res < float('inf') else -1
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.minimumSum(nums = [8,6,1,5,4]))
    print(problem.minimumSum(nums = [5,4,8,7,10,2]))
    print(problem.minimumSum(nums = [6,5,4,3,4,5]))
    