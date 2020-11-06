class Solution:
    def __init__(self):
        self.visited = set()

    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 and (i, j) not in self.visited:
                    for neighbor in self.setter(matrix, i, j):
                        matrix[neighbor[0]][neighbor[1]] = 0
                        self.visited.add((neighbor[0], neighbor[1]))
        print(matrix)

    def setter(self, matrix, i, j):

        neighbors = []
        if i < len(matrix) - 1:
            neighbors.append((i + 1, j))
        if i > 0:
            neighbors.append((i - 1, j))
        if j < len(matrix[i]) - 1:
            neighbors.append((i, j + 1))
        if j > 0:
            neighbors.append((i, j - 1))
        return neighbors


s = Solution()
s.setZeroes([[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]])
