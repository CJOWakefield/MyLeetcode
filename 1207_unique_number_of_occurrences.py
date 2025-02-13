from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        seen = set()
        for k, v in counts.items():
            if v in seen: return False
            seen.add(v)
        return True

if __name__ == '__main__':
    problem = Solution()
    print(problem.uniqueOccurrences([1,2,2,1,1,3]))
    print(problem.uniqueOccurrences([1,2]))
    print(problem.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
    
    