def largestIsland(grid: list[list[int]]) -> int:
    n = len(grid)
    islands = {}

    def dfs(x, y, id):
        grid[x][y] = id
        island_size = 1
        for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = x + adj[0], y + adj[1]
            if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 1:
                island_size += dfs(dx, dy, id)
        return island_size

    curr_id = 2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                size = dfs(i, j, curr_id)
                islands[curr_id] = size
                curr_id += 1

    if not islands.values(): return 1
    res = max(islands.values())
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                neighbours = set()
                for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    di, dj = i + adj[0], j + adj[1]
                    if 0 <= di < n and 0 <= dj < n and grid[di][dj] != 0:
                        neighbours.add(grid[di][dj])

                if len(neighbours) > 0:
                    new_size = sum(islands[neighbour] for neighbour in neighbours) + 1
                    if new_size > res: res = new_size

    return res

if __name__ == '__main__':
    print(largestIsland(grid = [[1,0],[0,1]]))
