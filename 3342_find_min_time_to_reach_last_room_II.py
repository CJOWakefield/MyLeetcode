from heapq import heappop, heappush
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        adjs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        times = [[float('inf')] * n for _ in range(m)]
        times[0][0] = 0
        pq = [(1, 0, 0, 0)]
        while pq:
            step_cost, time, x, y = heappop(pq)
            if x == m - 1 and y == n - 1: return time
            if time == times[x][y]:
                for dx, dy in adjs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        new_time = max(time, moveTime[nx][ny]) + step_cost
                        if new_time < times[nx][ny]:
                            times[nx][ny] = new_time
                            heappush(pq, (3 - step_cost, new_time, nx, ny))
        return -1
        
if __name__ == "__main__":
    print(Solution().minTimeToReach([[0, 4], [4, 4]]))
    print(Solution().minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]]))
    print(Solution().minTimeToReach([[27, 85], [22, 53]]))
    print(Solution().minTimeToReach([[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]))
