from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        seen = set()
        for num in nums:
            if num > k and num not in seen: seen.add(num)
        return len(seen)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations(nums = [5,2,5,4,5], k = 2))
    print(sol.minOperations(nums = [2,1,2], k = 2))
    print(sol.minOperations(nums = [9,7,5,3], k = 1))