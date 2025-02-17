class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == '*':stack.pop()
            else: stack.append(char)
        return ''.join(stack)
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.removeStars("leet**cod*e"))
    print(problem.removeStars("erase*****"))
    