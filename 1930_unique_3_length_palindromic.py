def countPalindromicSubsequence(s: str) -> int:
    left, right = [0] * 26, [0] * 26
    for char in s: right[ord(char) - ord('a')] += 1

    res = set()
    for i in range(len(s)):
        curr_i = ord(s[i]) - ord('a')
        right[curr_i] -= 1
        for j in range(26):
            if left[j] > 0 and right[j] > 0: res.add((curr_i * 26) + j)
        left[curr_i] += 1

    return len(res)

if __name__ == '__main__':
    print(countPalindromicSubsequence('aelllalelafc'))
