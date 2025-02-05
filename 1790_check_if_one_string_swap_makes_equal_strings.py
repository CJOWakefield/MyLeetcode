def areAlmostEqual(s1: str, s2: str) -> bool:
    swaps = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            swaps.append((s1[i], s2[i]))

    if len(swaps) == 1 or len(swaps) > 2: return False
    elif len(swaps) == 2:
        if swaps[0][0] == swaps[1][1] and swaps[0][1] == swaps[1][0]: return True
        else: return False
    else: return True

if __name__ == '__main__':
    print(areAlmostEqual('bank', 'kanb'))
