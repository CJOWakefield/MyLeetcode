from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        curr = set(nums)
        for i in range(1, len(nums)+1):
            if i not in curr: res.append(i)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(sol.findDisappearedNumbers([1,1]))
    print(sol.findDisappearedNumbers([1,2]))
