class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, (n+1)//2
        res = 0
        while left <= right:
            mp = (left + right) // 2
            coins_needed = (mp / 2) * (mp + 1)
            if coins_needed <= n: 
                res = max(res, mp)
                left = mp +1
            else: right = mp - 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.arrangeCoins(5))
    print(sol.arrangeCoins(8))
    print(sol.arrangeCoins(1))
    print(sol.arrangeCoins(2))
    print(sol.arrangeCoins(3))