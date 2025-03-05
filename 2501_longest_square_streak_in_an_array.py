from collections import Counter

class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        counts = Counter(nums)
        res = 0

        for num in nums:
            curr_seq, curr = [num], num ** 2
            while curr in counts and curr != 1:
                curr_seq.append(curr)
                curr *= curr
            res = max(res, len(curr_seq))
        return res if res > 1 else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSquareStreak([4,3,6,16,8,2]))
    print(sol.longestSquareStreak([2,3,5,6,7]))
    print(sol.longestSquareStreak([1,1]))
    
    