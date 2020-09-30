var decompressRLElist = function (nums, pairs = []) {
  if (nums.length < 2) return pairs;
  return decompressRLElist(
    nums.slice(2),
    pairs.concat(new Array(nums[0]).fill(nums[1]))
  );
};
console.log(decompressRLElist([1, 2, 3, 4]));
