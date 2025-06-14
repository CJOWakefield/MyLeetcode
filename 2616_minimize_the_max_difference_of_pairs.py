from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]

        def valid(curr_max):
            i, curr = 0, 0
            while i < n-1:
                if nums[i+1] - nums[i] <= curr_max:
                    curr += 1
                    i += 2
                else: i += 1
            return curr >= p
        
        while left < right:
            mp = (left + right) // 2
            if valid(mp): right = mp
            else: left = mp + 1
        return left

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    print(solution.minimizeMax(nums = [4,2,1,2], p = 1))
