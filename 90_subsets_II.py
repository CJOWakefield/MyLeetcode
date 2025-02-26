from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        counts = Counter(nums)

        def search(curr, prev, counts):
            res.append(curr)
            if not counts:return
            
            for num in list(counts.keys()):
                if num < prev: continue
                counts[num] -= 1
                if counts[num] == 0: del counts[num]
                search(curr + [num], num, counts)
                counts[num] += 1

        search([], float('-inf'), counts)
        return res
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.subsetsWithDup([1,2,2]))
    print(problem.subsetsWithDup([0]))