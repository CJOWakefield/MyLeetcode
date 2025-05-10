from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set('qwertyuiopQWERTYUIOP')
        second = set('asdfghjklASDFGHJKL')
        third = set('zxcvbnmZXCVBNM')
        
        return [word for word in words if all(c in (
            first if word[0] in first else
            second if word[0] in second else
            third
        ) for c in word)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findWords(words = ["Hello","Alaska","Dad","Peace"]))
    print(sol.findWords(words = ["omk"]))
    print(sol.findWords(words = ["adsdf","sfd"]))