class Solution:
    def restoreMatrix(self, rowSum, colSum):
        res = [[0] * len(colSum) for _ in range(len(rowSum))]

        i, j = 0, 0
        while i < len(rowSum) and j < len(colSum):
            selection = min(rowSum[i], colSum[j])
            print(selection)
            res[i][j] = selection
            rowSum[i] -= selection
            colSum[j] -= selection
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1


s = Solution()
s.restoreMatrix([5, 7, 10], [8, 6, 8])
