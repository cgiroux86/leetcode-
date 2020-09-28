var partitionLabels = function (S) {
  let chars = {};
  for (let i in S) {
    chars[S[i]] = i;
  }
  let curr_max = 0;
  let temp_total = 0;
  let results = [];
  for (let j in S) {
    curr_max = Math.max(curr_max, chars[S[j]]);
    temp_total++;
    if (curr_max == j) {
      results.push(temp_total);
      temp_total = 0;
      curr_max = 0;
    }
  }
  return results;
};
