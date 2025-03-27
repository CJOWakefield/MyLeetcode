from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = sorted(val for row in grid for val in row)
        med = vals[len(vals)//2]
        res = 0
        for val in vals:
            diff = abs(val-med)
            if diff % x != 0: return -1
            res += diff / x
        return int(res)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations(grid = [[2,4],[6,8]], x = 2))
    print(sol.minOperations(grid = [[1,5],[2,3]], x = 1))
    print(sol.minOperations(grid = [[1,2],[3,4]], x = 2))
    
    