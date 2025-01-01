def canJump(nums: list[int]) -> bool:
    def canReach(pos):
        if pos == 0:
            return True
        for j in range(pos-1, -1, -1):
            if nums[j] >= pos - j:
                # print(f'Index {pos} can be reached from index {j} which can jump {pos - j} as the jump allowed is {nums[j]}')
                return canReach(j)
        return False

    return True if canReach(len(nums)-1) else False


if __name__ == '__main__':
    print(canJump([3,2,1,0,4]))
