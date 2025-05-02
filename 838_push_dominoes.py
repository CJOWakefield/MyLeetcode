class Solution:  
    def pushDominoes(self, dominoes: str) -> str:
        forces = 'L' + dominoes + 'R'
        res, prev, n = list(forces), 0, len(forces)
        for i in range(1, n):
            if forces[i] == '.': continue
            if i - prev > 1:
                if forces[prev] == forces[i]:
                    for val in range(prev+1, i): res[val] = forces[i]
                elif forces[prev] == 'R' and forces[i] == 'L':
                    left, right = prev + 1, i - 1
                    while left < right:
                        res[left], res[right] = 'R', 'L'
                        left += 1
                        right -= 1
            prev = i
        return ''.join(res[1:-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.pushDominoes("RR.L"))
    print(sol.pushDominoes(".L.R...LR..L.."))
