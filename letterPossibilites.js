function numTilePossibilities(tiles, combos = new Set()) {
  // for (let i = 0; i < tiles.length; i++) {
  //   let str = tiles[i];
  //   combos.add(str);
  //   let new_str = str;
  //   for (let j = 0; j < tiles.length; j++) {
  //     if (j === i) continue;
  //     let short = str + tiles[j];
  //     new_str += tiles[j];
  //     combos.add(new_str);
  //     combos.add(short);
  //   }
  // }
  // return combos.size + 1;
}

console.log(numTilePossibilities("AAABBC"));
