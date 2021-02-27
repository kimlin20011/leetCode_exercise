# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use dfs
# return the maxium number of the left or right subtree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root　== None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
