from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        mode = counts.most_common(1)[0][0]
        left, right = 0, counts[mode]
        for i in range(n-1):
            if nums[i] == mode:
                left += 1
                right -= 1
                if left * 2 > i+1 and right * 2 > n-i-1: return i
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumIndex(nums = [1,2,2,2]))
    print(sol.minimumIndex(nums = [2,1,3,1,1,1,7,1,2,1]))
    print(sol.minimumIndex(nums = [3,3,3,3,7,2,2]))