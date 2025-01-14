from collections import defaultdict

def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
    count, res = 0, [0] * len(A)
    seen = defaultdict(int)
    for i in range(len(A)):
        seen[A[i]] += 1
        seen[B[i]] += 1
        if seen[A[i]] > 1 and A[i] != B[i]: count += 1
        if seen[B[i]] > 1 and A[i] != B[i]: count += 1
        elif seen[A[i]] == seen[B[i]] > 1: count += 1
        res[i] = count
    return res

## Slight improvement: Intuition: In perfect array, set increases by 1 each time. If it increases by more/less, means unbalanced pair or pair balanced.

def improved(A, B):
    seen = set()
    res = [0] * len(A)
    for i in range(len(A)):
        seen.add(A[i])
        seen.add(B[i])
        res[i] = (2 * (i+1)) - len(seen)
    return res

if __name__ == '__main__':
    print(findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))
    print(improved(A = [1,3,2,4], B = [3,1,2,4]))
