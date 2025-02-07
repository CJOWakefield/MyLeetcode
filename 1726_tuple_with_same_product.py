from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        res, counts = 0, defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if counts[product] > 0:
                    res += counts[product] * 8
                counts[product] += 1
        return res


if __name__ == '__main__':
    problem = Solution()
    print(problem.tupleSameProduct([2, 3, 4, 6]))
