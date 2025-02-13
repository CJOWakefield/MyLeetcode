class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if h == len(piles): return max(piles)
        left, right = 1, max(piles)
        while left < right:
            mp = (left + right) // 2
            time_taken = sum((pile + mp - 1) // mp for pile in piles)
            if time_taken <= h: right = mp
            else: left = mp + 1
        return left
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.minEatingSpeed([3,6,7,11], 8))
    print(problem.minEatingSpeed([30,11,23,4,20], 5))
    print(problem.minEatingSpeed([30,11,23,4,20], 6))
    