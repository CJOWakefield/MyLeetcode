def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    s = s.split()
    curr = {}

    if len(pattern) != len(s):
        return False

    for i, char in enumerate(pattern):
        if char not in curr.keys():
            curr[char] = s[i]
        if curr[char] != s[i]:
            return False

    # Check for repeated items
    if set(k for k,v in curr.items() if curr.values().count(v) > 1):
        return False

    return True

# Notes: Easy challenge, few edge case issues but solved immediately.

if __name__ == '__main__':
    # print(wordPattern("abba"))
    for char, i in enumerate([1, 2, 3, 4]):
        print(char)
        print(i)
