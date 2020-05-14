# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.count = collections.Counter()
        self.inOrder(root)
        freq = max(self.count.values())
        res = []
        for item, c in self.count.items():
            if c == freq:
                res.append(item)
        return res
        
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        self.count[root.val] += 1
        self.inOrder(root.right)
