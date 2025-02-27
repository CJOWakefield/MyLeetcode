class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        res, n = 0, len(arr)
        dp = [[2] * n for _ in range(n)]
        vals = {val: pos for pos, val in enumerate(arr)}

        for i in range(n):
            for j in range(i):
                prev = arr[i] - arr[j]
                if prev >= arr[j]: continue
                if prev in vals:
                    pos = vals[prev]
                    dp[i][j] = dp[j][pos] + 1
                    res = max(res, dp[i][j])
                # print(f'\n{dp}')

        return res if res > 2 else 0
    
# Intuition:
# 1. DP array to store the length of the longest fibonacci sequence ending with arr[i] and arr[j].
# 2. Iterate through array, for each pair (i, j). Identify if previous fibonacci number exists in the array.
# 3. If it exists, extend sequence by 1 and update dp[i][j].
# 4. Track maximum sequence length as dp updated. Return if value larger than 2 (fib must be minimum 3 numbers by default)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
    # print(sol.lenLongestFibSubseq([1,3,5]))
    # print(sol.lenLongestFibSubseq([2,4,7,8,9,10,14,15,18,23,32,50]))
    # print(sol.lenLongestFibSubseq([1,3,7,11,12,14,18]))
    # print(sol.lenLongestFibSubseq([1,2,3,4,5,6,7,8,9,10]))
    # print(sol.lenLongestFibSubseq([1,2,3,4,5,6,7,8,9,10]))
