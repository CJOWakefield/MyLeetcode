class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

if __name__ == '__main__':
    problem = Solution()
    print(problem.canWinNim(4))
    print(problem.canWinNim(1))
    print(problem.canWinNim(2))
    