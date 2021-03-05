# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t == None:
            return True
        if s == None and t == None:
            return True
        if s == None and t != None:
            return False
        return self.sameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)


"""
比較同一棵樹
檢查是不是subtree
檢查是不是同一棵樹



///preoreder 方法
treeValue  = []
streeValue = []
def preorder(node, traceTage):
    if s.val == None and traceTage == l:
        treeValue.append("lnull"）
    elif s.val == None and traceTage == r:
        treeValue.append("lnull"）
    else:
        treeValue.append(s.val)
        preorder(s.left)
        preorder(s.right)

"""
