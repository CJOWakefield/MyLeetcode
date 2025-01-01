# def fullJustify(words: list[str], maxWidth: int) -> list[str]:
#     res, curr = [], f'{words.pop(0)}
#     while words:
#         word = words.pop(0)
#         if len(curr) + len(word) > maxWidth:
#             rem = len(curr) - maxWidth
#             res.append(curr + ' ' * rem)
#             curr = word
#         else:
#             curr += ' ' + word
#     res.append(curr)

#     return res

def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    res, curr, curr_len = [], [], 0
    spaces = 0
    while words:
        word = words.pop(0)
        if curr_len + len(word) > maxWidth - len(curr) - 2:
            spaces = (maxWidth - curr_len) // len(curr)
            splitter = ' ' * spaces
            res.append(splitter.join(curr))
            curr, curr_len = [word], len(word)
        else:
            curr.append(word)
            curr_len += len(word)
        print(curr, curr_len, spaces)
    res.append(' '.join(curr) + (maxWidth - curr_len - len(curr)) * ' ')

    return res

# Notes: First attempt, misread the prompt. Successfully aligned words but need to evenly space. Can do by converting curr to list and implementing string concat when cumulative list lengths exceed maxLength.

if __name__ == '__main__':
    result = fullJustify(["What","must","be","acknowledgment","shall","be", 'but', 'i', 'know', 'that', 'everything', 'will', 'be', 'ok'], maxWidth = 16)
    for res in result:
        print(res, len(res))
