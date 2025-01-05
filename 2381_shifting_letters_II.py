def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    pos_shifts = [0] * (len(s) + 1)
    for (start, end, direction) in shifts:
        pos_shifts[start] += 1 if direction == 1 else -1
        if end + 1 < len(s):
            pos_shifts[end+1] -= 1 if direction == 1 else -1

    curr, shifted = 0, list(s)
    for i in range(len(shifted)):
        curr += pos_shifts[i]
        net = (curr % 26 + 26) % 26
        shifted[i] = chr((ord(shifted[i]) - ord('a') + net) % 26 + ord('a'))
    return ''.join(shifted)


if __name__ == '__main__':
    print(shiftingLetters('abc', [[0,1,0],[1,2,1],[0,2,1]]))
