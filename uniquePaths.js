var uniquePathsIII = function (grid) {
  if (grid[0][0] !== 1) {
    return 0;
  }

  let total = 0;
  let stack = [[[0, 0]]];
  let visited = new Map();
  while (stack.length) {
    let path = stack.pop();
    let curr = path[path.length - 1];

    let [i, j] = curr;
    if (grid[i][j] === 2) return true;
    if (grid[i][j] === -1) return;
    if (!visited.get(`${[i, j]}`)) {
      visited.set(`${[i, j]}`, true);
      console.log(visited);
      for (let neighbor of findNeighbors([i, j], grid)) {
        stack.push([neighbor]);
      }
      visited.delete(`${[i, j]}`);
    }
  }
};

function dft(grid, i, j, visited) {}

function findNeighbors(idxs, grid) {
  let neighbors = [];
  let [i, j] = idxs;
  if (i > 0) neighbors.push([i - 1, j]);
  if (i < grid.length - 1) neighbors.push([i + 1, j]);
  if (j < grid[i].length) neighbors.push([i, i + 1]);
  if (j > 0) neighbors.push([i, j - 1]);
  return neighbors;
}

uniquePathsIII([
  [1, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 2, -1],
]);
