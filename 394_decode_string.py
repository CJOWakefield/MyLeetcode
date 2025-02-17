class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr, curr_val = '', 0
        # if len(s) < 4: return ''
        for char in s:
            if char.isdigit(): curr_val = (curr_val * 10) + int(char)
            elif char == '[':
                stack.append((curr, curr_val))
                curr, curr_val = '', 0
            elif char == ']':
                prev, prev_val = stack.pop()
                curr = prev + (prev_val * curr)
            else: curr += char
        return curr
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.decodeString("3[a]2[bc]"))
    print(problem.decodeString("3[a2[c]]"))
    