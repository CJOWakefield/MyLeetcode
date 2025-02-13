class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies: res[i] = True
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.kidsWithCandies([2,3,5,1,3], 3))
    print(problem.kidsWithCandies([4,2,1,1,2], 1))
    print(problem.kidsWithCandies([12,1,12], 10))