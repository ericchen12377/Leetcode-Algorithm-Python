# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        queue = []
        queue.append(root)
        while queue:
            current = queue[0]
            queue = queue[1:]
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return root
        