from collections import defaultdict

def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
    sub_counts = defaultdict(int)
    for i in range(len(words2)):
        word_count, word = defaultdict(int), words2[i]
        for char in word: word_count[char] += 1
        for char in word_count: sub_counts[char] = max(word_count[char], sub_counts[char])

    res = []
    for word in words1:
        valid, counts = True, defaultdict(int)
        for char in word: counts[char] += 1
        for char in sub_counts:
            if sub_counts[char] > counts[char]: valid = False
        if valid: res.append(word)
    return res

if __name__ == '__main__':
    print(wordSubsets(words1 = ["bcbba","acbbc","aabaa","cbcbc","cacca"], words2 = ["cb","a","b"]))
