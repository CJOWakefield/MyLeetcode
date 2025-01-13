def rotateString(s: str, goal: str) -> bool:
    for i in range(len(s)):
        curr = ''.join([s[i:], s[:i]])
        if curr == goal: return True
    return False

if __name__ == '__main__':
    print(rotateString("gcmbf", goal = "fgcmb"))
