# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            vals.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return min([vals[i + 1] - vals[i] for i in range(len(vals) - 1)])
