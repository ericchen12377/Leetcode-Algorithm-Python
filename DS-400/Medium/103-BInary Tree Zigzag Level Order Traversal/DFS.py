# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def DFS(node, level):
            if len(levels) <= level:
                levels.append([node.val])
            else:
                if level % 2 == 0:
                    levels[level].append(node.val)
                elif level % 2 == 1:
                    levels[level].insert(0, node.val)
            
            if node.left:
                DFS(node.left, level + 1)
            if node.right:
                DFS(node.right, level + 1)
        DFS(root, 0)
        return levels