class Solution:
    def countAndSay(self, n: int) -> str:
        
        def convert(val):
            res = []
            curr = 1
            for i in range(1, len(val)):
                if val[i-1] == val[i]:
                    curr += 1
                    continue
                else:
                    res.append(f'{curr}{val[i-1]}')
                    curr = 1
            res.append(f'{curr}{val[-1]}')
            return ''.join(res)
        
        res = '1'
        for i in range(1, n):
            res = convert(res)
        return res
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(2))
    print(sol.countAndSay(3))
    print(sol.countAndSay(4))
    print(sol.countAndSay(5))