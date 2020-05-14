# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getLeafs(root1) == self.getLeafs(root2)
    
    def getLeafs(self, root):
        res = []
        if not root:
            return res
        if not root.left and not root.right:
            return [root.val]
        res.extend(self.getLeafs(root.left))
        res.extend(self.getLeafs(root.right))
        return res

t1 = TreeNode(1)
t1.right = TreeNode(0)
t1.right.left = TreeNode(0)
t1.right.right = TreeNode(1)
t2 = TreeNode(1)
t2.left = TreeNode(0)
t2.right = TreeNode(1)
p = Solution()
print(p.leafSimilar(t1,t2))