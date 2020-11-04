class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        res = []

        def subSequence(s, i, j, string, cache):
            print(string)
            if i > len(s) - 1 or j < 0:
                return string
            if i == j:
                return s[i]
            if s[i] == s[j]:
                cache[(i, j)] = string + subSequence(s,
                                                     i + 1, j - 1, string, cache)
            else:
                cache[(i, j)] = subSequence(
                    s, i + 1, j - 1, string, cache)
                string += cache[(i, j)]
                print(string)

                if s[i] == s[j]:
                    string += cache[(i, j)]

            res.append(cache[(i, j)])
            return cache[(i, j)]
        subSequence(s, 0, len(s) - 1, "", {})
        print(res)


s = Solution()
s.longestPalindromeSubseq("bbbaaab")
