from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr, curr_max, curr_min = 0, 0, 0
        for i in range(len(differences)):
            curr += differences[i]
            curr_min, curr_max = min(curr_min, curr), max(curr_max, curr)

        shift = lower - curr_min
        curr_min += shift
        curr_max += shift
        return max(0, upper - curr_max + 1)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfArrays([1,-3,4], 1, 6))
    print(sol.numberOfArrays([3,-4,5,1,-2], -4, 5))
    print(sol.numberOfArrays([4,-7,2], 3, 6))
    print(sol.numberOfArrays([-40], -46, 53))
    print(sol.numberOfArrays([83702, -5216], -82788, 14602))