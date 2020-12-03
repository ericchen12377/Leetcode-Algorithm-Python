# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node, curLevel, res):
            if not node:
                return
            if curLevel >= len(res):
                res.append(node.val)
            if node.right:
                dfs(node.right, curLevel + 1, res)
            if node.left:
                dfs(node.left, curLevel + 1, res)
        dfs(root, 0, res)
        return res