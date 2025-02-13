class Solution:
    def largestAltitude(self, gain: list[int]) -> int:  
        res, curr = 0, 0
        for i in range(len(gain)):
            curr += gain[i]
            res = max(res, curr)
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.largestAltitude([-5,1,5,0,-7]))
    print(problem.largestAltitude([-4,-3,-2,-1,4,3,2]))
    