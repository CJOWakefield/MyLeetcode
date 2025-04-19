from collections import Counter
from typing import List
from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        counts = Counter(nums)
        res = 0
        for i, val in enumerate(nums):
            counts[val] -= 1
            x, y = lower - val, upper - val
            for k, v in counts.items():
                if x <= k <= y and v: res += v
        return res
    
    # Time complexity O(n * k)

    def countFairPairs_II(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        for i, val in enumerate(nums):
            left = bisect_left(nums, lower - val, i+1)
            right = bisect_right(nums, upper - val, i+1)
            res += right - left
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countFairPairs([0,1,7,4,4,5], 3, 6))
    print(sol.countFairPairs([1,7,9,2,5], 11, 11))
    print(sol.countFairPairs([1,1,1,7,8], 1, 10))
    print(sol.countFairPairs([1,1,1,7,8], 1, 10))
    print(sol.countFairPairs_II([0,1,7,4,4,5], 3, 6))
    print(sol.countFairPairs_II([1,7,9,2,5], 11, 11))
    print(sol.countFairPairs_II([1,1,1,7,8], 1, 10))
    print(sol.countFairPairs_II([1,1,1,7,8], 1, 10))
