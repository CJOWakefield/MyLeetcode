from collections import Counter
from functools import lru_cache
from math import comb
import time

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        base_counts = Counter(num)
        res = 0

        def max_sum(counts):
            return sum(int(digit) * count for digit, count in counts.items())

        def dfs(curr, odd, even, rem_counts, rem_total):
            nonlocal res
            if len(curr) == len(num):
                if odd == even: res += 1
                return
            
            diff = abs(odd - even)
            if diff > rem_total or (rem_total - diff) % 2 != 0: return

            for char in rem_counts:
                if rem_counts[char] == 0: continue
                rem_counts[char] -= 1
                if len(curr) % 2 == 0: dfs(curr + char, odd + int(char), even, rem_counts, rem_total - int(char))
                else: dfs(curr + char, odd, even + int(char), rem_counts, rem_total - int(char))
                rem_counts[char] += 1

        total = max_sum(base_counts)
        if total % 2 != 0: return 0
        dfs('', 0, 0, base_counts, total)
        return res % (10 ** 9 + 7)

    # First solution valid but time complexity too high. Found solution online, utilising memoization & combinatorial multiplication to exit early permutations that cannot be valid.
    # Time complexity O(N x 10 x N^2). Space complexity the same. Much improved vs O(N!) for previous solution, which fails for larger num lengths.
    def countBalancedPermutations_II(self, num: str) -> int:

        @lru_cache(maxsize=8000)
        def dp(odd_digits, even_digits, odd_sum, digit, res=0):

            if digit > 9: return (odd_sum, odd_digits) == (target_sum, odd_positions)
            
            for odd_add in range(digit_counts[digit] + 1):
                even_add = digit_counts[digit] - odd_add
                if (digit * odd_add + odd_sum > target_sum or
                    odd_digits + odd_add > odd_positions or
                    even_digits + even_add > even_positions): continue
                
                res += (dp(odd_digits + odd_add,
                          even_digits + even_add,
                          odd_sum + digit * odd_add,
                          digit + 1) % mod *

                       comb(odd_positions - odd_digits, odd_add) % mod *
                       comb(even_positions - even_digits, even_add) % mod)
            
            return res % mod

        digit_counts, mod = [0] * 10, 10**9 + 7
        for char in num: digit_counts[int(char)] += 1
        total_sum = sum(int(char) * count for char, count in enumerate(digit_counts))
        if total_sum % 2: return 0
        odd_positions, even_positions, target_sum = len(num) // 2, (len(num) + 1) // 2, total_sum // 2

        return dp(0, 0, 0, 0)

if __name__ == "__main__":
    start = time.time()
    print(Solution().countBalancedPermutations("123"))
    print(Solution().countBalancedPermutations("112"))
    print(Solution().countBalancedPermutations("12345"))
    print(Solution().countBalancedPermutations("2231606925"))
    print(Solution().countBalancedPermutations("1890666349"))
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    start = time.time()
    print(Solution().countBalancedPermutations_II("123"))
    print(Solution().countBalancedPermutations_II("112"))
    print(Solution().countBalancedPermutations_II("12345"))
    print(Solution().countBalancedPermutations_II("2231606925"))
    print(Solution().countBalancedPermutations_II("1890666349"))
    end = time.time()
    print(f"Time taken: {end - start} seconds")