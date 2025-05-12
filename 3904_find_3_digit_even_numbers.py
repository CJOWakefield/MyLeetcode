from typing import List
from collections import Counter
import time

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

    def findEvenNumbers_brute(self, digits: List[int]) -> List[int]:
        counts = Counter(list(map(str, digits)))
        res = []
        for i in range(100, 1000, 2):
            curr_counts = Counter(str(i))
            if all(curr_counts[d] <= counts[d] for d in curr_counts):
                res.append(i)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    start = time.time()
    print(sol.findEvenNumbers([2,1,3,0]))
    print(sol.findEvenNumbers([2,2,8,8,2]))
    print(sol.findEvenNumbers([3,7,5]))
    end = time.time()
    print(f"Time taken: {end - start} seconds")

    start = time.time()
    print(sol.findEvenNumbers_brute([2,1,3,0]))
    print(sol.findEvenNumbers_brute([2,2,8,8,2]))
    print(sol.findEvenNumbers_brute([3,7,5]))
    end = time.time()
    print(f"Time taken: {end - start} seconds")