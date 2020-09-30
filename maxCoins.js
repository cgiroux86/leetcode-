//3n piles, choose pi

var maxCoins = function (piles, total = 0) {
  piles = piles.sort((a, b) => b - a);
  return coins(piles, total);
  function coins(piles, total) {
    if (piles.length < 3) return total;
    return (
      piles[1] +
      coins(piles.slice(2, piles.length - 2).concat(piles.pop()), total)
    );
  }
};
// 8 + 6 + 4
// console.log(maxCoins([2,4,1,2,7,8]));
// 7 + 2
// [,,2]
