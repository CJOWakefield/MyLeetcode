class Solution:
    def sumZero(self, n: int) -> list[int]:
        vals = list(range(1, n//2 + 1)) + list(range(-1, -n//2 - 1, -1))
        return vals[:-1] + [0] if n % 2 else vals

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumZero(5))
    print(sol.sumZero(4))
    print(sol.sumZero(3))
    print(sol.sumZero(1))
