class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        curr, self.stack = self.stack[-1], self.stack[:-1]
        return curr

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == '__main__':
    problem = MyStack()
    problem.push(1)
    problem.push(2)
    print(problem.top())
    print(problem.pop())
    print(problem.empty())