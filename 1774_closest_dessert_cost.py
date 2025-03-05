from functools import lru_cache
from time import time

class Solution:

    # Attempt 1: Backtracking. Time limit exceeded.

    def closestCost(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        counts = {i: 2 for i in range(len(toppingCosts))}
        res = baseCosts[0]

        def backtrack(counts, total):
            nonlocal res
            if abs(target - total) < abs(target - res) or (abs(target - total) == abs(target - res) and total < res):
                res = total
            if target - total == 0 or total > target + abs(target - res): return
            for i in range(len(toppingCosts)):
                if counts[i] > 0:
                    counts[i] -= 1
                    backtrack(counts, total + toppingCosts[i])
                    counts[i] += 1

        for cost in baseCosts:
            backtrack(counts, cost)
        return res 
    
    # Attempt 2: DP.

    def closestCost_II(self, baseCosts: list[int], toppingCosts: list[int], target: int) -> int:
        @lru_cache(None)
        def dp(pos, cost):
            if pos == len(toppingCosts) or cost > target: return cost
            curr_cost = toppingCosts[pos]
            res = dp(pos+1, cost), dp(pos+1, cost+curr_cost), dp(pos+1, cost+(2*curr_cost))
            return min(res, key=lambda x: (abs(x - target), x))
        
        res = [dp(0, cost) for cost in baseCosts]
        return min(res, key=lambda x: (abs(x - target), x))
        

if __name__ == "__main__":
    problem = Solution()
    start_time = time()
    print(problem.closestCost([1,7], [3,4], 10))
    print(problem.closestCost([2,3], [4,5,100], 18))
    print(problem.closestCost([1,2,3,4,5], [1,2,3,4,5], 10))
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time()
    print(problem.closestCost_II([1,7], [3,4], 10))
    print(problem.closestCost_II([2,3], [4,5,100], 18))
    print(problem.closestCost_II([1,2,3,4,5], [1,2,3,4,5], 10))
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
