# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("inf")
        self.prev = None
        self.inOrder(root)
        return self.res

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        if self.prev:
            self.res = min(self.res, root.val - self.prev.val)
        self.prev = root
        self.inOrder(root.right)

t1 = TreeNode(1)
t1.right = TreeNode(3)
t1.right.left = TreeNode(2)
p = Solution()
print(p.getMinimumDifference(t1))