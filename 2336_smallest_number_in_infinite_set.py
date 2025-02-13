class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.stored = set()

    def popSmallest(self) -> int:
        if self.stored:
            res = min(self.stored)
            self.stored.remove(res)
            return res
        else:
            self.curr += 1
            return self.curr - 1

    def addBack(self, num: int) -> None:
        if self.curr > num:
            self.stored.add(num)


if __name__ == '__main__':
    problem = SmallestInfiniteSet()
    print(problem.popSmallest())
    print(problem.popSmallest())
    print(problem.popSmallest())
    print(problem.addBack(1))
    print(problem.popSmallest())
    print(problem.popSmallest())
    print(problem.popSmallest())
    