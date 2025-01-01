def isIsomorphic(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    res = {}

    for i in range(len(s)):
        char = s[i]
        if char not in res.keys():
            res[char] = t[i]
        else:
            if res[char] == t[i]:
                continue
            else:
                return False

    if len(set(res.values())) == len(res):
        return True
    return False

# Notes: No real issues, few edge cases raised issues but quickly resolved using sets.

def optimal(s, t):
    diction = {}

    for i,j in zip(s,t):
        if i not in diction.keys():
            if j not in diction.values():
                diction[i] = j
            elif i not in diction.keys():
                return False
        elif diction[i] != j:
            return False


# Optimal solution uses zip instead of indexing to retrieve values, and implements edge case protecting logic directly.

if __name__ == '__main__':
    print(isIsomorphic("badc", "baba"))
