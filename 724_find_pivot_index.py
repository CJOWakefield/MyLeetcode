class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            curr = nums[i]
            right -= curr
            if left == right: return i
            left += curr
        return -1
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.pivotIndex([1,7,3,6,5,6]))
    print(problem.pivotIndex([1,2,3]))
    print(problem.pivotIndex([2,1,-1]))