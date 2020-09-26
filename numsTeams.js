var numTeams = function (rating) {
  let asc = new Array(rating.length).fill(0);
  let desc = new Array(rating.length).fill(0);
  let teams = 0;
  for (let i = rating.length - 1; i >= 0; i--) {
    for (let j = i + 1; j < rating.length; j++) {
      if (rating[i] < rating[j]) {
        desc[i] += 1;
        teams += desc[j];
      } else {
        asc[i] += 1;
        teams += asc[j];
      }
    }
  }
  return teams;
};
