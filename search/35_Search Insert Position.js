/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var searchInsert = function(nums, target) {
  if (nums == null || nums.length == 0) {
    return 0;
  }
  let startTag = 0;
  let endTag = nums.length - 1;
  let mid = 0;
  while (startTag <= endTag) {
    mid = Math.floor((startTag + endTag) / 2);
    if (nums[mid] == target) return mid; //有匹配則回傳
    //target大於中位數
    if (nums[mid] >= target) endTag = mid - 1;
    else startTag = mid + 1; //target小於中位數
  }
  return startTag; //最後無匹配則回傳最後的mid值
};
