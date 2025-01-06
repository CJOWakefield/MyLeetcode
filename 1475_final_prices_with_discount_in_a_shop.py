def finalPrices(prices: list[int]) -> list[int]:
    res = []
    for i in range(len(prices)-1):
        curr, j = prices[i], i+1
        while j < len(prices):
            if prices[i] >= prices[j]:
                curr -= prices[j]
                break
            else: j += 1
        res.append(curr)
    return res + [prices[-1]]

if __name__ == '__main__':
    print(finalPrices([8,7,4,2,8,1,7,7,10,1]))
