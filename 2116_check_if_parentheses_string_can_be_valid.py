def canBeValid(s: str, locked: str) -> bool:
    if len(s) % 2 != 0: return False
    opened, closed = 0, 0
    for i in range(len(s)):
        if s[i] == '(' or locked[i] == '0': opened += 1
        else: opened -= 1

        if s[-i-1] == ')' or locked[-i] == '0': closed += 1
        else: closed -= 1

        if opened < 0 or closed < 0: return False

    return True

if __name__ == '__main__':
    print(canBeValid("))()))", "010100"))
