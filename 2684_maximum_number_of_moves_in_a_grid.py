from functools import cache

class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dp(i, j):
            res = 0
            for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[i][j] < grid[x][y]:
                    res = max(res, 1 + dp(x, y))
            return res
        
        return max(dp(i, 0) for i in range(m))
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
    print(sol.maxMoves([[3,2,4],[2,1,9],[1,1,7]]))