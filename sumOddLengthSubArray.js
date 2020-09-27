var sumOddLengthSubarrays = function (arr) {
  let dp = new Array(arr.length).fill(0);
  let total = 0;
  for (let i = 0; i < arr.length; i++) {
    if (i) dp[i] = [...dp].slice(0, i + 1);
  }
};
