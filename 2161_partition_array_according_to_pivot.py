class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]: 
        left, right, pivots = [], [], []
        for num in nums:
            if num == pivot: pivots.append(num)
            elif num < pivot: left.append(num)
            else: right.append(num)
        return left + pivots + right
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.pivotArray([9,12,5,10,14,3,10], 10))
    print(sol.pivotArray([-3,4,3,2], 2))
    print(sol.pivotArray([2,1,3,3,2,4,6,7,9,2,19], 2))
    