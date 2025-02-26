class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'

        vals = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        m, n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                val1, val2 = vals[num1[i]], vals[num2[j]]
                pos1, pos2 = i+j, i+j+1
                
                calc = (val1 * val2) + res[pos2]
                res[pos2] = calc % 10
                res[pos1] += calc // 10

        return ''.join(map(str, res)).lstrip('0')
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2", "3"))
    print(sol.multiply("123", "456"))
    print(sol.multiply("0", "0"))
    print(sol.multiply("10", "10"))
    print(sol.multiply("10", "0"))