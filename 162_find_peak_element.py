class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mp = (left + right) // 2
            if nums[mp] > nums[mp+1]: right = mp
            else: left = mp + 1
        return left
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.findPeakElement([1,2,3,1]))
    print(problem.findPeakElement([1,2,1,3,5,6,4]))
    
    