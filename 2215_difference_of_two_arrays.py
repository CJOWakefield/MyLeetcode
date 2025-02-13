class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        counts_1, counts_2 = set(), set()
        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1): counts_1.add(nums1[i])
            if i < len(nums2): counts_2.add(nums2[i])
        return [list(counts_1 - counts_2), list(counts_2 - counts_1)]
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.findDifference([1,2,3], [2,4,6]))
    print(problem.findDifference([1,2,3,3], [1,1,2,2]))
    
    

