class Solution:
    def minimumRemoval(self, beans: list[int]) -> int:
        beans.sort()
        left, right = 0, sum(beans)
        res = float('inf')
        for i, bean in enumerate(beans):
            total = left + right - ((len(beans) - i) * bean)
            if total < res: res = total
            left += bean
            right -= bean
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.minimumRemoval([4,1,6,5]))
    print(problem.minimumRemoval([2,10,3,2]))
    