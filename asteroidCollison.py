class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                if stack and stack[-1] > 0:
                    popped = False
                    while stack and stack[-1] > 0:
                        if abs(asteroids[i]) >= stack[-1]:
                            popped = stack.pop()

                        else:
                            popped = False
                            break
                    if popped and abs(popped) != abs(asteroids[i]):
                        stack.append(asteroids[i])
                else:
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
        return stack


s = Solution()
print(s.asteroidCollision([-2, -2, 1, -2]))
