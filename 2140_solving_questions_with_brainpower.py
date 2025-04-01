from typing import List
from functools import cache
import time

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @cache
        def dp(pos):
            if pos >= n: return 0
            score, brainpower = questions[pos]
            return max(dp(pos+brainpower+1) + score, dp(pos+1))
        return dp(0)
    
    def mostPoints_II(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            score, brainpower = questions[i]
            solve = score + (dp[i+brainpower+1] if i+brainpower+1 <= n else 0)
            skip = dp[i+1]
            dp[i] = max(solve, skip)
        return dp[0]
    
# Notes: Caching easier to implement and simpler. II faster, utilising reverse traversal.

if __name__ == "__main__":
    sol = Solution()
    start = time.time()
    print(sol.mostPoints(questions = [[3,2],[4,3],[4,4],[2,5]]))
    print(sol.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]))
    print(sol.mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]))
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    start = time.time()
    print(sol.mostPoints_II(questions = [[3,2],[4,3],[4,4],[2,5]]))
    print(sol.mostPoints_II(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]))
    print(sol.mostPoints_II(questions = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]))
    end = time.time()
    print(f"Time taken: {end - start} seconds")