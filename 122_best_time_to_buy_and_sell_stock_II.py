def maxProfit(prices: list[int]) -> int:
    curr = 0
    for i in range(len(prices)-1):
        profit = prices[i+1] - prices[i]
        if profit > 0:
            curr += profit

    return curr


if __name__ == '__main__':
    print(maxProfit([5, 1, 2, 3, 1, 5, 9, 8, 8, 4]))
