from typing import List
from collections import defaultdict
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        seen = defaultdict(int)
        if not nums[0] + nums[1] > nums[2]: return 'none'
        for num in nums: seen[num] += 1
        if len(seen) == 1: return 'equilateral'
        if len(seen) == 2: return 'isosceles'
        else: return 'scalene'

if __name__ == "__main__":
    sol = Solution()
    print(sol.triangleType([2, 2, 3]))
    print(sol.triangleType([1, 1, 1]))
    print(sol.triangleType([1, 2, 3]))
    print(sol.triangleType([1, 1, 2]))
    print(sol.triangleType([1, 2, 2]))