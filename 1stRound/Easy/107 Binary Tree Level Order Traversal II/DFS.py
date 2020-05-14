# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.levelOrder(root, res, 0)
        return res[::-1]
    
    def levelOrder(self, root, res, level):
        if not root: return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.levelOrder(root.left, res, level + 1)
        self.levelOrder(root.right, res, level + 1)
