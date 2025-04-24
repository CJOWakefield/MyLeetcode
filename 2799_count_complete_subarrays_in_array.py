from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = len(set(nums))
        counts = {}
        res, left = 0, 0        
        for right, val in enumerate(nums):
            counts[val] = counts.get(val, 0) + 1
            while len(counts) == unique_count:
                res += len(nums) - right
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0: del counts[nums[left]]
                left += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countCompleteSubarrays([1, 3, 1, 2, 2]))
    print(sol.countCompleteSubarrays([5, 5, 5, 5]))
