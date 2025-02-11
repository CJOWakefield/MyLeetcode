class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(i, j):
            board[i][j] = '.'
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx, dy = i + di, j + dj
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'O':
                    dfs(dx, dy)

        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n-1] == 'O': dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m-1][j] == 'O': dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '.': board[i][j] = 'O'
        return board
        
if __name__ == '__main__':
    problem = Solution()
    board = problem.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])

    for row in board:
        print(row)