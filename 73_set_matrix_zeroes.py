import copy

def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    base_matrix = copy.deepcopy(matrix)
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            cell = base_matrix[i][j]
            if cell == 0:
                matrix[i] = [0 for _ in range(n)]
                for q in range(m):
                    matrix[q][j] = 0

    print(matrix)

# Notes: First attempt success. Poor timing complexity however due to iteration for each cell in matrix. Next attempt: Try to only iterate based on 0 values.

# def optimal(matrix):

#     m, n = len(matrix), len(matrix[0])

#     row_zeroes = any(matrix[i][0] for i in range(n))
#     col_zeroes = any(matrix[0][j] for j in range(m))

#     for i in range(1, n):
#         for j in range (1, m):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0

#     for i in range(1, n):
#         if matrix[i][0] == 0:
#             for j in range(1, m):
#                 matrix[i][j] = 0

#     for j in range(1, m):
#         if matrix[0][j] == 0:
#             for i in range(1, n):
#                 matrix[i][j] = 0

#     if row_zeroes:
#         for j in range(m):
#             matrix[0][j] = 0

#     if col_zeroes:
#         for i in range(n):
#             matrix[i][0] = 0

#     print(matrix)

if __name__ == '__main__':
    print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    # print(optimal([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
