# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t2:
            return t1
        if not t1:
            return t2
        newT = TreeNode(t1.val + t2.val)
        newT.left = self.mergeTrees(t1.left, t2.left)
        newT.right = self.mergeTrees(t1.right, t2.right)
        return newT



t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)
t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)
p = Solution()
newroot = p.mergeTrees(t1,t2)
print(newroot)
print(newroot.val)
print(newroot.left.val)
print(newroot.right.val)
print(newroot.left.left.val)