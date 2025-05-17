class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:
                mid += 1
        return nums

# Notes: Simple solution, swapping based on three pointers thus O(n) time complexity. Initial attempt with for i in range(len(nums)) loop but mid pointer more effective.

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortColors([1, 0, 0, 1, 2, 0, 1, 0, 2, 2, 0, 1]))
