def countUnguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in guards: grid[y][x] = 3
    for x, y in walls: grid[y][x] = 2
    adjs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for x_0, y_0 in guards:
        for dx, dy in adjs:
            x, y = x_0, y_0
            while True:
                x += dx
                y += dy
                if x < 0 or x >= m or y < 0 or y >= n or grid[y][x] == 2 or grid[y][x] == 3:
                    break
                grid[y][x] = 1

    return grid

if __name__ == '__main__':
    print(countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))
