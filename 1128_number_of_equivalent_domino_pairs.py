from typing import List
from collections import defaultdict, Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res, seen = 0, defaultdict(int)
        for domino in dominoes:
            curr = (min(domino), max(domino))
            seen[curr] += 1
            if seen[curr] > 1: res += seen[curr] - 1
        return res
    
    def numEquivDominoPairs_II(self, dominoes: List[List[int]]) -> int:
        counts = Counter(tuple(sorted(domino)) for domino in dominoes)
        res = 0
        for val in counts.values():
            if val > 1: res += val * (val - 1) // 2
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
    print(solution.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
    print(solution.numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]))
    