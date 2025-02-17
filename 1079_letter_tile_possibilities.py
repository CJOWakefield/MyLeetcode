from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(counter):
            combinations = 0
            for key, value in counter.items():
                if value == 0: continue
                combinations += 1
                counter[key] -= 1
                combinations += dfs(counter)
                counter[key] += 1
            return combinations
        
        counter = Counter(tiles)
        return dfs(counter)
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.numTilePossibilities("AAB"))
    print(problem.numTilePossibilities("AAABBC"))
    print(problem.numTilePossibilities("V"))