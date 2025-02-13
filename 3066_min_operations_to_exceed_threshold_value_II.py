import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, (2 * x) + y)
            res += 1
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.minOperations([1,2,3,4,5], 10))
    print(problem.minOperations([1,2,3,4,5], 15))
    print(problem.minOperations([999999999,999999999,999999999], 1000000000))
    
    