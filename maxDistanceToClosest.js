var maxDistToClosest = function (seats) {
  let dp = new Array(seats.length).fill(0);
  function recurse(s, idx, cache) {
    for (let i = idx; i < s.length; i++) {
      if (!s[i]) {
        if (!cache[i]) {
          cache[i] = 1 + recurse(s, idx + 1, cache);
        }
      }
      dp[i] = cache[i];
    }

    // let max_distance = 0;
    // let seat_choices = new Array(seats.length).fill(0);
    // let prev_seats = 0;
    // for (let i = seats.length - 1; i >= 0; i--) {
    //   if (!seats[i]) {
    //     seat_choices[i] += prev_seats + 1;
    //     if (i < seats.length - 1) seat_choices[i + 1]++;
    //     prev_seats++;
    //   } else {
    //     if (i !== seats.length - 1) seat_choices[i + 1] = 1;
    //     prev_seats = 0;
    //   }
    // }
    // if (!seats[seats.length - 1] && seat_choices[seats.length - 2]) {
    //   seat_choices[seats.length - 1] = seat_choices[seats.length - 2] + 1;
    // }
    // return Math.max(...seat_choices);
  }
  recurse(seats, 0, {});
  console.log(dp);
};

console.log(maxDistToClosest([1, 0, 0, 0, 1, 0, 1]));

// var maxDistToClosest = function (seats) {
//   let max_idx = 0;
//   let seat_choices = new Array(seats.length).fill(0);
//   let prev_seats = 0;
//   for (let i = 0; i < seats.length; i++) {
//     if (!seats[i] && !seats[i - 1] && !seats[i + 1]) {
//       seat_choices[i] += prev_seats + 1;
//       prev_seats++;
//       max_idx = seat_choices[i] > seat_choices[max_idx] ? i : max_idx;
//     } else {
//       prev_seats = 0;
//     }
//   }
//   console.log(seat_choices);
//   return max_idx;
// };
