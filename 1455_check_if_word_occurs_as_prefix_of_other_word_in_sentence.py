class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith(searchWord): return i+1
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPrefixOfWord("i love eating burger", "burg"))
    print(sol.isPrefixOfWord("this problem is an easy problem", "pro"))
    