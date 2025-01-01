def findKthLargest(nums: list[int], k: int) -> int:
        res = [nums[0]]

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr > res[-1]:
                res.append(curr)

            else:
                for j, val in enumerate(res):
                    if val >= curr:
                        res.insert(j, curr)
                        break

            res = res[-k:]

        return res[0]


if __name__ == '__main__':
    print(findKthLargest([3,2,1,5,6,4], 2))


# def findKthLargest(self, nums: List[int], k: int) -> int:
#         res = [nums[0]]

#         for i in range(1, len(nums)):
#             if nums[i] > res[-1]:
#                 if len(res) == k:
#                     res.append(num)
#                     _ = res.pop()

#             else:
#                 if len(res) >= 1:
#                     for j, val in enumerate(res):
#                         if nums[i] > val and nums[i] <= res[j-1]:
#                             res.insert(j, nums[i])
#                 else:
#                     if nums[i] > res[-1]:
#                         res.insert(1, nums[i])
#                     else:
#                         res.insert(0, nums[i])

#         return res
