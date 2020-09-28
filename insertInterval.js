// Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

// You may assume that the intervals were initially sorted according to their start times.

// Example 1:

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Example 2:

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
// Example 3:

// Input: intervals = [], newInterval = [5,7]
// Output: [[5,7]]
// Example 4:

// Input: intervals = [[1,5]], newInterval = [2,3]
// Output: [[1,5]]
// Example 5:

// Input: intervals = [[1,5]], newInterval = [2,7]
// Output: [[1,7]]

// Constraints:

// 0 <= intervals.length <= 104
// intervals[i].length == 2
// 0 <= intervals[i][0] <= intervals[i][1] <= 105
// intervals is sorted by intervals[i][0] in ascending order.
// newInterval.length == 2
// 0 <= newInterval[0] <= newInterval[1] <= 105

var insert = function (intervals, newInterval) {
  let results = [];
  let flag = false;
  let inserted = false;
  if (!intervals.length) return newInterval;
  for (let i = 0; i < intervals.length; i++) {
    if (isInterval(intervals[i], newInterval)) {
      let currInterval = [
        Math.min(intervals[i][0], newInterval[0]),
        Math.max(intervals[i][1], newInterval[1]),
      ];
      if (flag) results.pop();
      results.push(currInterval);
      newInterval = currInterval;
      flag = true;
      inserted = true;
    } else {
      results.push(intervals[i]);
      flag = false;
    }
  }
  if (!inserted) {
    if (newInterval[1] < results[results.length - 1][1]) {
      let popped = results.pop();
      results.push(newInterval);
      results.push(popped);
    } else {
      results.push(newInterval);
    }
  }
  return results.sort((a, b) => a - b);
};

function isInterval(arr1, arr2) {
  console.log(arr1, arr2);
  copy1 = arr1.slice();
  copy2 = arr2.slice();
  arr1 = copy1[1] < copy2[1] ? copy1 : copy2;
  arr2 = copy1[1] > copy2[1] ? copy1 : copy2;
  console.log(arr1, arr2, "sorted");
  if (arr2[0] <= arr1[1]) return true;
}

insert(
  [
    [1, 2],
    [3, 5],
    [6, 7],
    [8, 10],
    [12, 16],
  ],
  [4, 8]
);

insert([[1, 5]], [0, 0]);
