class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        maxInEachCol = [0] * len(grid)
        maxInEachRow = [0] * len(grid[0])

        for i in range(len(grid)):
            currentRowMax = 0
            currentColMax = 0
            for j in range(len(grid[i])):
                if grid[i][j] > currentRowMax:
                    currentRowMax = grid[i][j]
                if grid[j][i] > currentColMax:
                    currentColMax = grid[j][i]
            maxInEachRow[i] = currentRowMax
            maxInEachCol[i] = currentColMax

        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += min(maxInEachRow[i], maxInEachCol[j]) - grid[i][j]
        return sum


# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation:
# The grid is:
# [ [3, 0, 8, 4],
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]

# The grid after increasing the height of buildings without affecting skylines is:

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

s = Solution()
print(s.maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
