from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, curr, left = 0, 0, 0
        for right in range(len(nums)):
            curr += nums[right]
            while left <= right and curr * (right - left + 1) >= k:
                curr -= nums[left]
                left += 1
            res += right - left + 1
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([2,1,4,3,5], 10))
    print(solution.countSubarrays([1, 1, 1], 5))
