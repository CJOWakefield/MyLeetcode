from typing import List
from bisect import bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0] > 0 or nums[-1] < 0: return len(nums)
        left, right = 0, len(nums)
        while left < right:
            mp = (left + right) // 2
            if nums[mp] >= 0: right = mp
            else: left = mp+1
                
        neg, pos = left, len(nums)-left
        while left < len(nums) and nums[left] == 0:
            pos -= 1
            left += 1
        return max(neg, pos)
    
    # Second faster solution but utilising external library.
    
    def maximumCount_II(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = bisect_left(nums, 1)
        return max(neg, len(nums)-pos)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumCount([-2,-1,-1,1,2,3]))
    print(sol.maximumCount([-3,-2,-1,0,0,1,2]))
    print(sol.maximumCount([5,20,66,1314]))
    print(sol.maximumCount_II([-2,-1,-1,1,2,3]))
    print(sol.maximumCount_II([-3,-2,-1,0,0,1,2]))
    print(sol.maximumCount_II([5,20,66,1314]))