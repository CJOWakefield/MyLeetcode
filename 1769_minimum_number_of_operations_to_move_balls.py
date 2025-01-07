def minOperations(boxes: str) -> list[int]:
    n = len(boxes)
    l_tally, r_tally, left, right = 0, 0, [0] * n, [0] * n

    for i in range(1, n):
        if boxes[i-1] == '1': l_tally += 1
        left[i] = left[i-1] + l_tally

    for j in range(n-2, -1, -1):
        if boxes[j+1] == '1': r_tally += 1
        right[j] = right[j+1] + r_tally

    return [(l+r) for l,r in zip(left, right)]

if __name__ == '__main__':
    print(minOperations('110'))
