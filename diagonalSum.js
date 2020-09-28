var diagonalSum = function (mat) {
  const visited = new Map();
  const primary = primarySum(mat, 0, 0);
  const secondary = secondarySum(mat, 0, mat[0].length - 1);
  return primary + secondary;

  function primarySum(mat, i, j) {
    if (i === mat.length) {
      return 0;
    }
    visited.set(`${[i, j]}`, true);
    return mat[i][j] + primarySum(mat, i + 1, j + 1);
  }
  function secondarySum(mat, i, j) {
    if (i === mat.length || j < 0) return 0;
    console.log(visited, i, j);
    if (visited.get(`${[i, j]}`)) {
      return 0 + secondarySum(mat, i + 1, j - 1);
    }
    return mat[i][j] + secondarySum(mat, i + 1, j - 1);
  }
};

console.log(
  diagonalSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ])
);

console.log(
  diagonalSum([
    [7, 3, 1, 9],
    [3, 4, 6, 9],
    [6, 9, 6, 6],
    [9, 5, 8, 5],
  ])
);
