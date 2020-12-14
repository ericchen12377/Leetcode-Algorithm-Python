# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root,p,q):
            
            if root in (None,p,q):
                return root
            
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            
            if left and right:
                return root
            else:
                return left or right
                
                
        node = dfs(root,p,q)
        
        return node
        