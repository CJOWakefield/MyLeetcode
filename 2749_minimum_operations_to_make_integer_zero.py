class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(61):
            res = num1 - num2 * i
            if res >= 0 and res.bit_count() <= i <= res:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.makeTheIntegerZero(3, -2))
    print(sol.makeTheIntegerZero(5, 7))
