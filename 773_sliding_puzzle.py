from collections import defaultdict, deque
import itertools
from copy import deepcopy

from heapq import heappop, heappush
import itertools



class Solution:

    # Attempt 1: BFS w/ seen states. Not optimal but successful attempt.

    def slidingPuzzle(self, board: list[list[int]]) -> int:
        seen_states = defaultdict(int)
        res = float('inf')
    
        def start_pos(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0: return (i, j)

        def search(board_state, pos, moves):
            if board_state == [[1,2,3],[4,5,0]]: return moves
            board_key = ''.join(list(map(str, itertools.chain.from_iterable(board_state))))
            if seen_states[board_key] and moves >= seen_states[board_key]: return
            seen_states[board_key] = moves
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_state = deepcopy(board_state)
                i, j = pos[0] + di, pos[1] + dj
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    new_state[i][j], new_state[pos[0]][pos[1]] = new_state[pos[0]][pos[1]], new_state[i][j]
                    to_search.append([new_state, (i, j), moves + 1])
            return None

        to_search = deque([[board, start_pos(board), 0]])
        while to_search:
            board_state, pos, moves = to_search.popleft()
            curr = search(board_state, pos, moves)
            if curr != None: res = min(res, curr)
        return res if res != float('inf') else -1

    # Attempt 2: A* search w/ Manhattan distance. Much faster.

    def slidingPuzzle_II(self, board: list[list[int]]) -> int:
        board = ''.join(str(n) for n in itertools.chain.from_iterable(board))
        target = '123450'
        rows, cols = 2, 3
        
        sequence = [n for n in board if n != '0']
        inv_count = sum(sequence[i] > sequence[j] for i in range(len(sequence)) for j in range(i, len(sequence)))
        if inv_count % 2 != 0:
            return -1

        def manhattan(board):
            curr = 0
            for i, char in enumerate(board):
                if char != '0':
                    distance = ord(char) - ord('1')
                    curr += abs(i // cols - distance // cols) + abs(i % cols - distance % cols)
            return curr
        
        to_search = [(manhattan(board), board)]
        distances = {board: 0}
        while to_search:
            _, board = heappop(to_search)
            if board == target: return distances[board]
            curr_pos = board.index('0')
            i, j = curr_pos // cols, curr_pos % cols
            for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x, y = i + di, j + dj
                if 0 <= x < rows and 0 <= y < cols:
                    new_pos = x * cols + y
                    board_conv = list(board)
                    board_conv[curr_pos], board_conv[new_pos] = board_conv[new_pos], board_conv[curr_pos]
                    new_board = ''.join(board_conv)
                    if new_board not in distances or distances[new_board] > distances[board] + 1:
                        distances[new_board] = distances[board] + 1
                        heappush(to_search, (distances[new_board] + manhattan(new_board), new_board))
        
        return -1

from time import time

if __name__ == "__main__":
    problem = Solution()
    start = time()
    print(problem.slidingPuzzle([[1,2,3],[4,0,5]]))
    print(time() - start)
    start = time()
    print(problem.slidingPuzzle_II([[1,2,3],[4,0,5]]))
    print(time() - start)
    start = time()
    print(problem.slidingPuzzle([[1,2,3],[5,4,0]]))
    print(time() - start)
    start = time()
    print(problem.slidingPuzzle_II([[1,2,3],[5,4,0]]))
    print(time() - start)