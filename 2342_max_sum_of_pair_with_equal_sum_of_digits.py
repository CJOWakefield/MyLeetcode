from collections import defaultdict

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def sum_digits(num):
            count = 0
            while num: count, num = count + num % 10, num // 10
            return count
            
        res = 0
        digit_counts = defaultdict(int)
        for num in nums:
            curr = sum_digits(num)
            if digit_counts[curr]:
                val = digit_counts[curr]
                res = max(res, val + num)
                if num > val: digit_counts[curr] = num
            else: digit_counts[curr] = num
                
        return res if res else -1
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.maximumSum([18,43,36,13,7]))
    print(problem.maximumSum([10,12,19,14]))