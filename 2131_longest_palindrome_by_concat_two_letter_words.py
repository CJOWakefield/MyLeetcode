from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)
        res, centre = 0, False
        for word, count in counts.items():
            reverse = word[::-1]
            if word == reverse:
                res += (count // 2) * 4
                if count % 2 == 1: centre = True
            elif word < reverse:
                if reverse in counts:
                    res += min(count, counts[reverse]) * 4
                    counts[reverse] = 0
        return res + (2 if centre else 0)


    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome(["lc","cl","gg"]))
    print(sol.longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
    print(sol.longestPalindrome(["cc","ll","xx"]))
    print(sol.longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
    print(sol.longestPalindrome(["em","pe","mp","ee","pp","me","ep","em","em","me"]))