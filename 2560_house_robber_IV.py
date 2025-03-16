from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left < right:
            mp = (left + right) // 2
            curr, rem = 0, k
            while curr < len(nums) and rem > 0:
                if nums[curr] <= mp:
                    rem -= 1
                    curr += 1
                curr += 1

            if rem > 0: left = mp+1
            else: right = mp
        return left
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minCapability([2,3,5,9], 2))
    print(solution.minCapability([2,7,9,3,1], 2))
    print(solution.minCapability([1,2,3,4,5,6], 3))
    print(solution.minCapability([1,2,3,4,5,6], 4))
    print(solution.minCapability([1,2,3,4,5,6], 5))