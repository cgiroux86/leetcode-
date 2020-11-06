class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = [0]
        vals = {}
        i, j = 0, 0
        res = 0
        while j < len(s):
            print(stack)

            if s[j] not in vals:
                vals[s[j]] = j
                stack.append(j + 1)

            else:
                print(s[j], s[j - 1])
                if s[j] != s[j - 1] and j != len(s) - 1:
                    i = vals[s[j]] + 1
                    vals.pop(s[j])
                    vals[s[j]] = j
                    stack.append(j + 1)
                else:
                    i = j
            res = max(res, j - i + 1)
            j += 1

        return res


s = Solution()
print(s.lengthOfLongestSubstring(
    "dvdf"))
