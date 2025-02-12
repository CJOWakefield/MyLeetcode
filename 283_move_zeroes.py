class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        return nums
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.moveZeroes([0,1,0,3,12]))
    print(problem.moveZeroes([0]))
    