class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        res = 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                res += 1
            elif nums[left] + nums[right] < k: left += 1
            else: right -= 1
        return res
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.maxOperations([1,2,3,4], 5))
    print(problem.maxOperations([3,1,3,4,3], 6))
    