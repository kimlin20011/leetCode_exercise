# leetCode 筆記

# Linked List

- https://youtu.be/0czlvlqg5xw

* 使用快慢指針概念（Two pointers）
  - 兩個指針同向而行
  - 一快一慢，距離多少？
  - 兩個指針的移動速度

- 找中點：
  - 快指針速度為滿指針的兩倍。當快走終點(n/2)，慢指針當好走到中點(n/2)

```javascript=
function midpoint(list) {
  let fast = list.head;
  let slow = list.head;

  while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow; //回傳中點
}
```
