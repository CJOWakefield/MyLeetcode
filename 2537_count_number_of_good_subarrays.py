from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts, left, curr, res = defaultdict(int), 0, 0, 0
        for right, val in enumerate(nums):
            curr += counts[val]
            counts[val] += 1
            while curr >= k:
                counts[nums[left]] -= 1
                curr -= counts[nums[left]]
                res += len(nums) - right
                left += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countGood([1, 1, 1, 7, 8, 9], 3))
    print(sol.countGood([1, 1, 2, 2, 3], 2))
    print(sol.countGood([1, 1, 2, 2, 3], 4))
    print(sol.countGood([1, 1, 2, 2, 3], 5))
    print(sol.countGood([1, 1, 2, 2, 3], 6))