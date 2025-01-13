def timeRequiredToBuy(tickets: list[int], k: int) -> int:
    res = 0
    for i in range(len(tickets)):
        if i <= k: res += min(tickets[i], tickets[k])
        else: res += min(tickets[i], tickets[k]-1)
    return res

if __name__ == '__main__':
    print(timeRequiredToBuy([2, 3, 2], k=2))
