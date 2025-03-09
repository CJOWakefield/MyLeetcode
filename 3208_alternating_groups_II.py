class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        colors.extend(colors[:k-1])
        res, count = 0, 1
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]: 
                count = 1
                continue
            count += 1
            if count >= k: res += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfAlternatingGroups([1,1,2,2,3,3,4,4,5,5], 2))
    print(sol.numberOfAlternatingGroups([1,1,2,2,3,3,4,4,5,5], 3))
    print(sol.numberOfAlternatingGroups([1,1,2,2,3,3,4,4,5,5], 4))