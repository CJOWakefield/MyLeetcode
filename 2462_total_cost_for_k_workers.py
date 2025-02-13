import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        left_candidates = costs[:candidates]
        right_candidates = costs[max(candidates, len(costs)-candidates):]

        heapq.heapify(left_candidates)
        heapq.heapify(right_candidates)

        left, right = candidates, len(costs) - candidates - 1
        res = 0

        while k:
            if right_candidates and (not left_candidates or right_candidates[0] < left_candidates[0]):
                res += heapq.heappop(right_candidates)
                if left <= right:
                    heapq.heappush(right_candidates, costs[right])
                    right -= 1
            else:
                res += heapq.heappop(left_candidates)
                if left <= right:
                    heapq.heappush(left_candidates, costs[left])
                    left += 1
            k -= 1
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.totalCost([50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58], 7, 12))