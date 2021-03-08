class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.tem = dict()
        return self.dfs(nums, len(nums) - 1)

    def dfs(self, nums, i):
        if i in self.tem:
            return self.tem[i]  # 回傳現有資料
        if i == 0:
            return nums[0]
        elif i == 1:  # 回傳第一筆資料跟第二筆最大的
            return max(nums[0], nums[1])
        else:
            self.tem[i] = max(self.dfs(nums, i-1), self.dfs(nums, i-2)+nums[i])
            return self.tem[i]


"""
value = {} # maxmium after visiting house[i]
def dynamic_prog:
n = len(nums)
if n < 0:
    return 0 
if dp[n] > 0:
    return dp[n]
return max(self.rob(n-2)+dp[n], self.rob(n-1))

"""
