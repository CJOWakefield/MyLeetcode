def minCost(startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        [y0, y1], [x0, x1] = sorted([startPos[0], homePos[0]]), sorted([startPos[1], homePos[1]])
        row_cost = sum(rowCosts[y0:y1+1]) - rowCosts[startPos[0]]
        col_cost = sum(colCosts[x0:x1+1]) - colCosts[startPos[1]]
        return row_cost + col_cost


if __name__ == '__main__':
    print(minCost(startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]))
