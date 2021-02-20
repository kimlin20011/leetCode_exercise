/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */

var merge = function(intervals) {
  if (intervals.length <= 1) {
    return intervals;
  }
  //透過stack實作
  let stack = [];
  let top = null;
  //先將intervals排序，若回傳值為負，則a在b前；反之則b在a前
  intervals = intervals.sort((a, b) => a[0] - b[0]);
  //先代入第一組interval
  stack.push(intervals[0]);

  for (let i = 1; i < intervals.length; i++) {
    top = stack[stack.length - 1];
    //當前個interval第二個數小於後面的第一個數
    if (top[1] < intervals[i][0]) {
      //沒有overlap，直接加入
      stack.push(intervals[i]);
      //當前個interval第二個數大於等於後面的第一個數
    } else if (top[1] >= intervals[i][0]) {
      //有overlap，拿後面第二個數覆蓋前面第二個數
      //pop掉top再更新top
      top[1] = intervals[i][1];
      stack.pop();
      stack.push(top);
    }
  }
  return stack; //最後return完整的 stack
};
