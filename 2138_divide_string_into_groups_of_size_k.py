from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res, curr = [], ''
        for i in range(len(s)):
            if len(curr) == k:
                res.append(curr)
                curr = s[i]
            else: curr += s[i]
        
        if curr: res.append(curr + (fill * (k-len(curr))))
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.divideString(s = "abcdefghij", k = 3, fill = "x"))