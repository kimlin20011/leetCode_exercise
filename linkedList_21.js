/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
  //定義一個新的linkedList，設一個頭 dummyHead
  let dummyHead = new ListNode(0);
  let currentNode = dummyHead;
  //當l1 && l2有值的話
  while (l1 && l2) {
    //比較兩個最前面值的大小
    if (l1.val < l2.val) {
      //將l1的第一個值加進去
      currentNode.next = l1;
      l1 = l1.next; //講l1推移到下一個
    } else {
      //將l2的第一個值加進去
      currentNode.next = l2;
      l2 = l2.next; //講l2推移到下一個
    }
    currentNode = currentNode.next; //確認完後將currentNode往下移
  }

  //若l1或l2其中一個為null
  if (l1) {
    currentNode.next = l1; //若剩下l1有東西，直接將l1帶入linkedList
  } else if (l2) {
    currentNode.next = l2; //若剩下l2有東西，直接將l2帶入linkedList
  }

  return dummyHead.next; //回傳真實數列（去掉標頭）
};
