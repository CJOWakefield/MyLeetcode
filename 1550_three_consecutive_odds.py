from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if (arr[i] % 2, arr[i+1] % 2, arr[i+2] % 2) == (1, 1, 1): return True
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeConsecutiveOdds([2,6,4,1]))
    print(sol.threeConsecutiveOdds([1,2,34,5,7,23,8,9]))
