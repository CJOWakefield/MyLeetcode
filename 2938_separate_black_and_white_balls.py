class Solution:
    def minimumSteps(self, s: str) -> int:
        res, ones = 0, 0
        for val in s:
            if val == '1': ones += 1
            else: res += ones
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSteps("1111"))
    print(sol.minimumSteps("00110"))
    