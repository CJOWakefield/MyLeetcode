from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def dp(pos, curr, counts):
            if pos == 3: return [curr] if curr % 2 == 0 else []
            results = []
            for d in counts:
                if counts[d] > 0:
                    counts[d] -= 1
                    results.extend(dp(pos + 1, curr * 10 + d, counts))
                    counts[d] += 1
            return results

        return sorted(set(num for d in digits if d != 0 
                         for counts in [Counter(digits)]
                         for counts[d] in [counts[d] - 1]
                         for num in dp(1, d, counts)))
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findEvenNumbers([2,1,3,0]))
    print(sol.findEvenNumbers([2,2,8,8,2]))
    print(sol.findEvenNumbers([3,7,5]))