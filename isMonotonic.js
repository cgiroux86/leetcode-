var isMonotonic = function (A) {
  let direction = A[0] > A[1] ? 1 : A[0] === A[1] ? null : 0;
  for (let i = 1; i < A.length; ++i) {
    if (direction === null && getOrder(A[i], A[i + 1]) !== null) {
      direction = getOrder(A[i], A[i + 1]);
    }
    if (direction === 1 && A[i] < A[i + 1]) {
      return false;
    }
    if (direction === 0 && A[i] > A[i + 1]) {
      return false;
    }
  }
  return true;
};
function getOrder(x, y) {
  console.log("x", x, "y", y);
  return x < y ? 0 : x === y ? null : 1;
}

function isMonotonicOptimized(A) {
  let i = 0;
  let j = A.length - 1;
  let direction = null;

  while (i < j) {
    order = getOrder(A[i], A[j]);
    console.log("order", order, direction);
    if (direction === null && order !== null) direction = order;
    if (A[i] > A[j] && direction === 0) return false;
    if (A[i] < A[j] && direction === 1) return false;
    i++;
    j--;
  }
  if (A.length % 2) {
    return (direction === 0 && A[i] < A[i - 1]) ||
      (direction === 0 && A[i] > A[i + 1])
      ? false
      : (direction === 1 && A[i] > A[i - 1]) ||
        (direction === 1 && A[i] < A[i + 1])
      ? false
      : (direction === null && A[i] != A[i - 1]) ||
        (direction === null && A[i] != A[i + 1])
      ? false
      : true;
  }
  return true;
}

console.log(isMonotonicOptimized([3, 4, 2, 3]));
