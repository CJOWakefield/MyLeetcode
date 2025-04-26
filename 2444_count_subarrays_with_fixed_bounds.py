from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        total = 0
        last_invalid, last_min, last_max = -1, -1, -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK: last_invalid = i
            if num == minK: last_min = i
            if num == maxK:last_max = i
            valid_start = min(last_min, last_max)
            total += max(0, valid_start - last_invalid)
        return total
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))
