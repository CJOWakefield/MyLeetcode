from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        def can_complete(mp, pills):
            n, pos, queue = len(workers), 0, deque()
            for i in range(n - mp, n):
                worker = workers[i]
                while pos < mp and tasks[pos] <= worker + strength:
                    queue.append(tasks[pos])
                    pos += 1
                if not queue: return False
                if queue[0] <= worker: queue.popleft()
                else:
                    if not pills: return False
                    queue.pop()
                    pills -= 1
            return True
        
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))
        while left < right:
            mp = (left + right + 1) // 2
            if can_complete(mp, pills): left = mp
            else: right = mp - 1
        return left
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTaskAssign([3, 2, 1], [0, 3, 3], 1, 1))
    print(solution.maxTaskAssign([5, 4], [0, 0, 0], 1, 5))
    print(solution.maxTaskAssign([10, 15, 30], [0, 10, 10, 10, 10], 3, 10))
        