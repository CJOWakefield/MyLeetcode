class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack(pos, prev):
            if len(res) == k: return
            if pos == n:
                res.append(prev)
                return
            
            for char in 'abc':
                if prev and char == prev[-1]: continue
                backtrack(pos+1, prev+char)
        
        backtrack(0, '')
        return res[k-1] if k <= len(res) else '' 
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.getHappyString(3, 9))
    print(problem.getHappyString(1, 3))
    print(problem.getHappyString(2, 7))