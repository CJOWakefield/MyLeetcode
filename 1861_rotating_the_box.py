from time import time

class Solution:

    # First attempt, two pass. Utilising zip(*grid) method to transpose and then execute falling logic.
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        for row in boxGrid:
            for i in range(len(row)-1):
                if row[i] == '#':
                    pos = i+1   
                    empty = -1
                    while pos < len(row):
                        if row[pos] == '.': empty = pos
                        elif row[pos] == '*': break
                        pos += 1
                    if empty != -1: row[i], row[empty] = row[empty], row[i]

        return [list(row)[::-1] for row in zip(*boxGrid)]
    
    # Second attempt in one pass, inspired by another solution. Replacement grid altered as first grid logic is determined.
    def rotateTheBox_II(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        res = [['.'] * m for _ in range(n)]

        for i in range(m):
            new_row, empty_pos = m-i-1, n-1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '#':
                    res[empty_pos][new_row] = '#'
                    empty_pos -= 1
                elif boxGrid[i][j] == '*':
                    res[j][new_row] = '*'
                    empty_pos = j - 1
                    
        return res
    
if __name__ == "__main__":
    problem = Solution()
    start_time = time()
    print(problem.rotateTheBox([["#",".","#"]]))
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
    start_time = time()
    print(problem.rotateTheBox_II([["#",".","#"]]))
    end_time = time()
    print(f"Time taken: {end_time - start_time} seconds")
