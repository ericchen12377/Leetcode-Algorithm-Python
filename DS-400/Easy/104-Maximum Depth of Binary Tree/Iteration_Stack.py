# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            cur_depth, root = stack.pop()
            if root:
                depth = max(depth, cur_depth)
                stack.append((cur_depth + 1, root.left))
                stack.append((cur_depth + 1, root.right))
        return depth