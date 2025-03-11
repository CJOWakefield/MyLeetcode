class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        counts = [0, 0, 0]
        counts_map = {'a': 0, 'b': 1, 'c': 2}
        res, left = 0, 0

        for right in range(len(s)):
            counts[counts_map[s[right]]] += 1
            while all(counts) and left < right:
                counts[counts_map[s[left]]] -= 1
                left += 1
            res += left
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubstrings("abcabc"))
    print(s.numberOfSubstrings("aaacb"))
    print(s.numberOfSubstrings("abc"))
    print(s.numberOfSubstrings("abcc"))
    print(s.numberOfSubstrings("abcabcabc"))
    print(s.numberOfSubstrings("abcabcabcabc"))
    print(s.numberOfSubstrings("abcabcabcabcabc"))
    print(s.numberOfSubstrings("abcabcabcabcabcabc"))
