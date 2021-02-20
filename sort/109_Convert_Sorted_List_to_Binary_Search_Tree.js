/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
  //如果head沒有東西的話，回傳null（代表沒有點）
  if (!head) return null;
  //如果head的next沒有的話，直接回傳tree node（代表只有一個點）
  if (!head.next) return new TreeNode(head.val);
  //next
  let slow = head,
    fast = head,
    last = slow;
  while (fast.next && fast.next.next) {
    last = slow; //先儲存上一個節點的slow，之後用來驗證左邊
    slow = slow.next;
    fast = fast.next.next;
  }
  //右邊的開始
  fast = slow.next;
  //左邊的結束
  last.next = null;

  //將目前的node加進去
  let cur = new TreeNode(slow.val);
  //如果head = slow，表示slow沒有改變，左半邊不用遞迴
  if (head !== slow) cur.left = sortedListToBST(head);
  cur.right = sortedListToBST(fast);
  return cur;
};
