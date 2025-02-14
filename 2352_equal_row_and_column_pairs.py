from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        seen_cols, seen_rows = defaultdict(int), defaultdict(int)
        for i in range(len(grid)):
            row, col = tuple(val for val in grid[i]), tuple(grid[j][i] for j in range(len(grid)))
            seen_rows[row] += 1
            seen_cols[col] += 1

        res = 0
        for row in seen_rows:
            if row in seen_cols: res += seen_rows[row] * seen_cols[row]
        return res 

# SMALL improvement below: uses zip(*grid) to transpose grid (e.g. columns become rows) then iterating if there is a match.

# def equalPairs(self, grid: List[List[int]]) -> int:
#     ans = 0
#     row_dict = defaultdict(int)
#     for row in grid:
#         row_dict[tuple(row)] += 1

#     for col in zip(*grid):
#         ans += row_dict[col]
#     return ans
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
    print(problem.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
    