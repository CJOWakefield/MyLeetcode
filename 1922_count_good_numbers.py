class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10 ** 9) + 7
        even, odd = (n+1) // 2, n // 2
        return (pow(5, even, mod) * pow(4, odd, mod)) % mod
    
# Logic: Given pre-existing zeros possibility, for any digit position we have 5 even choice and 4 odd choices. Solution to identify, based
# on n, how many even and odd positions present. Then, use pow(x, y, mod) to calculate combinations for the odd and even positions, then
# multiply the results to obtain the final combinations (divided by mod for overflow protection)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countGoodNumbers(1))
    print(sol.countGoodNumbers(2))
    print(sol.countGoodNumbers(3))