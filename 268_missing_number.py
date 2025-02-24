class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected = (n * (n+1)) // 2
        return expected - sum(nums)

# Notes: Gaus formula. (n * (n+1)) // 2 is the sum of the first n natural numbers.

if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3,0,1]))
    print(sol.missingNumber([0,1]))
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
    print(sol.missingNumber([0]))
    