from collections import Counter

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # DP for value counts
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Backtrack to find characters and indices.
        i, j = m, n
        result, pos_1, pos_2 = [], [], []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                pos_1.append(i-1)
                pos_2.append(j-1)
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1
        
        # Identify remaining characters
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        result.reverse()
        return ''.join(result)
    
# Notes: Revisit this type of problem. Couldn't recall LCS implementation from memory. Overall, not a bad problem logic wise.

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestCommonSupersequence("abac", "cab"))   
    print(sol.shortestCommonSupersequence("bbdafefg", "jxdbafzzq"))


