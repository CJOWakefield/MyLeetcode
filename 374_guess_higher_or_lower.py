# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

import random

class Solution:
    def __init__(self):
        self.target = random.randint(1, 1000)

    def guess(self, num: int) -> int:
        if num == self.target: return 0
        elif num > self.target: return -1
        else: return 1

    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left < right:
            mp = (left + right) // 2
            res = self.guess(mp)
            if not res: return mp
            elif res > 0: left = mp + 1
            else: right = mp
        return left
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.guessNumber(1000))
    print(problem.guessNumber(1))
    print(problem.guessNumber(2))