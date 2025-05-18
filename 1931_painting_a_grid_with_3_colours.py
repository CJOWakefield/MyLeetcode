from collections import defaultdict
from functools import cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def ternary(num, length):
            if num == 0: return [0] * length
            digits = []
            while num: num, remainder = divmod(num, 3); digits.append(remainder)
            return digits + [0] * (length - len(digits))

        dp, valid_states = defaultdict(int), defaultdict(list)
        
        for state in range(3**m):
            colors = ternary(state, m)
            if all(colors[i] != colors[i + 1] for i in range(len(colors) - 1)):
                dp[state] = 1
                
        for state in dp:
            current_colors = ternary(state, m)
            for next_state in dp:
                next_colors = ternary(next_state, m)
                if all(curr != next for curr, next in zip(current_colors, next_colors)):
                    valid_states[state].append(next_state)
                    
        for _ in range(n - 1):
            new_dp = defaultdict(int)
            for current_state in valid_states:
                for next_state in valid_states[current_state]:
                    new_dp[current_state] = (new_dp[current_state] + dp[next_state]) % mod
            dp = new_dp
            
        return sum(dp.values()) % mod
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.colorTheGrid(1, 1))
    print(sol.colorTheGrid(1, 2))
    print(sol.colorTheGrid(2, 1))
    print(sol.colorTheGrid(2, 2))
    print(sol.colorTheGrid(3, 1))
    print(sol.colorTheGrid(3, 2))
    print(sol.colorTheGrid(5, 5))