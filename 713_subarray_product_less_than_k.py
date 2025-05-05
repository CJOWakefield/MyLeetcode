from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res, left, curr = 0, 0, 1
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k and left <= right: 
                curr //= nums[left]
                left += 1
            res += right - left + 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(sol.numSubarrayProductLessThanK([1, 2, 3], 0))
    print(sol.numSubarrayProductLessThanK([1, 1, 1], 2))
    print(sol.numSubarrayProductLessThanK([1, 1, 1], 1))
    print(sol.numSubarrayProductLessThanK([1, 1, 1], 0))