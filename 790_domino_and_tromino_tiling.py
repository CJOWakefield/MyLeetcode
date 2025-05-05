class Solution:
    def numTilings(self, n: int) -> int:
        mod = (10 ** 9) + 7
        arrangements = {1:1, 2:2, 3:5}
        for i in range(4, n+1): arrangements[i] = ((arrangements[i-1] * 2) + arrangements[i-3]) % mod
        return arrangements[n]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numTilings(3))
    print(sol.numTilings(1))
    print(sol.numTilings(2))
    print(sol.numTilings(4))
    print(sol.numTilings(5))
    print(sol.numTilings(6))