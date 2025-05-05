from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts_s, counts_t = Counter(s), Counter(t)
        for char in counts_t:
            if not counts_s[char] or not counts_s[char] == counts_t[char]: return char
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))
    print(sol.findTheDifference("a", "aa"))
    print(sol.findTheDifference("ae", "aea"))