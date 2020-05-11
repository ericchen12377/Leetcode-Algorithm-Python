# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root, res, '' + str(root.val))
        return res
        
    def dfs(self, root, res, path):
        if root.left == None and root.right == None:
            res.append(path)
        if root.left != None:
            self.dfs(root.left, res, path + '->' + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, res, path + '->' + str(root.right.val))
