class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        pos, sub_len, curr = 0, len(part), ''
        for char in s:
            curr += char
            pos += 1
            if curr.endswith(part) and pos >= sub_len:
                pos -= sub_len
                curr = curr[:-sub_len]
        return ''.join(curr)


if __name__ == '__main__':
    problem = Solution()
    print(problem.removeOccurrences('daabcbaabcbc', 'abc'))
