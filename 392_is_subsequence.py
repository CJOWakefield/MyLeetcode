class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True

        left, pos = 0, 0
        while left < len(t):
            if pos == len(s)-1 and s[pos] == t[left]: return True
            elif s[pos] == t[left]: pos += 1
            left += 1
        return False
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.isSubsequence("abc", "ahbgdc"))
    print(problem.isSubsequence("axc", "ahbgdc"))
    