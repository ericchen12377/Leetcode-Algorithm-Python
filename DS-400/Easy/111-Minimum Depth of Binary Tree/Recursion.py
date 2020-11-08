# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        child = [root.left, root.right]
        if not any(child):
            return 1
        min_depth = float("inf")
        for c in child:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1