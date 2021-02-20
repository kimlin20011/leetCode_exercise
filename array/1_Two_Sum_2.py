class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i  # covert tuple into dictionary
        for j in range(len(nums)):
            value = target - nums[j]
            if value in dic:
                if j != dic[value]:
                    return [dic[value], j]
