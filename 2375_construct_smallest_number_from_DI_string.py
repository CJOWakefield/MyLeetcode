class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res, stack = [], []
        
        for i in range(n + 1):
            stack.append(str(i + 1))
            # print(i, stack, res)
            if i == n or pattern[i] == 'I':
                res.extend(stack[::-1])
                stack = []
                
        return ''.join(res)
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.smallestNumber("IIIDIDDD"))
    print(problem.smallestNumber("DDD"))
    print(problem.smallestNumber("DIDDIIIIDI"))
    