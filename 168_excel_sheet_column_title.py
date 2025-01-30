def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber:
        columnNumber -= 1
        res.append(chr(columnNumber % 26 + ord('A')))
        columnNumber //= 26
    return ''.join(res[::-1])

if __name__ == '__main__':
    print(convertToTitle(120))
