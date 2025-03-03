class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if ((num * 2 in seen) or (num / 2 in seen)): return True
            seen.add(num)
        return False
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfExist([10,2,5,3]))
    print(sol.checkIfExist([7,1,14,11]))
    print(sol.checkIfExist([3,1,7,11]))