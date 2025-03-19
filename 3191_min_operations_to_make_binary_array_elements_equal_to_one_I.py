from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res, pos = 0, 0
        while pos < len(nums)-2:
            if nums[pos] == 0: 
                nums[pos], nums[pos+1], nums[pos+2] = nums[pos] ^ 1, nums[pos+1] ^ 1, nums[pos+2] ^ 1
                res += 1
            pos += 1
        if not all(nums[-3::]) > 0: return -1
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([1,1,1]))
    print(solution.minOperations([1,1,0,1,1]))
    print(solution.minOperations([1,1,0,1,1,0]))
    print(solution.minOperations([1,1,0,1,1,0,0]))
    print(solution.minOperations([1,1,0,1,1,0,0,1]))