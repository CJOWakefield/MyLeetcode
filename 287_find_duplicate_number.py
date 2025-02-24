class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen: return nums[i]
            seen.add(nums[i])

if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate([1,3,4,2,2]))
    print(sol.findDuplicate([3,1,3,4,2]))
    print(sol.findDuplicate([1,1]))
    print(sol.findDuplicate([1,1,2]))
    