from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res, seen = [], {}
        for num in nums:
            if not num in seen.keys(): seen[num] = 1  
            else:
                res.append(num)
                del seen[num]
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicates([4,3,2,7,8,2,3,1]))
    print(sol.findDuplicates([1,1,2]))
    print(sol.findDuplicates([1]))
