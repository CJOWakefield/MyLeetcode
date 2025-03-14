from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, sum(candies)//k
        res = 0
        while left <= right:
            mp = (left + right) // 2
            curr = sum(val//mp for val in candies)
            if curr >= k:
                res = mp
                left = mp + 1
            else: right = mp - 1
        return res
    
# Notes: Original start points left, right = 0, len(candies). Changed to 1, sum(candies)//k since 0 candies impossible. Sum(candies)//k
# since the max possible is the total candies divided evenly between the k target children.
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumCandies(candies = [5,8,6], k = 3))
    print(sol.maximumCandies(candies = [2,5,7,9,3,1,10,6,4,8], k = 5))
    print(sol.maximumCandies(candies = [1,2,3,4,10], k = 5))
    
    