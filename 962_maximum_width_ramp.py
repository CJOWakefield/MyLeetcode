class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        res, stack = 0, []
        for i, num in enumerate(nums):
            while not stack or nums[stack[-1]] > num:
                stack.append(i)
                
        for j in range(len(nums)-1, -1, -1):
            if not stack: return res
            while stack and nums[j] >= nums[stack[-1]]:
                pos = stack.pop()
                res = max(res, j - pos) 
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxWidthRamp([6,0,8,2,1,5]))
    print(sol.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))
    