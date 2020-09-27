# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# Example 1:

# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    curr_total = self.dft(grid, i, j, visited)
                    max_area = max(max_area, curr_total)
                    print(max_area)

        return max_area

    def dft(self, grid, i, j, visited):
        queue = [(i, j)]
        total = 0
        while queue:
            path = queue.pop()
            i, j = path
            print(i, j)
            if (i, j) not in visited:
                total += 1
                visited.add((i, j))
                for neighbor in self.findNeighbors(grid, i, j):
                    queue.append(neighbor)
        return total

    def findNeighbors(self, grid, i, j):
        neighbors = []
        if i > 0 and grid[i - 1][j]:
            neighbors.append((i - 1, j))

        if i < len(grid) - 1 and grid[i + 1][j]:
            neighbors.append((i + 1, j))

        if j > 0 and grid[i][j - 1]:
            neighbors.append((i, j - 1))

        if j < len(grid[i]) - 1 and grid[i][j + 1]:
            neighbors.append((i, j + 1))
        print(neighbors)
        return neighbors


s = Solution()
# s.maxAreaOfIsland(
#     [[1, 1, 0, 0, 0],
#      [1, 1, 0, 0, 0],
#      [0, 0, 0, 1, 1],
#      [0, 0, 0, 1, 1]])
# s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])

s.maxAreaOfIsland([[1, 1]])
