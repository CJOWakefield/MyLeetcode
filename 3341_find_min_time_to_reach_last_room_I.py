from collections import deque
from typing import List
from heapq import heappush, heappop
import time

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        res = float('inf')
        m, n = len(moveTime), len(moveTime[0])
        adjs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        to_search = deque([(0, 0, 0)])
        visited = {(0, 0): 0}
        while to_search:
            x, y, time = to_search.popleft()
            if x == m - 1 and y == n - 1: res = min(res, time)
            for dx, dy in adjs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_time = max(time, moveTime[nx][ny]) + 1
                    if (nx, ny) not in visited or new_time < visited[(nx, ny)]:
                        visited[(nx, ny)] = new_time
                        to_search.append((nx, ny, new_time))
        return res if res != float('inf') else -1

    def minTimeToReachDijkstra(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        adjs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        times = [[float('inf')] * n for _ in range(m)]
        times[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            time, x, y = heappop(pq)
            if x == m - 1 and y == n - 1: return time
            if time == times[x][y]:
                for dx, dy in adjs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        new_time = max(time, moveTime[nx][ny]) + 1
                        if new_time < times[nx][ny]:
                            times[nx][ny] = new_time
                            heappush(pq, (new_time, nx, ny))
        return -1

if __name__ == "__main__":
    start_time = time.time()
    print(Solution().minTimeToReach([[0, 4], [4, 4]]))
    print(Solution().minTimeToReach([[0, 0, 0], [0, 0, 0]]))
    print(Solution().minTimeToReach([[27, 85], [22, 53]]))
    print(Solution().minTimeToReach([[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time.time()
    print(Solution().minTimeToReachDijkstra([[0, 4], [4, 4]]))
    print(Solution().minTimeToReachDijkstra([[0, 0, 0], [0, 0, 0]]))
    print(Solution().minTimeToReachDijkstra([[27, 85], [22, 53]]))
    print(Solution().minTimeToReachDijkstra([[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
