from collections import deque

def findMaxFish(grid: list[list[int]]) -> int:
    m, n, res = len(grid), len(grid[0]), 0
    seen = set()
    for i in range(m):
        for j in range(n):
            if (i, j) in seen or grid[i][j] == 0: continue
            curr, to_search = 0, deque([(i, j)])
            seen.add((i, j))
            while to_search:
                x, y = to_search.popleft()
                curr += grid[x][y]
                if curr > res: res = curr
                for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dx, dy = x + adj[0], y + adj[1]
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in seen:
                        if grid[dx][dy] > 0: to_search.append((dx, dy))
                        seen.add((dx, dy))
    return res

if __name__ == '__main__':
    print(findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
