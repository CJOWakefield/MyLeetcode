def decrypt(code: list[int], k: int) -> list[int]:
    if k == 0: return [0] * len(code)
    elif k < 0: code, start, end = [0] + code[k:] + code, abs(k), len(code)+abs(k)
    else: code, start, end = code + code[:k], 0, len(code)

    cumulative = [0] * len(code)
    for i in range(len(code)):
        cumulative[i] = code[i] + cumulative[i-1]
    res = [cumulative[i+k] - cumulative[i] if k > 0 else cumulative[i] - cumulative[i+k] for i in range(start, end)]
    return res

if __name__ == '__main__':
    print(decrypt([1, 2, 3, 4, 5, 6, 7, 8], k=-3))
