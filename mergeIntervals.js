// Given a collection of intervals, merge all overlapping intervals.

// Example 1:

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
// Example 2:

// Input: intervals = [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

// Constraints:

// intervals[i][0] <= intervals[i][1]

var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  console.log(intervals);
  let results = [intervals[0]];

  if (intervals.length <= 1) return intervals;

  for (let i = 0; i < intervals.length; i++) {
    if (
      intervals[i][0] <= results[results.length - 1][1] &&
      intervals[i][1] >= results[results.length - 1][1]
    ) {
      let popped = results.pop();
      results.push([popped[0], intervals[i][1]]);
    } else if (
      intervals[i][0] >= results[results.length - 1][0] &&
      intervals[i][1] <= results[results.length - 1][1]
    ) {
      let popped = results.pop();
      results.push([popped[0], popped[popped.length - 1]]);
    } else {
      results.push(intervals[i]);
    }
  }
  return results;
};

console.log(
  merge([
    [1, 4],
    [0, 4],
  ])
);

console.log(
  merge([
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18],
  ])
);
console.log(
  merge([
    [1, 4],
    [2, 4],
  ])
);
