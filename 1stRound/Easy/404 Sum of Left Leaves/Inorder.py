#Definition for a binary tree node.
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
        self.sum = 0
        self.inOrder(root)
        return self.sum

    def inOrder(self, root):
        if not root: return 
        if root.left: #on left judge whether it leaf
            self.inOrder(root.left)
            if not root.left.left and not root.left.right:
                self.sum += root.left.val
        if root.right: #on right continue recursion
            self.inOrder(root.right)
