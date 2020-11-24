# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def DFSInorder(root):
            return DFSInorder(root.left) + [root.val] + DFSInorder(root.right) if root else []
        
        return DFSInorder(root)[k - 1]