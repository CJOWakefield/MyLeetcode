from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        res = [0] * len(queries)
        balls, colours = defaultdict(int), defaultdict(int)
        unique_colours = 0
        for i, (ball, colour) in enumerate(queries):
            curr_colour = balls[ball]
            if curr_colour == 0:
                colours[colour] += 1
                if colours[colour] == 1: unique_colours += 1
            elif curr_colour != colour:
                colours[curr_colour] -= 1
                colours[colour] += 1
                if colours[curr_colour] == 0: unique_colours -= 1
                if colours[colour] == 1: unique_colours += 1
            balls[ball], res[i] = colour, unique_colours
        return res

if __name__ == '__main__':
    problem = Solution()
    print(problem.queryResults(3, [[1, 1], [2, 2], [3, 3], [1, 2], [2, 3], [3, 1]]))
