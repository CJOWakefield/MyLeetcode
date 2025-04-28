from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i+2] == nums[i+1] / 2: res += 1
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1, 2, 1, 4, 1]))
    print(solution.countSubarrays([1, 1, 1]))
    print(solution.countSubarrays([1, 2, 3, 4, 5]))
    print(solution.countSubarrays([1, 2, 3, 4, 5, 6]))
