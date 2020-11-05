from typing import List


# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

#         def dft(heights, bricks, ladders, index, cache):

#             usingBricks = 0
#             usingLadders = 0
#             if index == len(heights) - 1:
#                 return 0
#             if bricks < 0 or ladders < 0:
#                 return 0
#             if index not in cache:
#                 if heights[index] >= heights[index + 1]:
#                     cache[index] = 1 + \
#                         dft(heights, bricks, ladders, index + 1, cache)
#                 else:
#                     if bricks - (heights[index + 1] - heights[index]) > 0 and ladders > 0:
#                         cache[index] = usingBricks = 1 + dft(heights, bricks -
#                                                              (heights[index + 1] - heights[index]), ladders, index + 1, cache) + 1 + \
#                             dft(heights, bricks, ladders - 1, index + 1, cache)
#                     else:
#                         cache[index] = 1 +
#       dft(heights, bricks, ladders - 1, index + 1, cache)

#             print(cache)
#             return cache[index]
#         return dft(heights, bricks, ladders, 0, {})


# s = Solution()
# s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19],
#                    10,
#                    2)


# [[0,0,0], [0,0,0], [0,0,0]]

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dp[i][j] =  dp[i-1][j-1] + 1 if A[i] == B[j]
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        result = 0
        for i in range(len(A)):
            for j in range(len(B)):
                # condition dp
                if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        return result

    def maxTurbulenceSize(self, A: List[int]) -> int:
        L, R = 0, 1
        sign = None
        res = 0
        while L < R < len(A):
            print(A[L:R + 1], sign)
            if sign == None:
                sign = 1 if A[R] > A[R - 1] else 0

                continue
            elif sign == 1 and A[R] < A[R - 1] or sign == 0 and A[R] > A[R - 1] or A[R] == A[R - 1]:
                print(A[R], A[R - 1])
                res = max(res, R - L + 1)
                sign = 1 if A[R] > A[R - 1] else 0
                L = R
                R += 1

            else:
                sign = 1 if A[R] > A[R - 1] else 0
                L += 1
                R += 1
            print(sign)

        res = max(res, R - L + 1)
        return res


s = Solution()
print(s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
