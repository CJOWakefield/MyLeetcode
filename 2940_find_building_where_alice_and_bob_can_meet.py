import heapq

def leftmostBuildingQueries(heights: list[int], queries: list[list[int]]) -> list[int]:
    res = [-1] * len(queries)
    search = [[] for _ in range(len(heights))]

    # Order queries based on relative heights: b always greater
    for i, (a, b) in enumerate(queries):
        if a > b: a, b = b, a
        if a == b or heights[a] < heights[b]: res[i] = b
        else: search[b].append((heights[a], i))

    heap = []
    for i, height in enumerate(heights):
        for curr in search[i]:
            heapq.heappush(heap, curr)
        while heap and heap[0][0] < height:
            _, i_res = heapq.heappop(heap)
            res[i_res] = i
    return res

if __name__ == '__main__':
    print(leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))
