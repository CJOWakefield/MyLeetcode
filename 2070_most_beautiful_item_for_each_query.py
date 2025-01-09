from collections import defaultdict

def maximumBeauty(items: list[list[int]], queries: list[int]) -> list[int]:
    items.sort(key=lambda x: x[0])
    query_sort = sorted(queries)
    query_i, item_i, curr_max, store = 0, 0, 0, defaultdict(int)

    while query_i < len(queries):
        while item_i < len(items) and query_sort[query_i] >= items[item_i][0]:
            curr_max = max(curr_max, items[item_i][1])
            item_i += 1
        store[query_sort[query_i]] = curr_max
        query_i += 1
    return [store[query] for query in queries]

if __name__ == '__main__':
    print(maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))
