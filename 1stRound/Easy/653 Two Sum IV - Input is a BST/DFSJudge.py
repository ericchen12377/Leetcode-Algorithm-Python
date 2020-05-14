# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = set()
        def inOrder(root):
            if not root:
                return False
            if k - root.val in res:
                return True
            res.add(root.val)
            return inOrder(root.left) or inOrder(root.right)
        return inOrder(root)
t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(6)
t1.left.left = TreeNode(2)
t1.left.right = TreeNode(4)
t1.right.right = TreeNode(7)
p = Solution()
print(p.findTarget(t1,9))
print(p.findTarget(t1,28))