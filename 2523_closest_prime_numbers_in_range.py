class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        def find_primes(n):
            is_prime = [True] * (n + 1)
            p = 2
            if n > 0: is_prime[0] = is_prime[1] = False
            while p * p <= n:
                if is_prime[p]:
                    for i in range(p * p, n + 1, p): is_prime[i] = False
                p += 1
            primes = [p for p in range(n + 1) if is_prime[p]]
            return primes

        primes = find_primes(right)
        res, diff = [], float('inf')
        for i in range(len(primes)-1, 0, -1):
            if primes[i-1] < left: break
            if primes[i]-primes[i-1] <= diff:
                diff = primes[i]-primes[i-1]
                res = [primes[i-1], primes[i]]
        return res if res else [-1, -1]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.closestPrimes(10, 19))
    print(sol.closestPrimes(1, 1000000))

