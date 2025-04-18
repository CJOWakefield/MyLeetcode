from collections import Counter, defaultdict
from typing import List
import math
import time

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res, curr = 0, 0
        while any(counts[val] > 1 for val in counts) and curr < len(nums):
            for i in range(curr, curr+3): 
                if i < len(nums): 
                    counts[nums[i]] -= 1
                    curr += 1
            res += 1
        return res
    
    def minimumOperations_II(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for i in range(len(nums)-1, -1, -1):
            counts[nums[i]] += 1
            if counts[nums[i]] == 2: return math.ceil((i+1)/3)
        return 0
    
if __name__ == "__main__":
    sol = Solution()
    start_time = time.time()
    print(sol.minimumOperations([1,2,3,4,2,3,3,5,7]))
    print(sol.minimumOperations([4,5,6,4,4]))
    print(sol.minimumOperations([6,7,8,9]))
    print(sol.minimumOperations([15,3,5,5]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time.time()
    print("--------------------------------")
    start_time = time.time()
    print(sol.minimumOperations_II([1,2,3,4,2,3,3,5,7]))
    print(sol.minimumOperations_II([4,5,6,4,4]))
    print(sol.minimumOperations_II([6,7,8,9]))
    print(sol.minimumOperations_II([15,3,5,5]))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
