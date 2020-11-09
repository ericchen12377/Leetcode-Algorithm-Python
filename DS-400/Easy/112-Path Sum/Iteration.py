# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, sum - root.val),]
        while stack:
            node, cur_sum = stack.pop()
            if not node.left and not node.right and cur_sum == 0:
                return True
            if node.right:
                stack.append((node.right, cur_sum - node.right.val))
            if node.left:
                stack.append((node.left, cur_sum - node.left.val))
        return False