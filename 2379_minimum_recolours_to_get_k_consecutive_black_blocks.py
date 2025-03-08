class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        res = whites
        for i in range(len(blocks)-k):
            whites += (blocks[k+i] == 'W') - (blocks[i] == 'W')
            res = min(res, whites)
        return res
    
# Notes: Fan of the logic on line 6. Originally took several more lines, much more concise here. Remember to use
# boolean logic in summation (especially for sliding window).

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumRecolors("WBBWWBBWBW", 7))
    print(sol.minimumRecolors("WBWBBBW", 2))
    print(sol.minimumRecolors("BWWWBB", 6))