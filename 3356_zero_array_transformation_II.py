from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        m, n = len(nums), len(queries)
        diffs = [0] * (m + 1)
        queries.reverse()

        curr = 0
        for i, num in enumerate(nums):
            curr += diffs[i]
            while queries and curr < num:
                left, right, val = queries.pop()
                if i <= right:
                    if i >= left: curr += val
                    else: diffs[left] += val
                    diffs[right+1] -= val
            if curr < num: return -1
        
        return n - len(queries)
    
# Notes: Intuition found online, had no idea how to approach this one. Idea to start diff array at 0, then build and try to reach/exceed the
# initial array. Cumulative sum maintained to track the highest current value achievable with the curr removed queries. If we cannot reach a value,
# we must pop another query. If queries is empty and value still not reached, solution not possible.
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))
    print(sol.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))
    
    