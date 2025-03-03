import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def pass_ratio(passed, students): return ((passed + 1) / (students + 1)) - (passed/students)

        heap = []
        heapq.heapify(heap)
        for passed, students in classes:
            diff = pass_ratio(passed, students)
            heapq.heappush(heap, (-diff, passed, students))

        while extraStudents:
            diff, passed, students = heapq.heappop(heap)
            heapq.heappush(heap, (-pass_ratio(passed+1, students+1), passed+1, students+1))
            extraStudents -= 1

        res = 0
        for _, passes, students in heap:
            res += passes/students
        return res / len(classes)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAverageRatio([[1,2],[3,5],[2,2]], 2))
    print(sol.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))
    