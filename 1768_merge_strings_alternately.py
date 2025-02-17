class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        fin = min(len(word1), len(word2))
        for i in range(fin): res += word1[i] + word2[i]
        if len(word1) != len(word2):
            if len(word1) > len(word2): res = res + word1[fin:]
            else: res = res + word2[fin:]
        return res  
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.mergeAlternately("abc", "pqr"))
    print(problem.mergeAlternately("ab", "pqrs"))
    print(problem.mergeAlternately("abcd", "pq"))