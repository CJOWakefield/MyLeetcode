from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        to_search = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    to_search.append((i, j))
                    res[i][j] = 0

        while to_search:
            i, j = to_search.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and res[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    to_search.append((x, y))
            
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
    
    
