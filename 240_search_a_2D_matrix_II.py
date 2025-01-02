def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix)-1, len(matrix[0])-1
    row, col = m, 0
    while 0 <= row and col <= n:
        curr = matrix[row][col]
        if curr > target: row -= 1
        elif curr < target: col += 1
        else: return True
    return False

# Note: Initial attempt to use binary search with the mp of row and col, but small bugs. Want to revist as think possible and lower time complexity O(log(n))

if __name__ == '__main__':
    print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
