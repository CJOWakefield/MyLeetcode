class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = []
        for num in nums:
            if not res or res[-1] < num: res.append(num)
            else:
                left, right = 0, len(res)-1
                while left <= right:
                    mp = (left + right) // 2
                    if num == res[mp]:
                        left = mp
                        break
                    elif res[mp] > num: right = mp - 1
                    else: left = mp + 1
                res[left] = num

        return len(res)

if __name__ == '__main__':
    problem = Solution()
    print(problem.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(problem.lengthOfLIS([0,1,0,3,2,3]))
    print(problem.lengthOfLIS([7,7,7,7,7,7,7]))
    
    