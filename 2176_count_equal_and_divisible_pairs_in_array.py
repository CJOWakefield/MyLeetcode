from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counts = defaultdict(list)
        res = 0
        for i, num in enumerate(nums):
            seen = counts[num]
            if seen:
                for val in seen:
                    if (i * val) % k == 0: res += 1
            counts[num].append(i)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countPairs([3, 1, 2, 2, 2, 1, 3], 2))
    print(sol.countPairs([1, 2, 3, 4], 1))
