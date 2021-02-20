class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):  # 訪問list中所有值 enumerate遍歷list中所有的值
            for j in range(i+1, len(nums), 1):
                if a + nums[j] == target:
                    return [i, j]
        raise Exception('No two sum solution')
