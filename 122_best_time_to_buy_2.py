def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    pos, profit = 0, 0
    while pos < len(prices)-1:
        if prices[pos] < prices[pos+1]:
            profit += prices[pos+1] - prices[pos]
        pos += 1
    return profit

## Notes - successful solution achieved off first attempt. Time complexity O(n) -> one loop through the prices. If we see an increase in price from pos -> pos+1, we log profit and move +1.

if __name__ == '__main__':
    print(maxProfit([1, 2, 3, 4, 5]))
