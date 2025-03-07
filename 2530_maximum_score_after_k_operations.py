import heapq

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        res = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k:
            curr = heapq.heappop(nums)
            heapq.heappush(nums, curr // 3)
            res += -curr
            k -= 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxKelements([1, 13, 45, 5, 44], 3))
    print(sol.maxKelements([4, 4, 4], 3))
