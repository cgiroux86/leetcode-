class Solution:
    def numTimesAllBlue(self, light):
        total = 0
        blue = 0
        for i in range(len(light)):
            total += (light[i] - 1)
            if total % (i + 1) == 0:
                blue += 1
        print(blue - 1)
        # dp = [0] * (len(light))
        # blue = 0
        # for i in range(len(light)):
        #     print(dp, light[i])
        #     if dp[i] == 1:
        #         blue += 1
        #     dp[light[i] - 1] = 1
        #     print(dp, blue)
        # print(blue)


s = Solution()
s.numTimesAllBlue([1, 2, 3, 4, 5, 6])
