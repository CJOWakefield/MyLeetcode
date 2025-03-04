import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:  
        ordered = sorted(range(len(times)), key=lambda x: times[x][0])
        empty, occupied = list(range(len(times))), []

        for pos in ordered: 
            arrival, departure = times[pos]
            while occupied and occupied[0][0] <= arrival:
                heapq.heappush(empty, heapq.heappop(occupied)[1])
            curr = heapq.heappop(empty)
            if pos == targetFriend: return curr
            heapq.heappush(occupied, (departure, curr))

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestChair([[1,4],[2,3],[4,6]], 1))
    print(sol.smallestChair([[3,10],[1,5],[2,6]], 0))
    