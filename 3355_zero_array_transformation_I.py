from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        if len(queries) < max(nums): return False
        diff = [0] * (len(nums)+1)
        for query in queries: 
            diff[query[0]] += 1
            diff[query[1]+1] -= 1
        for i in range(len(nums)):
            if i > 0: diff[i] += diff[i-1]
            if nums[i] > diff[i]: return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isZeroArray([1,0,1], [[0,2]]))
    print(sol.isZeroArray([4,3,2,1], [[0,2],[1,3]]))
    print(sol.isZeroArray([1,2,3,4,5], [[0,2],[1,3],[2,4],[3,4]]))
    print(sol.isZeroArray([1,2,3,4,5], [[0,2],[1,3],[2,4],[3,4],[4,4]]))