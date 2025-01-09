def prefixCount(words: list[str], pref: str) -> int:
    return len([word for word in words if word[:len(pref)] == pref])

if __name__ == '__main__':
    print(prefixCount(["pay","attention","practice","attend"], 'at'))
