var groupAnagrams = function (strs) {
  const groups = new Map();
  for (let i = 0; i < strs.length; i++) {
    const sorted = strs[i].split("").sort();
    if (groups[sorted]) groups[sorted].push(strs[i]);
    else groups[sorted] = [strs[i]];
  }
  let results = [];
  for (let val of Object.values(groups)) results.push(val);
  return results;
};
