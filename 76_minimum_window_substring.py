def minWindow(s: str, t: str) -> str:
    left, right = 0, 1
    curr = s

    if len(s) < len(t):
        return ''

    if len(t) == 1 and t in s:
        return t

    while right <= len(s)-1:
        if s[left] in t:
            window = s[left:right]
            print(window)
            while not all(char in window for char in t):
                right += 1
                window = s[left:right]
            if len(window) < len(curr):
                curr = window
            left = right
        else:
            left += 1
            right += 1

    print(curr)
    return curr if len(curr) <= len(s) else ''


if __name__ == '__main__':
    print(minWindow("ab", 'b'))
