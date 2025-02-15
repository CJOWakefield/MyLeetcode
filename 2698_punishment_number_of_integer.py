from functools import cache

class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def recursion(curr):
            seen = set()
            for i in range(len(curr)):
                parts = recursion(curr[i+1:]) if i != len(curr)-1 else set([0])
                for part in parts: seen.add(part + int(curr[:i+1]))
            return seen
        
        res = 0
        for i in range(1, n+1):
            if i in recursion(str(i * i)): res += i * i
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.punishmentNumber(10))
    print(problem.punishmentNumber(37))
    