from collections import defaultdict
from operator import itemgetter

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        values = defaultdict(int)
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1): values[nums1[i][0]] += nums1[i][1]
            if i < len(nums2): values[nums2[i][0]] += nums2[i][1]
        return sorted([[k, v] for k, v in values.items()], key=itemgetter(0))
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
    print(sol.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))
    