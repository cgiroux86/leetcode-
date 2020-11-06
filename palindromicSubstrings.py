class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        length = len(s)
        dp = [[0 for _ in s] for _ in s]

        for i in range(length):
            dp[i][i] = 1
            count += 1

        for col in range(1, length):
            for row in range(col):
                print(col, row)
                if row == col - 1:
                    if s[row] == s[col]:
                        dp[row][col] = 1
                        count += 1
                elif row < col and s[row] == s[col] and dp[row + 1][col - 1] == 1:
                    dp[row][col] = 1
                    count += 1
        print(dp)
        print(count)


s = Solution()
s.countSubstrings("abs")
