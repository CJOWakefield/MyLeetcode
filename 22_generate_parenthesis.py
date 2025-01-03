from collections import deque

def generateParenthesis(n: int) -> list[str]:
    to_search = deque([('(', n-1, n)])
    res = []
    while to_search:
        curr = to_search.popleft()
        curr_str, l_par_count, r_par_count = curr[0], curr[1], curr[2]
        if l_par_count == 0 and r_par_count == 0:
            res.append(curr_str)
            continue
        elif l_par_count < r_par_count:
            to_search.append([curr_str + ')', l_par_count, r_par_count-1])
        if l_par_count > 0:
            to_search.append([curr_str + '(', l_par_count-1, r_par_count])
    return res

if __name__ == '__main__':
    print(generateParenthesis(5))
