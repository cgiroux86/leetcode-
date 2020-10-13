var countBattleships = function (board) {
  let visited = new Map();
  let battleships = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === "X" && !visited.get(`${[i, j]}`)) {
        findNeighbors(board, i, j, visited);
        battleships++;
        visited.set(`${[i, j]}`, true);
      } else if (board[i][j] === "X" && visited.get(`${[i, j]}`)) {
        findNeighbors(board, i, j, visited);
        visited.set(`${[i, j]}`, true);
      }
    }
  }

  return battleships;
};

function findNeighbors(board, i, j, visited) {
  if (i > 0) visited.set(`${[i - 1, j]}`, true);
  if (i < board.length - 1) visited.set(`${[i + 1, j]}`, true);
  if (j > 0) visited.set(`${[i, j - 1]}`, true);
  if (j < board[i].length - 1) visited.set(`${[i, j + 1]}`, true);
}

console.log(
  countBattleships([
    ["X", ".", ".", "X"],
    [".", ".", ".", "X"],
    [".", ".", ".", "X"],
  ])
);
