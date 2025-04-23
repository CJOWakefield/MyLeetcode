from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n <= 9: return n
        seen, counts = defaultdict(int), defaultdict(int)
        for i in range(1, n+1):
            curr, val = 0, str(i)
            for char in val: curr += int(char)
            seen[curr] += 1
            counts[seen[curr]] += 1
        return counts[max(counts.keys())]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countLargestGroup(13))
    print(sol.countLargestGroup(2))
    print(sol.countLargestGroup(15))
    print(sol.countLargestGroup(24))