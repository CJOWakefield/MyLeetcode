class Solution:
    def minLength(self, s: str) -> int:
        seen = []
        for char in s:
            if seen and seen[-1] + char in ['AB', 'CD']: seen.pop()
            else: seen.append(char)
        return len(seen)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minLength("ABFCACDB"))
    print(sol.minLength("ACBBD"))
    