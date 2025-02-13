class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        res = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while s[left] not in vowels and left < right: left += 1
            while s[right] not in vowels and left < right: right -= 1
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return ''.join(res)
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.reverseVowels("hello"))
    print(problem.reverseVowels("leetcode"))
    