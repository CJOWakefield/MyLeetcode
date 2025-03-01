class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:    
        pos, n = 0, len(nums)
        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                nums[i], nums[pos] = 0, nums[i]
                pos += 1
        return nums
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.applyOperations([1,2,2,1,1,0]))
    print(sol.applyOperations([0,1]))
    
    
