var canCompleteCircuit = function (gas, cost) {
  let start_idx = -1;
  let tank = 0;
  for (let i = 0; i < gas.length; i++) {
    tank += gas[i] - cost[i];
    if (tank >= 0) {
      if (start_idx < 0) {
        start_idx = i;
      }
    } else {
      start_idx = -1;
      tank = 0;
    }
  }
  for (let i = 0; i < start_idx; i++) {
    tank += gas[i] - cost[i];
    if (tank < 0) return -1;
  }

  return start_idx;
};
