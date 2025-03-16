from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def valid(time):
            total = 0
            for rank in ranks:
                repairs = int((time / rank) ** 0.5)
                total += repairs
                if total >= cars: return True
            return False

        left, right = 1, min(ranks) *cars ** 2
        while left < right:
            mp = (left + right) // 2
            if valid(mp): right = mp
            else: left = mp + 1
        return left
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.repairCars([4,2,3,1], 10))
    print(solution.repairCars([5,1,8], 6))
    print(solution.repairCars([1,2,3], 10))
    print(solution.repairCars([1,2,3], 1))
    print(solution.repairCars([1,2,3], 2))
    print(solution.repairCars([5, 5, 2], 2))