# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: # if not found, return None
            return None
        if root.val == val: #if found, return root
            return root
        elif root.val < val: #if less, continue right, if more, continue left
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
