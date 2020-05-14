#Definition for a binary tree node.
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
        return self.postOrder(root1) == self.postOrder(root2)
        
    def postOrder(self, root):
        stack = []
        stack.append(root)
        res = []
        while stack:
            node = stack.pop()
            if not node: continue
            stack.append(node.left)
            stack.append(node.right)
            if not node.left and not node.right:
                res.append(node.val)
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