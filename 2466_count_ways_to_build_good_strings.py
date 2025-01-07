def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    mod = (10 ** 9) + 7
    dp = [0] * (high + 1)
    dp[0] = 1
    for i in range(1, high + 1):
        if i >= zero: dp[i] = (dp[i] + dp[i - zero]) % mod
        if i >= one: dp[i] = (dp[i] + dp[i - one]) % mod
    return sum(dp[i] for i in range(low, high+1)) % mod

if __name__ == '__main__':
    print(countGoodStrings(200, 200, 10, 1))
