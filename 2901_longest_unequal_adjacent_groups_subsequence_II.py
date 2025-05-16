from typing import List
from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        connections = defaultdict(list)
        
        for i in range(n):
            for j in range(i, n):
                if (groups[i] != groups[j] and 
                    len(words[i]) == len(words[j]) and 
                    sum(a != b for a, b in zip(words[i], words[j])) == 1):
                    connections[i].append(j)
        
        res, max_vals = [], {}        
        for i in range(n - 1, -1, -1):
            max_vals[i] = max((max_vals.get(j, []) for j in connections[i]), key=len, default=[])
            max_vals[i] = [words[i]] + max_vals[i]
            if len(max_vals[i]) > len(res):
                res = max_vals[i]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.getWordsInLongestSubsequence(["bab","dab","cab"], [1, 2, 2]))
    print(sol.getWordsInLongestSubsequence(["a","b","c","d","e"], [0, 1, 0, 1, 0]))