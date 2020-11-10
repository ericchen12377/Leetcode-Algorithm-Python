# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        stack = [(root),]
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                res += curr.val
            if curr.right:
                curr.right.val += curr.val * 10
                stack.append(curr.right)
            if curr.left:
                curr.left.val += curr.val * 10
                stack.append(curr.left)
        return res 