class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def search(i, curr):
            if len(curr) == k: 
                res.append(curr)
                return
            for num in range(i, n+1):
                search(num + 1, curr + [num])

        search(1, [])
        return res
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.combine(4, 2))
    print(problem.combine(1, 1))