from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res, count, prefix = 0, 0, defaultdict(int)
        prefix[0] = 1
        for num in nums:
            if num % modulo == k: count += 1
            rem = count % modulo
            target_rem = (rem - k) % modulo
            res += prefix[target_rem]
            prefix[rem] += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countInterestingSubarrays([3, 2, 4], 2, 1))
    print(sol.countInterestingSubarrays([3, 1, 9, 6], 3, 0))