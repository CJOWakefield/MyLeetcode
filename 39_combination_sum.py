class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(vals, total, pos):
            rem = target - total
            if rem <= 0:
                if rem == 0: res.append(vals[:])
                return
            for i in range(pos, len(candidates)):
                vals.append(candidates[i])
                backtrack(vals, total + candidates[i], i)
                vals.pop()

        backtrack([], 0, 0)
        return res
    
# Notes: Straightforward backtracking, need to recognise BT pattern more. Initial attempt to loop through candidates, building
# dictionary of factors for any value. Plan to then iterate through resulting dict and subtracting, calculating the number of combinations
# for each value to reach target. This would be O(n^2) and would require a lot of memory.
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    print(sol.combinationSum([2,3,5], 8))
    