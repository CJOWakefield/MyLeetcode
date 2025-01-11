from collections import Counter

def canConstruct(s: str, k: int) -> bool:
    if len(s) < k: return False
    counts = Counter(s)
    odds = sum(1 for char in counts if counts[char] % 2 == 1)
    return odds <= k

if __name__ == '__main__':
    print(canConstruct('annabelle', k=2))
