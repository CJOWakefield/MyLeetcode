class Solution:
    def coloredCells(self, n: int) -> int:
        return (n**2) + (n-1)**2
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coloredCells(1))
    print(sol.coloredCells(2))
    