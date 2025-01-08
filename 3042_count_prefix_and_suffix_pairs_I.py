def countPrefixSuffixPairs(words: list[str]) -> int:
    res = 0
    for i in range(len(words)):
        curr = words[i]
        rem = words[i+1:]
        for sub in rem:
            if len(sub) >= len(curr):
                if sub[:len(curr)] == sub[-len(curr):] == curr: res += 1
    return res

if __name__ == '__main__':
    print(countPrefixSuffixPairs(['ab', 'abab', 'abba']))
