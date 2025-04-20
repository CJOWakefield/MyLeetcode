from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        res = 0
        for k, v in counts.items():
            res += (k + v) // (k + 1) * (k + 1)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numRabbits([1,1,2]))
    print(sol.numRabbits([10,10,10]))