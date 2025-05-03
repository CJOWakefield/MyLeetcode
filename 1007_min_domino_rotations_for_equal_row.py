from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(val):
            rotations_top, rotations_bottom = 0, 0
            for i in range(len(tops)):
                if tops[i] != val and bottoms[i] != val: return float('inf')
                if tops[i] != val: rotations_top += 1
                if bottoms[i] != val: rotations_bottom += 1
            return min(rotations_top, rotations_bottom)
        
        min_rotations = min(check(tops[0]), check(bottoms[0]))
        return min_rotations if min_rotations != float('inf') else -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
    print(solution.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
                