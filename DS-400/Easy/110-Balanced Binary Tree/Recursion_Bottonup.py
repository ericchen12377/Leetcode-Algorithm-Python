# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]
    def helper(self, root):
        if not root:
            return True, -1
        
        leftIsBalanced, leftHeight = self.helper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.helper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)