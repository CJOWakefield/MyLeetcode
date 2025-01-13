from collections import Counter

def minimumLength(s: str) -> int:
    res, counts = 0, Counter(s)
    for k, v in counts.items():
        if v <= 2:
            res += counts[k]
            continue
        elif v % 2 != 0: res += v % 2
        else: res += 2
    return res

if __name__ == '__main__':
    print(minimumLength(s = "abaacbcbb"))
