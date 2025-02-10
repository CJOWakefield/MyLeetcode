class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        digits = '1234567890'
        for i in range(len(s)):
            if s[i] in digits:
                res.pop(-1)
            else: res.append(s[i])
        return ''.join(res)

if __name__ == '__main__':
    problem = Solution()
    print(problem.clearDigits("abccd1f6dd3a"))
