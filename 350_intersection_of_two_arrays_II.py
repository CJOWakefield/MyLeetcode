from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums2) < len(nums1): nums1, nums2 = nums2, nums1
        counts, nums2 = Counter(nums2), set(nums2)
        for val in nums1:
            if val in nums2 and counts[val] > 0:
                res.append(val)
                counts[val] -= 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersect([1,2,2,1], [2,2]))
    print(sol.intersect([4,9,5], [9,4,9,8,4]))