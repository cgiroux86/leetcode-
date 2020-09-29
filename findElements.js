var FindElements = function (root) {
  root.val = 0;
  this.root = root;
  let stack = [[root, 0]];
  while (stack.length) {
    let curr = stack.pop();
    if (curr[0] && curr[0].left) {
      curr[0].left.val = 2 * curr[1] + 1;
      stack.push([curr[0].left, curr[0].left.val]);
    }
    if (curr[0] && curr[0].right) {
      curr[0].right.val = 2 * curr[1] + 2;
      stack.push([curr[0].right, curr[0].right.val]);
    }
  }
};

/**
 * @param {number} target
 * @return {boolean}
 */
FindElements.prototype.find = function (target, start_node = null) {
  let stack = [this.root];
  while (stack.length) {
    let curr = stack.pop();
    if (curr.val === target) return true;
    if (curr.left) stack.push(curr.left);
    if (curr.right) stack.push(curr.right);
  }
  return false;
};
