from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        m, n = len(nums), len(queries)
        workload = [0] * (m + 1)

        queries.sort()
        available = []
        q_pos = 0

        for time in range(m):
            if time > 0: workload[time] += workload[time - 1]
            while q_pos < n and queries[q_pos][0] == time:
                heapq.heappush(available, -queries[q_pos][1])
                q_pos += 1

            while workload[time] < nums[time]:
                if not available or -available[0] < time:
                    return -1
                workload[time] += 1
                end_time = -heapq.heappop(available)
                if end_time + 1 < len(workload):
                    workload[end_time + 1] -= 1

        return len(available)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxRemoval(nums = [2,0,2], queries = [[0,2],[1,1],[0,2]]))   