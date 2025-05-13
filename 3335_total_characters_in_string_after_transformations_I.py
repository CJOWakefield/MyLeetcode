from collections import Counter
import time

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        frequencies = [0] * 26
        for char in s: frequencies[ord(char) - ord('a')] += 1
        for _ in range(t):
            freq_adjusted = [0] * 26
            for pos in range(1, 26): freq_adjusted[pos] = frequencies[pos - 1]
            freq_adjusted[0] = frequencies[25]
            freq_adjusted[1] += frequencies[25]
            frequencies = freq_adjusted
        return sum(frequencies) % mod
    
    # Found this solution post completion. Relies on Fibonacci like sequence to map the string expansion. Each cycle of 25 chars from a -> z,
    # each char doubles the number of chars in the string.
    def lengthAfterTransformations_II(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        dp = [1] * (t + 26)
        for i in range(26, len(dp)): dp[i] = (dp[i-26] + dp[i-25]) % mod

        res, counts = 0, Counter(s)
        for key, val in counts.items():
            res = (res + val * dp[(ord(key) - ord('a')) + t]) % mod
        return res
    
    
if __name__ == "__main__":
    solution = Solution()
    start_time = time.time()
    print(solution.lengthAfterTransformations(s = "abcyy", t = 2))
    print(solution.lengthAfterTransformations(s = "azbk", t = 1))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    print(solution.lengthAfterTransformations_II(s = "abcyy", t = 2))
    print(solution.lengthAfterTransformations_II(s = "azbk", t = 1))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
