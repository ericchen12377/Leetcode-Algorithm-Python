# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(node):
            nonlocal count
            if not node.left and not node.right:
                count += 1
                return True
            isuni = True
            
            if node.left:
                isuni = helper(node.left) and isuni and node.left.val == node.val
            if node.right:
                isuni = helper(node.right) and isuni and node.right.val == node.val
            count += isuni
            return isuni
        count = 0
        helper(root)
        return count
            
        