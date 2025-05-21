import copy
import time

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # First attempt.
        base_matrix = copy.deepcopy(matrix)
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                cell = base_matrix[i][j]
                if cell == 0:
                    matrix[i] = [0 for _ in range(n)]
                    for q in range(m):
                        matrix[q][j] = 0

    def setZeroes_II(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        to_change = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: to_change.add((i, j))
        
        for i, j in to_change:
            matrix[i] = [0] * n
            for row in matrix:
                row[j] = 0


# Notes: First attempt success. Poor timing complexity however due to iteration for each cell in matrix. Next attempt: Try to only iterate based on 0 values.

if __name__ == '__main__':
    sol = Solution()
    start = time.time()
    print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    end = time.time()
    print(f"Time taken: {end - start} seconds")
    start = time.time()
    print(sol.setZeroes_II([[1,1,1],[1,0,1],[1,1,1]]))
    print(sol.setZeroes_II([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    end = time.time()
    print(f"Time taken: {end - start} seconds")
