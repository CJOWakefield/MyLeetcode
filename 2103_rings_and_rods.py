from collections import defaultdict

def countPoints(rings: str) -> int:
    res = defaultdict(set)
    for i in range(0, len(rings), 2):
        c, rod = rings[i], rings[i+1]
        res[rod].add(c)
    return sum(1 if len(v) == 3 else 0 for k, v in res.items())

if __name__ == '__main__':
    print(countPoints("B0B6G0R6R0R6G9"))
