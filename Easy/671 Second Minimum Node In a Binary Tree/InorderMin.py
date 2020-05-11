# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        self.res = float("inf")
        self.min = root.val
        self.inOrder(root)
        return self.res if self.res != float("inf") else -1

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        if self.min < root.val < self.res:
            self.res = root.val
        self.inOrder(root.right)
