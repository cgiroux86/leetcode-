class Solution:
    def numIslands(self, grid):
        total = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and self.dft(grid, i, j, visited):
                    total += 1
        return total

    def dft(self, grid, i, j, visited):
        stack = [(i, j)]
        counting = False
        while stack:
            curr = stack.pop()
            i, j = curr
            if curr not in visited:
                counting = True
                visited.add((i, j))
                for neighbor in self.findNeighbors(grid, i, j):
                    stack.append(neighbor)
        return counting

    def findNeighbors(self, grid, i, j):
        neighbors = []
        if i > 0 and grid[i - 1][j] == '1':
            neighbors.append((i - 1, j))

        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            neighbors.append((i + 1, j))

        if j > 0 and grid[i][j - 1] == "1":
            neighbors.append((i, j - 1))

        if j < len(grid[i]) - 1 and grid[i][j + 1] == '1':
            neighbors.append((i, j + 1))

        return neighbors


s = Solution()
print(s.numIslands([["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]]))
