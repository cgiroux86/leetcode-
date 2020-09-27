function searchInsert(
  nums,
  target,
  start = 0,
  end = nums.length - 1,
  visited = new Set()
) {
  let mid = Math.floor((start + end + 1) / 2);
  if (start > end || target === nums[mid]) {
    return mid;
  }
  if (visited.has(mid)) {
    return target < nums[mid] ? mid - 1 : mid + 1;
  }
  if (target > nums[mid])
    return searchInsert(nums, target, mid + 1, end, visited);
  if (target < nums[mid])
    return searchInsert(nums, target, 0, mid - 1, visited);
}
console.log(searchInsert([1, 3, 5, 6], 2));
