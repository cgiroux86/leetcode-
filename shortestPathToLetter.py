class Solution:
    def shortestToChar(self, S, C):
        res = []
        for i in range(len(S)):

            # while i < len(S):
            #     low = i
            #     high = i
            #     while S[high] != 'e' and high < len(S):
            #         high += 1
            #     while S[low] != 'e' and low >= 0:
            #         low -= 1
            #     if low == high:
            #         res.append(0)
            #     else:
            #         if low > 0:
            #             print(i, high + i - i, low - i + 1, "$$$$$")
            #             res.append(min(high - i, i - low))
            #         else:
            #             res.append(high - i)
            #     i += 1

        print(res)
        # res.append(min(i))

        # print(high, low)

        # def findPath(i, c, curr_max):
        #     print(i, S[i])
        #     if i < 0:
        #         return
        #     if i > len(S):
        #         return
        #     if S[i] == C:
        #         print('returning i')
        #         return i
        #     curr_max = min(findPath(i + 1, c, curr_max),
        #                    findPath(i - 1, c, curr_max))
        #     return curr_max

        # for i in range(len(S)):
        #     test = findPath(i, S, float('inf'))
        #     print(test)


s = Solution()
s.shortestToChar('loveleetcode', 'e')
