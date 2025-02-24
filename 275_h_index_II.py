class Solution:
    def hIndex(self, citations: list[int]) -> int:
        res, n = 0, len(citations)
        left, right = 0, n-1
        while left <= right:
            mp = (left + right) // 2
            if citations[mp] >= n - mp:
                res = n - mp
                right = mp -1
            else: left = mp + 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([0,1,3,5,6]))
    print(sol.hIndex([0,1,2,3,4,5,6,7,8,9,10]))
    print(sol.hIndex([0,1,2,3,4,5,6,7,8,9,10]))
    print(sol.hIndex([0,1,2,3,4,5,6,7,8,9,10]))
    
