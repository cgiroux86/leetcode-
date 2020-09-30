var maxProduct = function (nums) {
  let dp = new Array(nums.length).fill(0);
  dp[0] = nums[0];
  let temp = dp[0];
  let curr_max = dp[0];
  let flag = false;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] < 0) {
      let t = temp * nums[i];
      dp[i] = Math.max(t, nums[i], dp[i - 1] * nums[i]);
    } else {
      dp[i] = Math.max(nums[i], dp[i - 1] * nums[i]);
    }
    curr_max = Math.max(curr_max, dp[i]);
    temp *= nums[i];
  }
  console.log(dp);
  return curr_max;
  //   let curr_max = nums[0];

  //   dp[0] = nums[0];
  //   for (let i = 1; i < nums.length; i++) {
  //     dp[i] = nums[i] * dp[i - 1];
  //     curr_max = Math.max(nums[i], dp[i]);
  //     console.log(curr_max);
  //   }
  //   console.log(dp);
  //   return curr_max;
};

console.log(maxProduct([2, 3, 2, -4]));
console.log(maxProduct([2, -5, -2, -4, 3]));
