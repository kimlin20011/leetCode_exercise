# 用greedy解，前面的結果不影響後面的答案
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        number = len(nums)
        if number < 2:
            return number
        preDif = nums[1] - nums[0]
        count = 1 if preDif == 0 else 2  # 若前兩數相等，算一個數，否則算2個數
        for i in range(2, number):
            dif = nums[i] - nums[i-1]
            if (preDif >= 0 and dif < 0) or (preDif <= 0 and dif > 0):
                count += 1
                preDif = dif
        return count
