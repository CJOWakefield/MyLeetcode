import copy

def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    new_board = copy.deepcopy(board)
    m, n = len(board), len(board[0])
    adj_matrix = [(row, col) for row in (-1,0,1) for col in (-1,0,1) if not (row == col == 0)]

    # Row i, col j
    for row in range(m):
        for col in range(n):
            cell = new_board[row][col]
            # Identify neighbouring co-ordinates based on adj_matrix
            adj_cells_rel = [neighbour for neighbour in adj_matrix if 0 <= neighbour[0]+row < m and 0 <= neighbour[1]+col < n]
            adj_cells_coords = [(neigh[0]+row, neigh[1]+col) for neigh in adj_cells_rel]
            alive_neighbours = [new_board[neigh[0]][neigh[1]] for neigh in adj_cells_coords]
            alive_tally = sum(alive_neighbours)
            # print(f'row: {row}, col: {col} --- neighbours: {adj_cells_coords} --- alive neighbours: {alive_neighbours} --- alive tally: {alive_tally}')

            # Alive or dead cases applied
            if cell == 0 and alive_tally == 3:
                board[row][col] = 1
            elif cell == 1:
                if alive_tally < 2 or alive_tally > 3:
                    board[row][col] = 0
            else:
                board[row][col] = cell

            print(f'Cell ({row}, {col}) converted from {cell} to {board[row][col]}')
            print(board)
            print(new_board)

# Notes: completed more or less at first time of trying, no solution required. Long time taken due to small errors (e.g. applying live transformation for >= 3 neighbours, not >)

if __name__ == '__main__':
    print(gameOfLife([[0,1,0],
                      [0,0,1],
                      [1,1,1],
                      [0,0,0]]))
