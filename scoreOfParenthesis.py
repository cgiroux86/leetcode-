class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        total = 0
        stack = []
        tmp = 0
        for s in S:
            if s == "(":
            stack.append((s, 0))

        # def dfs(S, index, max_idx):

        #     if index > len(S):
        #         return 0
        #     max_idx = max(max_idx, index)
        #     if S[index] == ')':
        #         return 1
        #     if S[index] == '(':
        #         total = 2 * dfs(S, index + 1, index)
        #         return (total, max_idx + 1)
        # i = 0
        # while i < len(S) - 1:
        #     print(i)
        #     if S[i] == '(':
        #         res = dfs(S, i + 1, -1)
        #         print(res)
        #         total += 1 + df
        #         i += res[1]
        #     else:
        #         i += 1
        # print(total)
s = Solution()
s.scoreOfParentheses("(()(()))")
