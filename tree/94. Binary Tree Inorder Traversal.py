# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        valueSet = []

        def inorder(root):
            if root.val == None:
                return None
            # 先搜左邊
            if root.left != None:
                inorder(root.left)
            # 中間
            valueSet.append(root.val)
            # 再右邊
            if root.right != None:
                inorder(root.right)
        inorder(root)
        return valueSet
