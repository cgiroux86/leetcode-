var flatten = function (head) {
  if (!head) return head;
  let stack = [head];
  let pickup_stack = [];
  while (stack.length) {
    let node = stack.pop();
    if (node.next) {
      stack.push(node.next);
    }
    if (!node.next && pickup_stack.length) {
      let popped = pickup_stack.pop();
      if (popped) {
        node.next = popped;
        popped.prev = node;
      }
    }
    if (node.child) {
      pickup_stack.push(node.next);
      stack.push(node.child);
      node.child.prev = node;
      node.next = node.child;
      node.child = null;
    }
  }
  return head;
};
