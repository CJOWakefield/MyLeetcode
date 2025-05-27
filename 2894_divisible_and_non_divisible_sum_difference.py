class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i % m == 0: res -= i
            else: res += i
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.differenceOfSums(10, 3))
    print(sol.differenceOfSums(5, 6))