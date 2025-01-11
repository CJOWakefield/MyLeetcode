def addSpaces(s: str, spaces: list[int]) -> str:
    spaces.append(len(s))
    res, pos, i_space = [], 0, 0
    while pos < len(s):
        if pos == spaces[i_space]:
            res.append(' ')
            i_space += 1
        res.append(s[pos])
        pos += 1
    return ''.join(res)

if __name__ == '__main__':
    print(addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
