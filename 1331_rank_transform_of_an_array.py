from collections import defaultdict

def arrayRankTransform(arr: list[int]) -> list[int]:
    sort, ranking = sorted(list(set(arr))), defaultdict(int)
    for i in range(len(sort)): ranking[sort[i]] = i+1
    return [ranking[val] for val in arr]

if __name__ == '__main__':
    print(arrayRankTransform([37,12,28,9,100,56,80,5,12]))
