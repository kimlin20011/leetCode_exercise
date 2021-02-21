class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
# compare from lager to small
# create  index1, index2, p = m-1, n-1, m+n-1

# while index1<0 and index2 < 0
# if nums1[index1]>= nums2[index2]
# swap (nums1[p] nums[index1])
# p--
# index1--
# else
# put nums2[index2] into nums1[p]
# p--

# put the rest number in num2 to num 1

        index1, index2, p = m-1, n-1, m+n-1

        if index1 < 0 and index2 < 0:
            return
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] >= nums2[index2]:
                nums1[p] = nums1[index1]
                p, index1 = p-1,  index1-1
            else:  # nums2 bigger
                nums1[p] = nums2[index2]
                p, index2 = p-1,  index2-1
        if index2 >= 0:
            nums1[:index2+1] = nums2[:index2+1]
