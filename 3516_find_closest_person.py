class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx, dy = abs(x-z), abs(y-z)
        if dx < dy: return 1
        elif dy < dx: return 2
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosest(2, 7, 4))
    print(sol.findClosest(2, 5, 6))
    print(sol.findClosest(1, 5, 3))
