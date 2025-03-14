class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2: return False
            n //= 3
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkPowersOfThree(12))
    print(sol.checkPowersOfThree(91))
    