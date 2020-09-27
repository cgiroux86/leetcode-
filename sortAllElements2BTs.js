var getAllElements = function (root1, root2) {
  let list = [];
  dft(root1, list);
  dft(root2, list);
  return list.sort((a, b) => a - b);
};

function dft(root, list) {
  if (!root) return;
  list.push(root.val);
  dft(root.left, list);
  dft(root.right, list);
}
