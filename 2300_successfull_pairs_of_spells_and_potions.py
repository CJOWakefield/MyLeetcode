class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        res = []
        potions.sort()

        def potion_search(spell):
            left, right = 0, len(potions)-1
            while left <= right:
                mp = (left + right) // 2
                curr = spell * potions[mp]
                if curr == success:
                    return potions.index(potions[mp])
                elif curr < success: left = mp + 1
                else: right = mp-1
            return left if left < len(potions) else -1

        for spell in spells:
            pos = potion_search(spell)
            if pos >= 0: res.append(len(potions) - pos)
            else: res.append(0)
        return res
    
if __name__ == '__main__':
    problem = Solution()
    print(problem.successfulPairs([5,1,3], [1,2,3,4,5], 7))
    print(problem.successfulPairs([3,1,2], [8,5,8], 16))
    