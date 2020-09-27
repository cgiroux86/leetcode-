var groupThePeople = function (groupSizes) {
  let results = [];
  let visited = new Set();
  for (let j in groupSizes) {
    let temp = [];
    let idx = groupSizes.length - 1;
    let target = groupSizes[j];

    while (temp.length < target && idx >= 0) {
      if (!visited.has(idx) && groupSizes[idx] === target) {
        visited.add(idx);
        temp.push(idx);
      }
      idx--;
    }
    if (temp.length === target) results.push(temp);
  }
  return results;
};

console.log(groupThePeople([2, 1, 3, 3, 3, 2]));
