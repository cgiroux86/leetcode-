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
