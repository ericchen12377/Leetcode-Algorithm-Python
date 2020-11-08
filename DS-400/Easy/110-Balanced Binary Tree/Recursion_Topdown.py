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
        def height(root):
            if not root:
                return -1
            return 1 + max(height(root.left), height(root.right))
        if not root:
            return True
        
        return abs(height(root.left) - height(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)