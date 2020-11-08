class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def BFS(node, level):
            if len(levels) == level:
                levels.append([])
            if level % 2 == 0:
                levels[level].append(node.val)
            elif level % 2 == 1:
                levels[level].insert(0,node.val)
            
            if node.left:
                BFS(node.left, level + 1)
            if node.right:
                BFS(node.right, level + 1)
        BFS(root, 0)
        return levels