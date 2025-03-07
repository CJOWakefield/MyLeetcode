class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        curr, replacements = 0, 0
        for char in s:
            if char == '(': curr += 1
            else: curr -= 1
            if curr < 0:
                replacements -= curr
                curr = 0
        return curr + replacements
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minAddToMakeValid("()))(("))
    print(sol.minAddToMakeValid("(()))"))
    print(sol.minAddToMakeValid("()"))