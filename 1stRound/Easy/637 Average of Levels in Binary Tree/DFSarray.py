# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        self.getLevel(root, 0, res)
        return [sum(line) / float(len(line)) for line in res]
    
    def getLevel(self, root, level, res):
        if not root:
            return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.getLevel(root.left, level + 1, res)
        self.getLevel(root.right, level + 1, res)
