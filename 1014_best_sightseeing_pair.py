def maxScoreSightseeingPair(values: list[int]) -> int:
    res, max_seen, max_idx = 0, values[0], 0
    for i in range(1, len(values)):
        curr_score = values[max_idx] + values[i] + max_idx - i
        if curr_score > res:
            res = curr_score
        if values[i] >= max_seen:
            max_seen, max_idx = values[i], i
        max_seen -= 1
    return res

if __name__ == '__main__':
    print(maxScoreSightseeingPair([8,1,5,2,6]))
