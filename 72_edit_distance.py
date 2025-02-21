from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        c1, c2 = len(word1), len(word2)
        
        @lru_cache(None)
        def search(i, j):
            # if (i, j) in seen: return
            if i == c1: return c2 - j
            if j == c2: return c1 - i
            if word1[i] == word2[j]: return search(i+1, j+1)

            return min(search(i, j+1),
                       search(i+1, j),
                       search(i+1, j+1)) + 1

        return search(0, 0)
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.minDistance("horse", "ros"))
    print(problem.minDistance("intention", "execution"))
    
    
