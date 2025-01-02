def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    vowels = 'aeiou'
    double_ended = [0] * (len(words)+1)
    res = []

    for i in range(len(words)):
        double_ended[i+1] = double_ended[i]
        if words[i][0] in vowels and words[i][-1] in vowels:double_ended[i+1] += 1

    for query in queries:
        res.append(double_ended[query[1]+1] - double_ended[query[0]])
    return res

if __name__ == '__main__':
    print(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))
