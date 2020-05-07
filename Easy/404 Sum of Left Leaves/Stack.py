# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack = []
        stack.append(root)
        leftsum = 0
        while stack:
            node = stack.pop()
            if not node: continue
            if node.left:
                if not node.left.left and not node.left.right:
                    leftsum += node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leftsum
