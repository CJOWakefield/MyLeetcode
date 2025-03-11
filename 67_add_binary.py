class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a: return b
        if not b: return a

        res, carried = [], 0
        a_pos, b_pos = len(a)-1, len(b)-1

        while 0 <= a_pos or 0 <= b_pos or carried:
            if a_pos >= 0:
                carried += int(a[a_pos])
                a_pos -= 1
            if b_pos >= 0:
                carried += int(b[b_pos])
                b_pos -= 1
            res.append(str(carried % 2))
            carried //= 2
        
        return ''.join(res[::-1])
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))
    print(sol.addBinary("1010", "1011"))
    print(sol.addBinary("100", "110010"))
