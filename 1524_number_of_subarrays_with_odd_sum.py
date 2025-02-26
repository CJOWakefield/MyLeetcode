class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = (10 ** 9) + 7
        curr, odds, evens = 0, 0, 1

        res = 0
        for val in arr:
            curr += val
            if curr % 2 == 1:
                odds += 1
                res += evens
            else:
                evens += 1
                res += odds
        res %= mod
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfSubarrays([1,3,5]))
    print(sol.numOfSubarrays([2,4,6]))
    print(sol.numOfSubarrays([1,2,3,4,5,6,7,8,9]))
