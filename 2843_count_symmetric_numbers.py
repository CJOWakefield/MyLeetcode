import time

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            curr = str(i)
            n = len(curr)
            if n % 2 == 0:
                left, right = curr[:n//2], curr[n//2:]
                if sum(int(x) for x in left) == sum(int(x) for x in right):
                    count += 1
        return count
    
    def countSymmetricIntegers_II(self, low: int, high: int) -> int:
        count = 0 
        for i in range(low, high+1):
            curr = str(i)
            n = len(curr)
            if n % 2 == 0:
                left, right = int(curr[:n//2]), int(curr[n//2:])
                l_sum, r_sum = 0, 0
                while left: 
                    l_sum += left % 10
                    left //= 10
                while right:
                    r_sum += right % 10
                    right //= 10
                if l_sum == r_sum:
                    count += 1
        return count
    
if __name__ == "__main__":
    sol = Solution()
    start_time = time.time()
    print(sol.countSymmetricIntegers(low = 1, high = 100))
    print(sol.countSymmetricIntegers(low = 1200, high = 1230))
    print(sol.countSymmetricIntegers(low = 100, high = 1782))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    start_time = time.time()
    print(sol.countSymmetricIntegers_II(low = 1, high = 100))
    print(sol.countSymmetricIntegers_II(low = 1200, high = 1230))
    print(sol.countSymmetricIntegers_II(low = 100, high = 1782))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    
    
    
