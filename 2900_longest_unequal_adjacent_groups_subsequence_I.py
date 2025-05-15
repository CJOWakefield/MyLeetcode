from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res, curr = [words[0]], groups[0]
        for i in range(1, len(words)):
            if groups[i] != curr:
                curr = groups[i]
                res.append(words[i])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.getLongestSubsequence(["e", "a", "b"], [0, 0, 1]))
    print(sol.getLongestSubsequence(["a","b","c","d"], [1, 0, 1, 1]))