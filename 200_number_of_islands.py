from collections import deque

class Solution:
    def numIslands(self, grid:  list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        res = 0

        def bfs(i, j):
            seen.add((i, j))
            to_search = deque([(i, j)])
            while to_search:
                i, j = to_search.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx, dy = i + di, j + dj
                    if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == '1' and (dx, dy) not in seen:
                        to_search.append((dx, dy))
                        seen.add((dx, dy))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    res += 1
                    bfs(i, j)

        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print(problem.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))