class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < -1 * asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -1 * asteroid:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.asteroidCollision([5, 10, -5]))
    print(problem.asteroidCollision([8, -8]))
    print(problem.asteroidCollision([10, 2, -5]))