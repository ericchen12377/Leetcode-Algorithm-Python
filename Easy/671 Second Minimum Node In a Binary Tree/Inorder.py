# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = set()
        self.inOrder(root)
        if len(self.res) <= 1:
            return -1
        min1 = min(self.res)
        self.res.remove(min1)
        return min(self.res)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.res.add(root.val)
        self.inOrder(root.right)
