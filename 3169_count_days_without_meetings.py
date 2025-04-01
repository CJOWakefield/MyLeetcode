class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        
        merged = []
        for meet in meetings:
            if not merged or merged[-1][1] < meet[0]: 
                merged.append(meet)
            else: 
                merged[-1][1] = max(merged[-1][1], meet[1])
        
        res, curr = 0, 1
        for meet in merged:
            if meet[0] > curr: res += meet[0] - curr
            curr = meet[1] + 1
        return res + (days - curr + 1) if curr <= days else res

if __name__ == "__main__": 
    problem = Solution()
    print(problem.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
    print(problem.countDays(days = 10, meetings = [[1,2],[3,4],[5,6],[7,8],[9,10]]))
    print(problem.countDays(days = 57, meetings = [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]))
