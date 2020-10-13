var sortByBits = function (arr) {
  return mergeSort(arr);
};

function mergeSort(arr) {
  if (arr.length < 2) return arr;
  let mid = Math.floor(arr.length / 2);
  let left = arr.slice(0, mid);
  let right = arr.slice(mid);
  left = mergeSort(left);
  right = mergeSort(right);
  return merge(left, right);
}

function merge(left, right) {
  let merged = [];
  let left_copy = left.map((el) => [
    el
      .toString(2)
      .split("")
      .reduce((a, b) => +a + +b),
    el,
  ]);
  let right_copy = right.map((el) => [
    el
      .toString(2)
      .split("")
      .reduce((a, b) => +a + +b),
    el,
  ]);
  while (left_copy.length && right_copy.length) {
    if (left_copy[0][0] < right_copy[0][0]) {
      merged.push(left_copy.shift()[1]);
    } else if (left_copy[0][0] > right_copy[0][0]) {
      merged.push(right_copy.shift()[1]);
    } else {
      left_copy[0][1] < right_copy[0][1]
        ? merged.push(left_copy.shift()[1])
        : merged.push(right_copy.shift()[1]);
    }
  }
  merged.push(...left_copy.map((el) => el[1]));
  merged.push(...right_copy.map((el) => el[1]));
  return merged;
}
console.log(7 & 6, "#$##$#");
console.log(sortByBits([2, 3, 5, 7, 11, 13, 17, 19]));
