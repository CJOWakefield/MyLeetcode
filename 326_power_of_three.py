class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        if n == 0: return False
        return (n % 3 == 0) and self.isPowerOfThree(n // 3)
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.isPowerOfThree(27))
    print(problem.isPowerOfThree(0))
    print(problem.isPowerOfThree(9))