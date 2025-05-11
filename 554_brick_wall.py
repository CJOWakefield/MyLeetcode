from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        pos = defaultdict(int)
        for row in wall:
            curr = 0
            for i in range(len(row)-1):
                curr += row[i]
                pos[curr] += 1
        return len(wall) - (max(pos.values()) if pos else 0)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
    print(sol.leastBricks([[1],[1],[1]]))