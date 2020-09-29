function numTilePossibilities(tiles, combos = new Set()) {
  for (let i = 0; i < tiles.length; i++) {
    let str = tiles[i];
    combos.add(str);
    let new_str = str;
    for (let j = 0; j < tiles.length; j++) {
      if (j === i) continue;
      let short = str + tiles[j];
      new_str += tiles[j];
      combos.add(new_str);
      combos.add(short);
    }
  }
  return combos.size + 1;
  // combos = []
  // for (let i = 0; i < tiles.length; i++) {
  //   let str = tiles[i];
  //   combos.add(str);
  //   let j = 0;
  //   let new_str = str;
  //   while (j < tiles.length) {
  //     if (j === i) {
  //       j++;
  //       continue;
  //     }
  //     new_str += tiles[j];
  //     combos.add(new_str);
  //     console.log(new_str, str, j, i);
  //     j++;
  //   }
}

//   for (let i = 0; i < tiles.length; i++) {
//     let str = tiles[i];
//     combos.add(str);
//     for (let j = 0; j < tiles.length; j++) {
//       if (j === i) continue;
//       let new_str = str + tiles[j];
//       console.log(new_str);
//       if (!combos.has(new_str)) {
//         combos.add(new_str);
//       }
//       str = new_str;
//     }
//   }
//   return combos;

console.log(numTilePossibilities("AAABBC"));
