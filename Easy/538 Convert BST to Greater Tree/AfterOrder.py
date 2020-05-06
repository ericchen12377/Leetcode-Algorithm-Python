# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def afterOrder(cur): #from right to node to left
            if not cur: return
            afterOrder(cur.right)
            self.sum += cur.val
            cur.val = self.sum
            afterOrder(cur.left)
        afterOrder(root)
        return root
