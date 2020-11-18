# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        levels = []
        if not root:
            return levels
        
        def BFS(node, level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                BFS(node.left, level + 1)
            if node.right:
                BFS(node.right, level + 1)
        BFS(root, 0)
        return [level[-1] for level in levels]
        