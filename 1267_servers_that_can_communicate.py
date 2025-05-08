from collections import defaultdict
from typing import List
import time

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, columns = defaultdict(int), defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    columns[j] += 1
                
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rows[i] > 1 or columns[j] > 1: res += 1
        return res

    # Found an improved time complexity solution and implemented by self. 
    def countServers_II(self, grid: List[List[int]]) -> int:
        m, res = len(grid), 0
        for row in range(m):
            row_sum = sum(grid[row])
            if row_sum > 1: res += row_sum
            elif row_sum == 1:
                column = grid[row].index(1)
                if sum(grid[row][column] for row in range(m)) > 1: res += 1
        return res
    
if __name__ == "__main__":
    start_time = time.time()
    print(Solution().countServers([[1, 0], [0, 1]]))
    print(Solution().countServers([[1, 0], [1, 1]]))
    print(Solution().countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time.time()
    print(Solution().countServers_II([[1, 0], [0, 1]]))
    print(Solution().countServers_II([[1, 0], [1, 1]]))
    print(Solution().countServers_II([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    
    