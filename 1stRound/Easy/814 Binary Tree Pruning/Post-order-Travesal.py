# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root


t1 = TreeNode(1)
t1.right = TreeNode(0)
t1.right.left = TreeNode(0)
t1.right.right = TreeNode(1)

p = Solution()
newroot = p.pruneTree(t1)
print(newroot)
print(newroot.val)
print(newroot.right.val)
print(newroot.right.left)
print(newroot.right.right.val)


t2 = TreeNode(1)
t2.left = TreeNode(0)
t2.right = TreeNode(1)
t2.left.left = TreeNode(0)
t2.left.right = TreeNode(0)
t2.right.left = TreeNode(0)
t2.right.right = TreeNode(1)

p = Solution()
newroot = p.pruneTree(t2)
print(newroot)
print(newroot.val)
print(newroot.right.val)
print(newroot.right.left)
print(newroot.right.right.val)