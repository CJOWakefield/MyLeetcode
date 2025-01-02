def maxScore(s: str) -> int:
    ones = s.count('1')
    if ones == 0: return len(s)-1
    best_score = ones+1 if s[0] == '0' else ones-1
    curr_score = best_score
    for i in range(1, len(s)-1):
        if s[i] == '0': curr_score += 1
        else: curr_score -= 1
        best_score = max(best_score, curr_score)
    return best_score

if __name__ == '__main__':
    print(maxScore('0101000101010111101010'))
