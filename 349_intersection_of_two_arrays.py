class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        res = []
        for num in nums2:
            if num in seen:
                seen.remove(num)
                res.append(num)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))
    print(sol.intersection([4,9,5], [9,4,9,8,4]))
    