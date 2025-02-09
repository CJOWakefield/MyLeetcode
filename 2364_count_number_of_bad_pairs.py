class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        res, vals = 0, {}
        for i, val in enumerate(nums):
            curr = val - i
            res += vals.get(curr, 0)
            vals[curr] = vals.get(curr, 0) + 1

        return ((len(nums) * (len(nums)-1)) // 2) - res

# Intuition: As we iterate through sample, we track occurrences of each nums[i] - i value. If a value repeats, then a new valid pair is formed. Simply remove the total of good
# pairs from the total possible pairs to get the bad pairs.

if __name__ == '__main__':
    problem = Solution()
    print(problem.countBadPairs([1, 2, 3, 4, 5]))
