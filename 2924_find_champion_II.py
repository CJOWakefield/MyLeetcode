from collections import defaultdict, deque

def findChampion(n: int, edges: list[list[int]]) -> int:
    res, rankings = set(), defaultdict(set)
    for strong, weak in edges: rankings[weak].add(strong)

    for i in range(n):
        if i not in rankings: res.add(i)
    return list(res)[0] if len(res) == 1 else -1

if __name__ == '__main__':
    print(findChampion(4, [[0,2],[1,3],[1,2]]))
