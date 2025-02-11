class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        seen = set()

        def dfs(i, j, k):
            if k == len(word): return True
            if not (0 <= i < m) or not (0 <= j < n): return False
            if (i, j) in seen or board[i][j] != word[k]: return False

            seen.add((i, j))
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            seen.remove((i, j))
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(problem.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
