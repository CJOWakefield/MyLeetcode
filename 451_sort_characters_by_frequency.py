from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        return ''.join(char * count for char, count in counts)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))
    print(sol.frequencySort("cccaaa"))
    print(sol.frequencySort("Aabb"))
