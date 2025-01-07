def stringMatching(words: list[str]) -> list[str]:
    res = []
    for i in range(len(words)):
        rem = words[:i] + words[i+1:]
        for word in rem:
            if words[i] in word:
                res.append(words[i])
                break
    return res

# Alt version:
def stringMatching_II(words: list[str]) -> list[str]:
    joined = ','.join(words)
    return [word for word in words if joined.count(word) > 1]

if __name__ == '__main__':
    print(stringMatching(["mass","as","hero","superhero"]))
    print(stringMatching_II(["mass","as","hero","superhero"]))
