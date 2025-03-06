from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        res = []
        for row in grid: res.extend(row)
        
        missed = list(set(list(range(1, len(res)+1))) - set(res))[0]
        duplicate = [k for k,v in Counter(res).items() if v > 1][0]
        return [int(duplicate), int(missed)]
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.findMissingAndRepeatedValues([[1,2,2,4],[4,3,3,3],[5,6,7,8]]))
    