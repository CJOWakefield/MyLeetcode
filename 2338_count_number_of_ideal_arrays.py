class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        max_val = 10000
        
        base_counts = [[i + 1 for i in range(max_val)]]
        prev, next = [1] * max_val, [0] * max_val
        prev_val = 1
        
        while (prev_val << 1) <= max_val:
            next_val = prev_val << 1
            next[next_val-1:] = [0] * (max_val - next_val + 1)
            for prev_num in range(prev_val, max_val + 1):
                prev_count = prev[prev_num - 1]
                max_mult = max_val // prev_num
                for mult in range(2, max_mult + 1):
                    next[prev_num * mult - 1] = (next[prev_num * mult - 1] + prev_count) % mod
            current = [next[next_val - 1]]
            for next_num in range(next_val, max_val):
                current.append((current[-1] + next[next_num]) % mod)
            base_counts.append(current)
            prev, next = next, prev
            prev_val = next_val
            
        count, combo, n_choose_k, k = 0, 1, n-1, 1
        for base in (1 << i for i in range(min(n, len(base_counts)))):
            if base <= maxValue:
                count = (count + combo * base_counts[k-1][maxValue - base]) % mod
            else:
                break
            combo = combo * n_choose_k // k
            n_choose_k -= 1
            k += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.idealArrays(2, 5))
    print(solution.idealArrays(5, 3))

