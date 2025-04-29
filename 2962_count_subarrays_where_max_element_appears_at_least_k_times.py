from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, curr, left, val = 0, 0, 0, max(nums)
        for right in range(len(nums)):
            if nums[right] == val: curr += 1
            while curr >= k:
                if nums[left] == val: curr -= 1
                left += 1
            res += left
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1, 3, 2, 3, 3], 2))
    print(solution.countSubarrays([1, 4, 2, 1], 3))
    print(solution.countSubarrays([1, 2, 3, 4, 5], 3))
