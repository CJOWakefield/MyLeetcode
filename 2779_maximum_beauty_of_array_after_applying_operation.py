class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        res, left, right = 0, 0, 0
        while right < len(nums):
            curr = nums[right] - nums[left]
            while curr > k * 2:
                left += 1
                curr = nums[right] - nums[left]
            res = max(res, right - left + 1)
            right += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumBeauty([1,2,3,4,5], 2))
    print(sol.maximumBeauty([1,2,3,4,5], 3))
    print(sol.maximumBeauty([1,2,3,4,5], 4))