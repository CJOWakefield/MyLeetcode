def maxDistance(colors: list[int]) -> int:
    res = 0
    for i, colour in enumerate(colors):
        if colour != colors[0]: res = max(res, i)
        if colour != colors[-1]: res = max(res, len(colors)-1-i)
    return res

if __name__ == '__main__':
    print(maxDistance(colors = [1,1,1,6,1,1,1]))
