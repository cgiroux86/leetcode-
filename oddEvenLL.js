// Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

// You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

// Example 1:

// Input: 1->2->3->4->5->NULL
// Output: 1->3->5->2->4->NULL
// Example 2:

// Input: 2->1->3->5->6->4->7->NULL
// Output: 2->3->6->7->1->5->4->NULL

// Constraints:

// The relative order inside both the even and odd groups should remain as it was in the input.
// The first node is considered odd, the second node even and so on ...
// The length of the linked list is between [0, 10^4].

function TreeNode(val, next = null) {
  this.val = val;
  this.next = next;
}

var oddEvenList = function (head) {
  if (!head || !head.next) return head; // Watch out for edge cases! (0 or 1 item)

  // Core strategy: make 2 chains (odds/evens) by "leapfrogging".
  // No need to keep track of a counter or extra pointers, just need these 3:
  let odd = head;
  let even = head.next;
  const evenHead = head.next;

  // ("even.next" means more to go since even pointer is rightmost)
  // ("even &&" is there to avoid null reference error, but also for even positions)
  while (even && even.next) {
    odd.next = even.next;
    odd = odd.next;
    even.next = odd.next;
    even = even.next;
  }

  // Connect the two chains: (tail of odds to head of evens)
  odd.next = evenHead;

  return head;
};

var oddEvenList = function (head) {
  let curr = head;
  let slow = curr;
  let fast;
  let temp_head = head.next;
  let temp_slow = temp_head;
  let temp_fast;
  let temp_curr = temp_head;
  while (curr.next && curr.next.next) {
    slow = curr;
    fast = curr.next.next;
    slow.next = fast;
    curr = fast;
  }
  while (temp_curr.next && temp_curr.next.next) {
    temp_slow = temp_curr;
    temp_fast = temp_curr.next.next;
    console.log(temp_head);
    temp_slow.next = temp_fast;
    temp_curr = temp_fast;
  }
  console.log(temp_head);
  return head;
};

let vals = [1, 2, 3, 4, 5];
let i = 1;
let head = new TreeNode(vals[0]);
let temp = head;
while (i < vals.length) {
  temp.next = new TreeNode(vals[i]);
  temp = temp.next;
  i++;
}

console.log(oddEvenList(head));
