class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        res = []
        n = len(nums[0])

        def backtrack(pos, prev):
            if prev in nums or res: return
            if pos == n:
                res.append(prev)
                return
            for val in '10': backtrack(pos+1, prev+val)

        backtrack(0, '')
        return res[0]
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.findDifferentBinaryString(["01","10"]))
    print(problem.findDifferentBinaryString(["00","01"]))
    print(problem.findDifferentBinaryString(["111","011","001"]))