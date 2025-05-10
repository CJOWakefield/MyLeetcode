from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zeroes1 = sum(nums1), nums1.count(0)
        sum2, zeroes2 = sum(nums2), nums2.count(0)
        sum1 += zeroes1
        sum2 += zeroes2

        if (zeroes1 == 0 and sum2 > sum1) or (zeroes2 == 0 and sum1 > sum2): return -1
        return max(sum1, sum2)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minSum(nums1 = [3,2,0,1,0], nums2 = [6,5,0]))
    print(sol.minSum(nums1 = [2,0,2,0], nums2 = [1,4]))
    print(sol.minSum(nums1 = [0,29,5,22,5,9,30,11,20,0,18,16,26,11,3,0,24,24,14,24], nums2 = [30,12,16,3,24,6,13,0,16]))
    print(sol.minSum(nums1 = [25,29,10,12,25,26,19,6,19,10,18], nums2 = [0,0,22,2,17,0,7,23,22,18,20,0,13,22,0,0,0,13,6,8]))
