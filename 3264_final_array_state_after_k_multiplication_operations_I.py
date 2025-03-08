import heapq

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        res = nums.copy()
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        while k:
            curr, pos = heapq.heappop(nums)
            heapq.heappush(nums, (curr * multiplier, pos))
            res[pos] *= multiplier
            k -= 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.getFinalState([1,2,3,4,5], 3, 2))
    print(sol.getFinalState([1,2,3,4,5], 10, 2))
    print(sol.getFinalState([1,2,3,4,5], 1, 1))