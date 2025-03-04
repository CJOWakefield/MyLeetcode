class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str, digits = str(num), list(str(num))
        seen = {digit: i for i, digit in enumerate(digits)}
        for i, digit in enumerate(digits):
            for j in range(9, int(digit), -1):
                if str(j) in seen and seen[str(j)] > i:
                    digits[i], digits[seen[str(j)]] = digits[seen[str(j)]], digits[i]
                    return int(''.join(digits))
        return num
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSwap(2736))
    print(sol.maximumSwap(9973))
    